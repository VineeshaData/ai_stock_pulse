import yfinance as yf

ticker = "ADANIPORTS.NS"
stock = yf.Ticker(ticker)
news = stock.news

if news:
    print(f"--- 📦 RAW DATA DUMP FOR {ticker} ---")
    # This prints the first article so we can see all the labels (keys)
    print(news[0]) 
    print("-----------------------------------")
else:
    print("No news found.")