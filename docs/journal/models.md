finance Ticker.
db_create.py
+1
from sqlalchemy import text
import pandas as pdfrom sqlalchemy import text
db_create.py
+44
        return int(ticker_id)
        return int(ticker_id)def load_ohlcv_bulk(    engine: Engine,    *,
db_create.py
+4
-8
    # Map yfinance columns (Open/High/Low/Close/Volume, Date/Datetime) to schema    df = df.copy()    df = df.rename(columns={    })    date_col = "date" if "date" in df.columns else ("Datetime" if "Datetime" in df.columns else "Date")
    df = df.copy()    date_col = "date" if "date" in df.columns else ("Datetime" if "Datetime" in df.columns else "Date")    df = df.reset_index() if df.index.name in ("Date", "Datetime") else df    if "date" not in df.columns and "Date" in df.columns:        df = df.rename(columns={"Date": "date"})    elif "date" not in df.columns and "Datetime" in df.columns:        df = df.rename(columns={"Datetime": "date"})    df = df[["date", "open", "high", "low", "close", "volume"]]    # Map yfinance columns (Open/High/Low/Close/Volume, Date/Datetime) to schema    df = df.rename(columns={    })
ticker.py
+11
-3
import yfinance as yf
from __future__ import annotationsfrom typing import TYPE_CHECKINGimport datetimeimport yfinance as yf
ticker.py
+17
    def save_ohlcv(        self,        engine: Engine,        ticker_id: int,        interval: str = "1d",
Here’s what’s in place

Here’s what’s in place:

## Recommendation: keep them separate, add a sync method

**yfinance Ticker** = data source (API client)  
**db Ticker** = persistence model (ORM)

They stay separate, but the yfinance Ticker now has a `save_ohlcv()` method that syncs data into Postgres.

## What was added

**1. `load_ohlcv_bulk`** in `db_create.py` – bulk insert OHLCV from a DataFrame with `ON CONFLICT DO NOTHING`.

**2. `save_ohlcv()`** on the yfinance Ticker – fetches OHLCV and writes it to the DB:

```python
from market_extractor.providers.yfinance import Ticker
from market_extractor.db._engine import make_engine

ticker = Ticker("AAPL")
engine = make_engine()

# Fetch from yfinance and load into Postgres (ticker_id from core.ticker)
rows = ticker.save_ohlcv(engine, ticker_id=1, interval="1d")
# Or with date range:
rows = ticker.save_ohlcv(engine, ticker_id=1, interval="1d", from_date="2024-01-01", to_date="2024-12-31")
```

## Flow

1. `core.ticker` holds tickers (via `create_ticker` or the ORM).
2. yfinance Ticker fetches OHLCV from Yahoo.
3. `save_ohlcv()` writes into `data.ohlcv` using the existing `ticker_id`.

The SQLAlchemy Ticker model is used by the DB layer; the yfinance Ticker only needs `ticker_id` and `engine` to sync. No merging of the two classes.