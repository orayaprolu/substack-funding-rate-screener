
class FundingRateFetcher:
    @staticmethod
    def get_current_funding_rate(exchange_obj, symbol: str, interval_hours: int):
        return float(exchange_obj.fetch_funding_rate(symbol)['fundingRate']) / interval_hours

    @staticmethod
    def get_average_funding_rate_and_interval(exchange_obj, symbol: str, days_back: int):
        ts = exchange_obj.milliseconds() - days_back * 24 * 60 * 60 * 1000
        funding_rates = exchange_obj.fetch_funding_rate_history(symbol, ts)

        if len(funding_rates) < 2:
            raise ValueError("Not enough data")

        t0 = funding_rates[0]['timestamp']
        t1 = funding_rates[1]['timestamp']
        interval_hours = (t1 - t0) / (1000 * 60 * 60)

        avg_rate = sum(float(fr['fundingRate']) for fr in funding_rates) / len(funding_rates)

        return avg_rate / interval_hours, interval_hours
