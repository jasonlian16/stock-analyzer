import yfinance as yf
import pandas as pd

ticker_symbol = input("Enter your Stock Ticker: ")

try:
    # creates object for Ticker
    ticker = yf.Ticker(ticker_symbol)

    # fetches historical data from 5 year timeline
    hist_data = ticker.history(period="5y")
    if hist_data.empty:
        raise ValueError("No data found for Ticker")
    print("Historical Data: ")
    print(hist_data)

    # puts the data into a CSV file
    df = pd.DataFrame(hist_data)
    output_path = "data/raw.csv"
    df.to_csv(output_path, index=False)
    print(f"Data successfully written to {output_path}")

except Exception as e:
    print(f"Invalid ticker or error fetching data: {e}")






