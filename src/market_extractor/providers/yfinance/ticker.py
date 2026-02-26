import yfinance as yf
import requests

s = requests.Session()

class Ticker:
    def __init__(self, ticker: str):
        self.ticker = yf.Ticker(ticker, session=s)

    @property
    def actions(self):
        return self.ticker.actions

    @property
    def analyst_price_targets(self):
        return self.ticker.analyst_price_targets

    @property
    def balance_sheet(self):
        return self.ticker.balance_sheet

    @property
    def balancesheet(self):
        return self.ticker.balancesheet

    @property
    def calendar(self):
        return self.ticker.calendar

    @property
    def capital_gains(self):
        return self.ticker.capital_gains

    @property
    def cash_flow(self):
        return self.ticker.cash_flow

    @property
    def cashflow(self):
        return self.ticker.cashflow

    @property
    def dividends(self):
        return self.ticker.dividends

    @property
    def earnings(self):
        return self.ticker.earnings

    @property
    def earnings_dates(self):
        return self.ticker.earnings_dates

    @property
    def earnings_estimate(self):
        return self.ticker.earnings_estimate

    @property
    def earnings_history(self):
        return self.ticker.earnings_history

    @property
    def eps_revisions(self):
        return self.ticker.eps_revisions

    @property
    def eps_trend(self):
        return self.ticker.eps_trend

    @property
    def fast_info(self):
        return self.ticker.fast_info

    @property
    def financials(self):
        return self.ticker.financials

    @property
    def funds_data(self):
        return self.ticker.funds_data

    @property
    def growth_estimates(self):
        return self.ticker.growth_estimates

    @property
    def history_metadata(self):
        return self.ticker.history_metadata

    @property
    def income_stmt(self):
        return self.ticker.income_stmt

    @property
    def incomestmt(self):
        return self.ticker.incomestmt

    @property
    def info(self):
        return self.ticker.info

    @property
    def insider_purchases(self):
        return self.ticker.insider_purchases

    @property
    def insider_roster_holders(self):
        return self.ticker.insider_roster_holders

    @property
    def insider_transactions(self):
        return self.ticker.insider_transactions

    @property
    def institutional_holders(self):
        return self.ticker.institutional_holders

    @property
    def isin(self):
        return self.ticker.isin

    @property
    def major_holders(self):
        return self.ticker.major_holders

    @property
    def mutualfund_holders(self):
        return self.ticker.mutualfund_holders

    @property
    def news(self):
        return self.ticker.news

    @property
    def options(self):
        return self.ticker.options

    @property
    def quarterly_balance_sheet(self):
        return self.ticker.quarterly_balance_sheet

    @property
    def quarterly_balancesheet(self):
        return self.ticker.quarterly_balancesheet

    @property
    def quarterly_cash_flow(self):
        return self.ticker.quarterly_cash_flow

    @property
    def quarterly_cashflow(self):
        return self.ticker.quarterly_cashflow

    @property
    def quarterly_earnings(self):
        return self.ticker.quarterly_earnings

    @property
    def quarterly_financials(self):
        return self.ticker.quarterly_financials

    @property
    def quarterly_income_stmt(self):
        return self.ticker.quarterly_income_stmt

    @property
    def quarterly_incomestmt(self):
        return self.ticker.quarterly_incomestmt

    @property
    def recommendations(self):
        return self.ticker.recommendations

    @property
    def recommendations_summary(self):
        return self.ticker.recommendations_summary

    @property
    def revenue_estimate(self):
        return self.ticker.revenue_estimate

    @property
    def sec_filings(self):
        return self.ticker.sec_filings

    @property
    def shares(self):
        return self.ticker.shares

    @property
    def splits(self):
        return self.ticker.splits

    @property
    def sustainability(self):
        return self.ticker.sustainability

    @property
    def ttm_cash_flow(self):
        return self.ticker.ttm_cash_flow

    @property
    def ttm_cashflow(self):
        return self.ticker.ttm_cashflow

    @property
    def ttm_financials(self):
        return self.ticker.ttm_financials

    @property
    def ttm_income_stmt(self):
        return self.ticker.ttm_income_stmt

    @property
    def ttm_incomestmt(self):
        return self.ticker.ttm_incomestmt

    @property
    def upgrades_downgrades(self):
        return self.ticker.upgrades_downgrades