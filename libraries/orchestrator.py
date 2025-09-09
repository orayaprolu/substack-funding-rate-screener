import pandas as pd

from libraries.scanner import Scanner
from libraries.funding_rate_fetcher import FundingRateFetcher
from libraries.dashboard import Dashboard

class Orchestrator:
    def __init__(self, exchange_obj):
        self.exchange = exchange_obj
        self.data = None

    def display(self):
        if self.data is None:
            self.data = self._gather_funding_rates()
        dashboard = Dashboard(self.data)
        dashboard.display()

    def save_to_csv(self, filename):
        if self.data is None:
            self.data = self._gather_funding_rates()
        dashboard = Dashboard(self.data)
        dashboard.save_to_csv(filename)

    def refresh_data(self):
        """Clear the cached data and fetch new data."""
        self.data = self._gather_funding_rates()
        return self.data

    def _gather_funding_rates(self):
        symbols = Scanner.get_all_symbols(self.exchange)
        rows = []

        for symbol in symbols:
            try:
                avg_funding_rate, interval = FundingRateFetcher.get_average_funding_rate_and_interval(
                    exchange_obj=self.exchange,
                    symbol=symbol,
                    days_back=7
                )
                current_funding_rate = FundingRateFetcher.get_current_funding_rate(
                    exchange_obj=self.exchange,
                    symbol=symbol,
                    interval_hours=interval
                )

                annualized_avg_funding_rate = avg_funding_rate * 24 * 365
                annualized_current_funding_rate = current_funding_rate * 24 * 365

                rows.append({
                    'Symbol': symbol,
                    '7 Day Average Funding Rate (Annualized %)': (annualized_avg_funding_rate * 100),
                    'Current Funding Rate (Annualized %)': (annualized_current_funding_rate * 100)
                })

                print(f"Processed symbol: {symbol}")
            except Exception as e:
                print(f"Skipped symbol {symbol}: {str(e)}")
                continue

        df = pd.DataFrame(rows)
        self.data = df
        return df
