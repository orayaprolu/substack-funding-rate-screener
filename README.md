# Funding Rate Scanner

A Python application that scans and analyzes funding rates for cryptocurrency perpetual futures across different exchanges. The app fetches current and historical funding rate data, calculates annualized rates, and exports the results to CSV format.

## Supported Exchanges

The following exchanges are supported (configurable in `config.py`):

- binance, bingx, bitget, bitmart, blofin, coincatch, coinex, cryptocom
- deribit, derive, digifinex, gate, hashkey, hibachi, hitbtc, htx
- kucoinfutures, mexc, modetrade, okx, phemex, woo, woofipro, xt

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/orayaprolu/substack-funding-rate-screener
   cd substack-funding-rate
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Edit `config.py` to change the target exchange:

```python
import ccxt

# Change 'hyperliquid' to any supported exchange
EXCHANGE = ccxt.hyperliquid()
```

## Usage

Run the scanner:

```bash
python main.py
```

The application will:
1. Fetch all active perpetual swap symbols from the configured exchange
2. Retrieve current funding rates and 7-day historical data for each symbol
3. Calculate annualized funding rates (current and 7-day average)
4. Display results in the terminal
5. Save results to a CSV file in the `output/` directory

## Output

The scanner generates a CSV file named `funding_rates_{exchange_name}.csv` in the output folder with the following columns:

- **Symbol**: The trading pair symbol (e.g., BTC/USDT:USDT)
- **7 Day Average Funding Rate (Annualized %)**: Historical 7-day average funding rate converted to annual percentage
- **Current Funding Rate (Annualized %)**: Current funding rate converted to annual percentage

## Example Output

```
Symbol                    7 Day Average Funding Rate (Annualized %)    Current Funding Rate (Annualized %)
BTC/USDT:USDT            5.47                                          4.23
ETH/USDT:USDT            8.91                                          7.65
SOL/USDT:USDT            12.34                                         15.22
```

## Requirements

- Python 3.12+
- See `requirements.txt` for complete dependency list

## Notes

- Funding rates are typically updated every 8 hours on most exchanges
- Some exchanges may have rate limits - the scanner respects these automatically
- Historical data availability varies by exchange (typically 7-30 days)
- Annualized rates are calculated by multiplying hourly rates by 24 × 365

## License

This project is open source. Please check with individual exchanges regarding their API usage terms and conditions.
