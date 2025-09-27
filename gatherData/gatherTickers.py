import yfinance as yf
from pathlib import Path

"""

1. Information Technology
Companies: Apple (AAPL), Microsoft (MSFT), Alphabet (GOOGL), Nvidia (NVDA), Adobe (ADBE)

ETFs: Technology Select Sector SPDR Fund (XLK), iShares U.S. Technology ETF (IYW)

2. Financials
Companies: JPMorgan Chase (JPM), Berkshire Hathaway (BRK.B), Bank of America (BAC), Goldman Sachs (GS)

ETFs: Financial Select Sector SPDR Fund (XLF), iShares U.S. Financials ETF (IYF)

3. Health Care
Companies: Johnson & Johnson (JNJ), Pfizer (PFE), Merck (MRK), UnitedHealth Group (UNH)

ETFs: Health Care Select Sector SPDR Fund (XLV), iShares U.S. Healthcare ETF (IYH)

4. Consumer Discretionary (Consumer Services)
Companies: Amazon (AMZN), Tesla (TSLA), Nike (NKE), Starbucks (SBUX)

ETFs: Consumer Discretionary Select Sector SPDR Fund (XLY), iShares U.S. Consumer Discretionary ETF (IYC)

5. Consumer Staples (Consumer Non-Durables)
Companies: Procter & Gamble (PG), Coca-Cola (KO), Walmart (WMT), PepsiCo (PEP)

ETFs: Consumer Staples Select Sector SPDR Fund (XLP), iShares U.S. Consumer Staples ETF (IYK)

6. Energy
Companies: ExxonMobil (XOM), Chevron (CVX), ConocoPhillips (COP)

ETFs: Energy Select Sector SPDR Fund (XLE), iShares U.S. Energy ETF (IYE)

7. Industrials
Companies: Boeing (BA), Caterpillar (CAT), 3M (MMM), Honeywell (HON)

ETFs: Industrial Select Sector SPDR Fund (XLI), iShares U.S. Industrials ETF (IYJ)

8. Materials (Basic Materials / Non-Energy Minerals)
Companies: DuPont (DD), Sherwin-Williams (SHW), Newmont Corporation (NEM)

ETFs: Materials Select Sector SPDR Fund (XLB), iShares U.S. Materials ETF (IYM)

9. Utilities
Companies: Duke Energy (DUK), Southern Company (SO), NextEra Energy (NEE)

ETFs: Utilities Select Sector SPDR Fund (XLU), iShares U.S. Utilities ETF (IDU)

10. Communication Services (Telecommunications & Media)
Companies: Meta Platforms (META), Verizon (VZ), AT&T (T), Comcast (CMCSA)

ETFs: Communication Services Select Sector SPDR Fund (XLC), iShares U.S. Telecom ETF (IYZ)

11. Real Estate (REITs)
Companies: Prologis (PLD), American Tower (AMT), Equity Residential (EQR)

ETFs: Real Estate Select Sector SPDR Fund (XLRE), Vanguard Real Estate ETF (VNQ)

Major Indices Tracking the US Market as a Whole
S&P 500 Index (SPX): Tracks 500 large-cap US companies across sectors

Dow Jones Industrial Average (DJI): Tracks 30 large, publicly-owned companies

Nasdaq Composite (IXIC): Heavy on tech and growth companies, over 3000 stocks

Russell 2000 (RUT): Small-cap US companies

S&P 400 MidCap Index: Mid-sized US companies

S&P Composite 1500: Combination of S&P 500, 400, and 600

"""

information_tickers = [
    "AAPL", "MSFT", "GOOGL", "NVDA", "ADBE", "INTC", "CSCO", "AMD", "ORCL", "IBM",
    "TXN", "QCOM", "AVGO", "NOW", "CRM", "ADI", "MU", "ZBRA", "LRCX", "KLAC"
]

finance_tickers = [
    "JPM", "BRK.B", "BAC", "WFC", "C", "GS", "MS", "AXP", "BLK", "SCHW",
    "TFC", "PNC", "ICE", "USB", "CME", "SPGI", "AIG", "ALL", "MET", "PRU"
]

