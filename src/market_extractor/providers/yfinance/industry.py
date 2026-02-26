import yfinance as yf

class Industry:
    def __init__(self, industry):
        self.industry = yf.Industry(industry)

    @property
    def key(self):
        return self.industry.key

    @property
    def name(self):
        return self.industry.name

    @property
    def overview(self):
        return self.industry.overview

    @property
    def research_reports(self):
        return self.industry.research_reports

    @property
    def sector_key(self):
        return self.industry.sector_key

    @property
    def sector_name(self):
        return self.industry.sector_name

    @property
    def symbol(self):
        return self.industry.symbol

    @property
    def ticker(self):
        return self.industry.ticker

    @property
    def top_companies(self):
        return self.industry.top_companies

    @property
    def top_growth_companies(self):
        return self.industry.top_growth_companies

    @property
    def top_performing_companies(self):
        return self.industry.top_performing_companies