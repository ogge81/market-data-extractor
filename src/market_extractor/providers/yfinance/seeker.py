import yfinance as yf

class Seeker:
    def __init__(self, query, max_results=8, news_count=8):
        self.query = query
        self.max_results = max_results
        self.news_count = news_count

    @property
    def search_quotes(self):
        return yf.Search(
            query=self.query,
            max_results=self.max_results,
            news_count=self.news_count
        ).quotes

    @property
    def search_news(self):
        return yf.Search(
            query=self.query,
            max_results=self.max_results,
            news_count=self.news_count
        ).news
    
    ## LOOKUP - Stocks etc
    def lookup(
            self, 
            query: str | None = None, 
            type: str | None = None,
            count: int | None = None
        ):

        if query:
            self.query = query

        if type == "stock":
            if count:
                return yf.Lookup(query=self.query).get_stock(count=count)
            else:
                return yf.Lookup(query=self.query).stock

        elif type == "etf":
            if count:
                return yf.Lookup(query=self.query).get_etf(count=count)
            else:
                return yf.Lookup(query=self.query).etf
        elif type == "crypto":
            if count:
                return yf.Lookup(query=self.query).get_cryptocurrency(count=count)
            else:
                return yf.Lookup(query=self.query).cryptocurrency
        elif type == "index":
            if count:
                return yf.Lookup(query=self.query).get_index(count=count)
            else:
                return yf.Lookup(query=self.query).index
        else:
            if count:
                return yf.Lookup(query=self.query).get_all(count=count)
            else:
                return yf.Lookup(query=self.query).all

