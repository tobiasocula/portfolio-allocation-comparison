import pandas as pd
import yfinance as yf
from pathlib import Path


datafolder = Path.cwd() / 'data'

for folder in datafolder.iterdir():
    for csv_ticker in folder.iterdir():

        df = pd.read_csv(datafolder / folder / csv_ticker, index_col=0)
        if df.empty:
            # remove
            (datafolder / folder / csv_ticker).unlink()