#!/usr/bin/env python3
"""
Fetch stock data based on user selections and save to CSV
"""
import json
import yfinance as yf
from datetime import datetime, timedelta

# Stock ticker mapping
STOCK_TICKERS = {
    "Nvidia": "NVDA",
    "Google": "GOOGL",
    "Salesforce": "CRM"
}

# Read user input
with open('.anyt/cells/input-t0jh/response.json', 'r') as f:
    user_input = json.load(f)

stock_name = user_input['values']['Stock to review']
last_days = user_input['values']['Last days']

print(f"Fetching {stock_name} stock data for the last {last_days} days...")

# Get the ticker symbol
ticker_symbol = STOCK_TICKERS[stock_name]

# Calculate date range
end_date = datetime.now()
start_date = end_date - timedelta(days=last_days)

# Fetch stock data
ticker = yf.Ticker(ticker_symbol)
stock_data = ticker.history(start=start_date, end=end_date)

# Save to CSV
stock_data.to_csv('stocks.csv')

print(f"Successfully fetched {len(stock_data)} days of stock data")
print(f"Data saved to stocks.csv")
print(f"\nPreview of the data:")
print(stock_data.head())
