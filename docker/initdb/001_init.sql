CREATE SCHEMA IF NOT EXISTS core;
CREATE SCHEMA IF NOT EXISTS data;

DO $$
BEGIN
  CREATE TYPE core.yf_code AS ENUM (
    'NMS',   -- Nasdaq
    'NYQ',   -- NYSE
    'LON',   -- London Stock Exchange
    'FRA',   -- Frankfurt Stock Exchange
    'STO',   -- Stockholm Stock Exchange
    'PAR',   -- Paris Stock Exchange
    'TYO',   -- Tokyo Stock Exchange
    'HKG',   -- Hong Kong Stock Exchange
    'TSE'    -- Toronto Stock Exchange
  );
EXCEPTION
  WHEN duplicate_object THEN NULL;
END $$;

DO $$
BEGIN
  CREATE TYPE core.asset AS ENUM (
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

DO $$
BEGIN
  CREATE TYPE core.sector AS ENUM (
    'energy',
    'materials',
    'industrials',
    'consumer_discretionary',
    'consumer_staples',
    'health_care',
    'financials',
    'information_technology',
    'communication_services',
    'utilities',
    'real_estate',
    'other'
  );
EXCEPTION
  WHEN duplicate_object THEN NULL;
END $$;

DO $$
BEGIN
  CREATE TYPE core.industry AS ENUM (
    'aerospace_defense',
    'automobiles',
    'banks',
    'biotechnology',
    'software',
    'capital_goods',
    'consumer_services',
    'energy',
    'health_care_equipment',
    'insurance',
    'materials',
    'media_entertainment',
    'pharmaceuticals',
    'real_estate',
    'retailing',
    'semiconductors',
    'technology_hardware',
    'telecommunications',
    'transportation',
    'utilities',
    'other'
  );
EXCEPTION
  WHEN duplicate_object THEN NULL;
END $$;

CREATE TABLE IF NOT EXISTS core.market (
    market_id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    code core.yf_code NOT NULL,
    timezone TEXT NOT NULL DEFAULT 'UTC',
    country TEXT,
    currency TEXT
);

CREATE TABLE IF NOT EXISTS core.ticker (
    ticker_id BIGSERIAL PRIMARY KEY,
    market_id BIGINT NOT NULL REFERENCES core.market(market_id) ON DELETE RESTRICT,
    
    name TEXT NOT NULL,
    symbol TEXT NOT NULL UNIQUE,
    asset core.asset NOT NULL DEFAULT 'equity',
    sector core.sector NOT NULL DEFAULT 'other',
    industry core.industry NOT NULL DEFAULT 'other'
);

Data (timeframe, ohlcv) 
DO $$
BEGIN
  CREATE TYPE data.timeframe AS ENUM (
    '1m','5m','15m','1h','4h','1d','1w'
  );
EXCEPTION
  WHEN duplicate_object THEN NULL;
END $$;

CREATE TABLE IF NOT EXISTS data.ohlcv (
    ticker_id BIGINT NOT NULL REFERENCES core.ticker(ticker_id) ON DELETE RESTRICT,
    timeframe data.timeframe NOT NULL,
    date TIMESTAMPTZ NOT NULL,

    open DOUBLE PRECISION,
    high DOUBLE PRECISION,
    low DOUBLE PRECISION,
    close DOUBLE PRECISION,
    volume DOUBLE PRECISION

    PRIMARY KEY (ticker_id, timeframe, date),
)