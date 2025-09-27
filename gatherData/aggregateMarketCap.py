import pandas as pd
from pathlib import Path

datafolder = Path.cwd() / 'data'

for folder in datafolder.iterdir():
    for csv_ticker in folder.iterdir():

        df = pd.read_csv(datafolder / folder / csv_ticker, index_col=0)
        if 'MarketCap' in df.columns:
            df["MarketCap"] = df["MarketCap"].fillna(method='bfill')
            df.to_csv(datafolder / folder / csv_ticker)
            