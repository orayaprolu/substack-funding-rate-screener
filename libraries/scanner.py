

class Scanner:
    @staticmethod
    def get_all_symbols(exchange, quote: str | None = None):
        markets = exchange.load_markets()
        syms = []
        for m in markets.values():
            # contract == True means futures/options/swaps; swap narrows to perpetuals
            if m.get('contract') and m.get('swap') and m.get('active', True):
                if quote is None or m.get('quote') == quote:
                    syms.append(m['symbol'])
        return syms
