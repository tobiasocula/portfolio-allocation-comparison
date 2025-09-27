import pandas as pd
import yfinance as yf
from pathlib import Path

datafolder = Path.cwd() / 'data'

for folder in datafolder.iterdir():
    for csv_ticker in folder.iterdir():

        df = pd.read_csv(datafolder / folder / csv_ticker, index_col=0)
        if 'MarketCap' in df.columns:

            continue

        #print(df)
        ticker = yf.Ticker(csv_ticker.name.split(".")[0])

        try:

            quarterly_shares = ticker.quarterly_income_stmt.loc['Basic Average Shares']
            quarter_dates = pd.to_datetime(quarterly_shares.index)
            shares_df = pd.DataFrame({
                'shares_outstanding': quarterly_shares.values.flatten()
                }, index=quarter_dates)
            
            shares_df = shares_df.sort_index()
            shares_df = shares_df.reindex(df.index, method='ffill')

            df["MarketCap"] = df["Close"] * shares_df["shares_outstanding"]
            #print('new df:'); print(df[["MarketCap", "Close"]])
            print('added market cap for ticker', csv_ticker.name.split('.')[0])

            df.to_csv(datafolder / folder / csv_ticker)

        except Exception as e:
            print('failed for ticker', csv_ticker.name.split('.')[0], ':', e)
        
        

        