healthcare_tickers = [
    "JNJ", "PFE", "MRK", "UNH", "ABBV", "TMO", "ABT", "LLY", "BMY", "CVS",
    "GILD", "MDT", "DHR", "AMGN", "BIIB", "VRTX", "REGN", "ISRG", "ZTS", "HCA"
]

consumer_discretionary_tickers = [
    "AMZN", "TSLA", "NKE", "SBUX", "MCD", "HD", "LOW", "LULU", "BKNG", "GM",
    "F", "TGT", "ROST", "CAR", "DIS", "VFC", "NCLH", "MAR", "YUM", "MNST"
]

consumer_staples_tickers = [
    "PG", "KO", "WMT", "PEP", "COST", "MO", "PM", "CL", "KMB", "ADM",
    "HSY", "MDLZ", "KHC", "GIS", "EL", "STZ", "MKC", "SJM", "BF.B", "TSN"
]

energy_tickers = [
    "XOM", "CVX", "COP", "PSX", "OXY", "EOG", "KMI", "SLB", "VLO", "MPC",
    "HAL", "FTI", "BKR", "WMB", "OKE", "APA", "CDEV", "HES", "NOV", "PXD"
]

industrials_tickers = [
    "BA", "CAT", "MMM", "HON", "GE", "LMT", "UTX", "DE", "FDX", "GD",
    "EMR", "CSX", "AOS", "PH", "REG", "RHI", "SWK", "ITW", "EXPD", "WM"
]

materials_tickers = [
    "DD", "SHW", "NEM", "ECL", "APD", "LIN", "PPG", "MLM", "LYB", "VMC",
    "BLL", "CF", "FMC", "MOS", "NUE", "IFF", "ALB", "EMN", "WMS", "VRS"
]

utilities_tickers = [
    "DUK", "SO", "NEE", "AEP", "EXC", "ED", "D", "PEG", "SRE", "XEL",
    "PNW", "ES", "PPL", "CMS", "ETR", "WEC", "LNT", "CMS", "EIX", "AES"
]

communication_services_tickers = [
    "META", "VZ", "T", "CMCSA", "NFLX", "DIS", "CHTR", "ATVI", "EA", "TMUS",
    "CCL", "LYV", "WBD", "IPG", "OMC", "DISH", "FOXA", "GOOG", "GOOGL", "SIRI"
]

real_estate_tickers = [
    "PLD", "AMT", "EQR", "CCI", "SPG", "DLR", "PSA", "VTR", "WELL", "O",
    "AVB", "EXR", "EQIX", "IRM", "REG", "FRT", "KIM", "HST", "BXP", "ESS"
]

tickerlist = {
    "information": information_tickers,
    "finance": finance_tickers,
    "healthcare": healthcare_tickers,
    "consumer_discretionary": consumer_discretionary_tickers,
    "consumer_staples": consumer_staples_tickers,
    "energy": energy_tickers,
    "industrials": industrials_tickers,
    "materials": materials_tickers,
    "utilities": utilities_tickers,
    "communication": communication_services_tickers,
    "real_estate": real_estate_tickers
}

for sector_name, lst in tickerlist.items():
    sector_path = Path(sector_name)
    sector_path.mkdir(parents=True, exist_ok=True)

    for t in lst:

        try:
            df = yf.Ticker(t).history(interval='1d', period='max')
            df = df.drop(
                [c for c in df.columns if c not in ['Date', 'Open' ,'High', 'Close', 'Low', 'Volume']], axis=1
            )
            df = df.tz_localize(None)

            df.to_csv(sector_path / f"{t}.csv")
        except Exception as e:
            print('failed to save ticker', t, 'from sector', sector_name, 'because:', e)

"""
index type:
<class 'pandas.core.indexes.datetimes.DatetimeIndex'>
<class 'pandas._libs.tslibs.timestamps.Timestamp'>
"""