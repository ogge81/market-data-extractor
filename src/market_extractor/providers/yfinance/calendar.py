import yfinance as yf

class Calendar:
    def __init__(self, start_date: str, end_date: str):
        if start_date and end_date:
            self.calendar = yf.Calendars(start = start_date, end = end_date)
        else:
            self.calendar = yf.Calendars()

    def earnings_calendar(
            self, 
            market_cap: float | None = None, 
            filter_most_active: bool = True, 
            start=None, 
            end=None, 
            limit=12, 
            offset=0, 
            force=False
        ):
        try:

            return self.calendar.get_earnings_calendar(
                market_cap = market_cap, 
                filter_most_active = filter_most_active, 
                start = start, 
                end = end, 
                limit = limit, 
                offset = offset, 
                force = force
            )
        except Exception as e:
            print(f"Error getting earnings calendar: {e}")
            return None

    def economic_events(
            self,
            start: str | None = None,
            end: str | None = None,
            limit: int = 12,
            offset: int = 0,
            force: bool = False
        ):
        try:
            return self.calendar.get_economic_events_calendar(
                start = start,
                end = end,
                limit = limit,
                offset = offset,
                force = force
            )
        except Exception as e:
            print(f"Error getting economic events: {e}")
            return None

    def ipo_info(
            self,
            start: str | None = None,
            end: str | None = None,
            limit: int = 12,
            offset: int = 0,
            force: bool = False
        ):
        try:
            return self.calendar.get_ipo_info_calendar(
                start = start,
                end = end,
                limit = limit,
                offset = offset,
                force = force
            )
        except Exception as e:
            print(f"Error getting IPO info: {e}")
            return None

    def splits_calendar(
            self,
            start: str | None = None,
            end: str | None = None,
            limit: int = 12,
            offset: int = 0,
            force: bool = False
        ):
        try:
            return self.calendar.get_splits_calendar(
                start = start,
                end = end,
                limit = limit,
                offset = offset,
                force = force
            )
        except Exception as e:
            print(f"Error getting splits calendar: {e}")
            return None
    
