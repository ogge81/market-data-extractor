from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from sqlalchemy import text
from sqlalchemy.engine import Engine


@dataclass(frozen=True)
class ListingRef:
    listing_id: int
    market_code: str
    local_ticker: str
    symbol_code: str


def get_or_create_market(
    engine: Engine,
    *,
    code: str,
    name: Optional[str] = None,
    timezone: str = "UTC",
    country: Optional[str] = None,
    currency: Optional[str] = None,
    mic: Optional[str] = None,
) -> int:
    """
    Returns market_id. Creates if missing.
    """
    code = code.strip().upper()
    if not name:
        name = code

    sql = text(
        """
        INSERT INTO core.market(code, name, mic, timezone, country, currency)
        VALUES (:code, :name, :mic, :timezone, :country, :currency)
        ON CONFLICT (code) DO UPDATE
          SET name = EXCLUDED.name
        RETURNING market_id;
        """
    )

    # If conflict triggers, RETURNING works for DO UPDATE.
    with engine.begin() as conn:
        market_id = conn.execute(
            sql,
            dict(code=code, name=name, mic=mic, timezone=timezone, country=country, currency=currency),
        ).scalar_one()

    return int(market_id)


def get_or_create_symbol(
    engine: Engine,
    *,
    symbol_code: str,
    name: Optional[str] = None,
    asset_class: str = "equity",
    base_currency: Optional[str] = None,
    quote_currency: Optional[str] = None,
) -> int:
    symbol_code = symbol_code.strip().upper()

    sql = text("""
        INSERT INTO core.symbol(symbol_code, name, asset_class, base_currency, quote_currency)
        VALUES (:symbol_code, :name, :asset_class, :base_currency, :quote_currency)
        ON CONFLICT (symbol_code) DO UPDATE
          SET name = COALESCE(EXCLUDED.name, core.symbol.name),
              base_currency = COALESCE(EXCLUDED.base_currency, core.symbol.base_currency),
              quote_currency = COALESCE(EXCLUDED.quote_currency, core.symbol.quote_currency),
              is_active = TRUE
        RETURNING symbol_id;
    """)

    with engine.begin() as conn:
        symbol_id = conn.execute(
            sql,
            {
                "symbol_code": symbol_code,
                "name": name,
                "asset_class": asset_class,   # 'equity' etc
                "base_currency": base_currency,
                "quote_currency": quote_currency,
            },
        ).scalar_one()

    return int(symbol_id)


def get_or_create_listing(
    engine: Engine,
    *,
    market_code: str,
    symbol_code: str,
    local_ticker: Optional[str] = None,
    listing_currency: Optional[str] = None,
) -> ListingRef:
    """
    Returns ListingRef(listing_id, market_code, local_ticker, symbol_code).
    Creates market+symbol if needed, then listing.

    local_ticker defaults to symbol_code (common case for US equities).
    """
    market_code = market_code.strip().upper()
    symbol_code = symbol_code.strip().upper()
    if not local_ticker:
        local_ticker = symbol_code
    local_ticker = local_ticker.strip().upper()

    # Ensure dimensions exist
    market_id = get_or_create_market(engine, code=market_code, name=market_code)
    symbol_id = get_or_create_symbol(engine, symbol_code=symbol_code, name=None)

    # Insert listing; if exists, just fetch its id
    insert_sql = text(
        """
        INSERT INTO core.listing(market_id, symbol_id, local_ticker, currency)
        VALUES (:market_id, :symbol_id, :local_ticker, :currency)
        ON CONFLICT (market_id, local_ticker) DO UPDATE
          SET symbol_id = EXCLUDED.symbol_id,
              currency = COALESCE(EXCLUDED.currency, core.listing.currency),
              is_active = TRUE
        RETURNING listing_id;
        """
    )

    with engine.begin() as conn:
        listing_id = conn.execute(
            insert_sql,
            dict(market_id=market_id, symbol_id=symbol_id, local_ticker=local_ticker, currency=listing_currency),
        ).scalar_one()

    return ListingRef(
        listing_id=int(listing_id),
        market_code=market_code,
        local_ticker=local_ticker,
        symbol_code=symbol_code,
    )