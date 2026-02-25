CREATE SCHEMA IF NOT EXISTS core;
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS analytics;
CREATE SCHEMA IF NOT EXISTS meta;

CREATE TABLE IF NOT EXISTS core.market (
  market_id  BIGSERIAL PRIMARY KEY,
  code       TEXT NOT NULL UNIQUE,          -- e.g. NASDAQ, NYSE, BINANCE
  name       TEXT NOT NULL,                 -- human name
  mic        TEXT,                          -- optional ISO MIC code
  timezone   TEXT NOT NULL DEFAULT 'UTC',   -- e.g. America/New_York
  country    TEXT,
  currency   TEXT                           -- e.g. USD, SEK
);


DO $$
BEGIN
  CREATE TYPE core.asset_class AS ENUM (
    'equity',
    'etf',
    'crypto',
    'fx',
    'index',
    'future',
    'option',
    'bond',
    'other'
  );
EXCEPTION
  WHEN duplicate_object THEN NULL;
END $$;

CREATE TABLE IF NOT EXISTS core.symbol (
  symbol_id       BIGSERIAL PRIMARY KEY,
  symbol_code     TEXT NOT NULL UNIQUE,     -- canonical symbol
  name            TEXT,
  asset_class     core.asset_class NOT NULL DEFAULT 'equity',
  base_currency   TEXT,
  quote_currency  TEXT,
  is_active       BOOLEAN NOT NULL DEFAULT TRUE,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS core.listing (
  listing_id    BIGSERIAL PRIMARY KEY,

  market_id     BIGINT NOT NULL REFERENCES core.market(market_id) ON DELETE RESTRICT,
  symbol_id     BIGINT NOT NULL REFERENCES core.symbol(symbol_id) ON DELETE RESTRICT,

  local_ticker  TEXT NOT NULL,             -- e.g. AAPL, VOLV-B.ST
  isin         TEXT,
  currency     TEXT,
  start_date   DATE,
  end_date     DATE,

  is_active    BOOLEAN NOT NULL DEFAULT TRUE,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT now(),

  CONSTRAINT uq_listing_market_local UNIQUE (market_id, local_ticker),
  CONSTRAINT uq_listing_market_symbol UNIQUE (market_id, symbol_id)
);

CREATE INDEX IF NOT EXISTS ix_listing_symbol_id ON core.listing(symbol_id);
CREATE INDEX IF NOT EXISTS ix_listing_market_id ON core.listing(market_id);

DO $$
BEGIN
  CREATE TYPE raw.timeframe AS ENUM ('1m','5m','15m','1h','4h','1d','1w');
EXCEPTION
  WHEN duplicate_object THEN NULL;
END $$;

CREATE TABLE IF NOT EXISTS raw.ohlcv (
  listing_id   BIGINT NOT NULL REFERENCES core.listing(listing_id) ON DELETE RESTRICT,
  tf           raw.timeframe NOT NULL,
  ts           TIMESTAMPTZ NOT NULL,

  open         DOUBLE PRECISION,
  high         DOUBLE PRECISION,
  low          DOUBLE PRECISION,
  close        DOUBLE PRECISION,
  volume       DOUBLE PRECISION,

  source       TEXT,                           -- yfinance, stooq, etc
  ingested_at  TIMESTAMPTZ NOT NULL DEFAULT now(),

  PRIMARY KEY (listing_id, tf, ts),

  CONSTRAINT chk_ohlcv_high_low CHECK (high IS NULL OR low IS NULL OR high >= low),
  CONSTRAINT chk_ohlcv_nonneg_volume CHECK (volume IS NULL OR volume >= 0)
);

CREATE INDEX IF NOT EXISTS ix_ohlcv_listing_tf_ts_desc
  ON raw.ohlcv(listing_id, tf, ts DESC);