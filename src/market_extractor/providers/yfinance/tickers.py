import yfinance as yf
# import datetime

class Tickers:
    def __init__(self, tickers: list[str]):
        self.tickers = yf.Tickers(tickers)

    ###################################
    # Data fetchers
    ###################################
    def get_data(self, interval: str = "1d", from_date: str = None, to_date: str = None):
        try:
            historical_data = self.tickers.history(start=from_date, end=to_date, interval=interval)
            return historical_data
        except Exception as e:
            print(f"Error getting data: {e}")
            return None

    @property
    def news(self):
        return self.tickers.news()