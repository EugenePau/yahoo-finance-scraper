import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Yahoo News RSS URL
TICKER_SYMBOL = "AAPL"
WINDOW_DAYS = 30

def get_dates():
    # Get today's date
    raw_today = datetime.today()
    today = raw_today.strftime("%Y-%m-%d")
    
    # Get the start-of-record day
    raw_start_date = raw_today - timedelta(days = WINDOW_DAYS)
    start_date = raw_start_date.strftime("%Y-%m-%d")
    
    # Print results
    #print("Today:", today)
    #print("30 days ago:", thirty_days_ago)

    return start_date, today

def parse_from_yfinance():
    # Get Dates
    start_date, today = get_dates()
    
    # Fetch stock data
    stock = yf.download(TICKER_SYMBOL, start_date, today)
    print(stock.isnull().sum())  # Check for missing data


    # Check if DataFrame is empty, else synthesis stock data
    if stock.empty:
        print("⚠️ Error: Stock data fetch failed! DataFrame is empty.")
            
    else:
        print("✅ Stock data fetched successfully!")


    # Save as Parquet
    stock.to_parquet(f"stock_data_{today}.parquet", engine="pyarrow", index=True)
    
    # Restore from Parquet
    stock_restored = pd.read_parquet(f"stock_data_{today}.parquet", engine="pyarrow")

    # Compare
    print(stock.head())
    print(stock_restored.head())

print('開始執行...')
parse_from_yfinance()
print('執行完成')

