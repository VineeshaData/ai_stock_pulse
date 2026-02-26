import yfinance as yf

# Let's check NEWGEN SOFTWARE TECH (NVDANEWGEN) - a huge AI stock in 2026
ticker = "NEWGEN" 

print(f"--- 📊 Running Report for {ticker} ---")

# Get data from your starting point (Sept 2025) to Today (Feb 2026)
stock_info = yf.Ticker(ticker)
history = stock_info.history(start="2025-09-01")

# Check if we actually got data
if not history.empty:
    start_price = history['Close'].iloc[0]
    current_price = history['Close'].iloc[-1]
    change = ((current_price - start_price) / start_price) * 100

    print(f"Price on Sept 1, 2025: ${start_price:.2f}")
    print(f"Price on Feb 24, 2026: ${current_price:.2f}")
    print(f"Overall Portfolio Change: {change:.2f}%")
else:
    print("Could not find data. Check your internet connection!")