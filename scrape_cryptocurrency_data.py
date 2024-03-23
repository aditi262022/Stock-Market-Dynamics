import yfinance as yf
import pandas as pd
import requests

def download_crypto_data(symbol, start_date, end_date):

    try:
        print(f"Downloading data for {symbol}...")
        crypto_data = yf.download(symbol, start=start_date, end=end_date)
        print(f"Data downloaded successfully for {symbol}")
        return crypto_data
    except Exception as e:
        print(f"Error downloading data for {symbol}: {e}")
        return None

def convert_to_inr(dataframe):

    # Fetch current exchange rate from USD to INR
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    exchange_rates = response.json()["rates"]
    usd_to_inr_rate = exchange_rates.get("INR", 1)  # Default to 1 if rate is not available

    # Convert prices to INR
    dataframe_inr = dataframe.copy()
    dataframe_inr['Open'] *= usd_to_inr_rate
    dataframe_inr['High'] *= usd_to_inr_rate
    dataframe_inr['Low'] *= usd_to_inr_rate
    dataframe_inr['Close'] *= usd_to_inr_rate

    return dataframe_inr

def main():
    # Define the ticker symbols for Bitcoin, Ethereum, and Ripple
    symbols = ['BTC-USD', 'ETH-USD', 'XRP-USD']
    start_date = '2020-01-01'
    end_date = '2024-01-01'

    # Download data for each cryptocurrency
    for symbol in symbols:
        crypto_data = download_crypto_data(symbol, start_date, end_date)
        
        if crypto_data is not None:
            # Convert prices to INR
            crypto_data_inr = convert_to_inr(crypto_data)
            
            # Save the data to a CSV file
            file_name = f"{symbol.lower().replace('-', '_')}_data_inr.csv"
            crypto_data_inr.to_csv(file_name)
            print(f"Data saved to {file_name}")
        else:
            print(f"Failed to download data for {symbol}")

if __name__ == "__main__":
    main()
