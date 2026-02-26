import yfinance as yf

SECTORS = [
    "basic-materials",
    "communication-services",
    "consumer-cyclical",
    "consumer-defensive",
    "energy",
    "financial-services",
    "healthcare",
    "industrials",
    "real-estate",
    "technology",
    "information-technology",
    "materials",
    "telecommunication-services",
    "utilities",
]

class Sector:
    def __init__(self, sector):
        if sector not in SECTORS:
            raise ValueError(f"Invalid sector: {sector}")
            
        self.sector = yf.Sector(sector)

    @property
    def key(self):
        return self.sector.key

    @property
    def name(self):
        return self.sector.name

    @property
    def overview(self):
        return self.sector.overview

    @property
    def research_reports(self):
        return self.sector.research_reports

    @property
    def symbol(self):
        return self.sector.symbol

    @property
    def ticker(self):
        return self.sector.ticker

    @property
    def top_companies(self):
        return self.sector.top_companies

    @property
    def top_etfs(self):
        return self.sector.top_etfs

    @property
    def top_mutual_funds(self):
        return self.sector.top_mutual_funds

    @property
    def industries(self):
        return self.sector.industries