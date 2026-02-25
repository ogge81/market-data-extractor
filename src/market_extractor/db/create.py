from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from sqlalchemy import text
from sqlalchemy.engine import Engine
from .engine import make_engine

def create_market(
    engine: Engine, 
    *, 
    name: str, 
    code: str, 
    country: str = "US", 
    currency: str = "USD",
    timezone: str = "UTC"
    ) -> int:

    sql = """
        INSERT INTO core.market(name, code, country, currency, timezone)
        VALUES (:name, :code, :country, :currency, :timezone)
        RETURNING market_id
    """

    with engine.connect() as conn:
        market_id = conn.execute(
            text(sql),
            dict(
                name=name, 
                code=code, 
                country=country, 
                currency=currency, 
                timezone=timezone
                )).scalar_one()
        conn.commit()
        return int(market_id)

def create_ticker(
    engine: Engine, 
    *, 
    market_id: int, 
    name: str,
    symbol: str, 
    asset: str = "equity", 
    sector: str = "other", 
    industry: str = "other"
    ) -> int:

    sql = text("""
        INSERT INTO core.ticker(market_id, name, symbol, asset, sector, industry) 
        VALUES (:market_id, :name, :symbol, :asset, :sector, :industry)
        RETURNING ticker_id
    """)

    with engine.connect() as conn:
        ticker_id = conn.execute(
            sql, 
            dict(
                market_id=market_id, 
                name=name, 
                symbol=symbol, 
                asset=asset, 
                sector=sector, 
                industry=industry
                )).scalar_one()
        conn.commit()
        return int(ticker_id)