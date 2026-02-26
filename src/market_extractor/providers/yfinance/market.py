import yfinance as yf
from typing import Literal

MARKETS = ["US", "GB", "ASIA", "EUROPE", "RATES", "COMMODITIES", "CURRENCIES", "CRYPTOCURRENCIES"]
MarketType = Literal["US", "GB", "ASIA", "EUROPE", "RATES", "COMMODITIES", "CURRENCIES", "CRYPTOCURRENCIES"]

class Market:
    def __init__(self, market: MarketType):
        if market not in MARKETS:
            raise ValueError(f"market must be one of {MARKETS}, got {market!r}")
        self.market = yf.Market(market)
        self.status = self.market.status
        self.summary = self.market.summary

