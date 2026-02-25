# Structure

## Folder structure

```
docker/
    docker-compose.yml
    initdb/
        001_schema.sql

notebooks/
    00_sandbox.ipynb
    01_extract.ipynb
    02_load.ipynb
    00_transform.ipynb

scripts/
    main_scripts.py

tests/
    main_tests.py

src/
    market_extractor/
    __init__.py
    config.py
    logging.py

    db/
        __init__.py
        engine.py
        migrations.py
        models.py

    extract/
        __init__.py
        providers/
            yf_provider.py

    load/
        __init__.py

    utils/
        __init__.py
        time_utils.py
        files_utils.py
        data_utils.py


    pipelines/
        __init__.py

```

## Database Schemas

### Core (market, ticker, asset, yf_code) 

```SQL
core.asset ENUM (
    'equity',
    'etf',
    'crypto',
    'fx',
    'index',
    'future',
    'option',
    'bond',
    'other'
)

core.yf_code ENUM (
    "NMS", -- "Nasdaq",
    "NYQ", -- "NYSE",
    "LON", -- "London Stock Exchange",
    "FRA", -- "Frankfurt Stock Exchange",
    "STO", -- "Stockholm Stock Exchange",
    "PAR", -- "Paris Stock Exchange",
    "TYO", -- "Tokyo Stock Exchange",
    "HKG", -- "Hong Kong Stock Exchange",
    "TSE", -- "Toronto Stock Exchange",
)

core.market (
    market_id: BIGSERIAL PRIMARY KEY,
    name: TEXT NOT NULL,
    code: core.yf_code NOT NULL,
    timezone: TEXT NOT NULL DEFAULT 'UTC',
    country: TEXT,
    currency: TEXT
)

core.ticker (
    ticker_id: BIGSERIAL PRIMARY KEY,
    market_id: BIGINT NOT NULL REFERENCES core.market(market_id) ON DELETE RESTRICT,

    name: TEXT NOT NULL,
    symbol: TEXT NOT NULL UNIQUE,
    industry: TEXT NOT NULL,
    sector: TEXT NOT NULL,
    asset: core.asset_class NOT NULL DEFAULT 'equity',
)
```

### Data (timeframe, ohlcv) 

``` SQL
data.timeframe ENUM (
    '1m','5m','15m','1h','4h','1d','1w'
)

data.ohlcv (
    ticker_id: BIGINT NOT NULL REFERENCES core.ticker(ticker_id) ON DELETE RESTRICT
    timeframe: data.timeframe NOT NULL

    date: TIMESTAMPTZ NOT NULL
    open: DOUBLE PRECISION
    high: DOUBLE PRECISION
    low: DOUBLE PRECISION
    close: DOUBLE PRECISION
)
```



## Wireframe