import yfinance as yf

us_market_indices = [
    "^GSPC",   # S&P 500 Index
    "^DJI",    # Dow Jones Industrial Average
    "^IXIC",   # Nasdaq Composite
    "^RUT",    # Russell 2000
    "^SP1500"  # S&P Composite 1500
]

for idx in us_market_indices:
    try:
        df = yf.Ticker(idx).history(interval='1d', period='max')
        df = df.drop(
            [c for c in df.columns if c not in ['Date', 'Open' ,'High', 'Close', 'Low', 'Volume']], axis=1
        )
        df = df.tz_localize(None)

        df.to_csv(f"{idx}.csv")
    except Exception as e:
        print('failed to save index', idx, 'because', e)