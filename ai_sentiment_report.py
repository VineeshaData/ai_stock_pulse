import yfinance as yf
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the "Smart" AI
analyzer = SentimentIntensityAnalyzer()
my_stocks = ["ADANIPORTS.NS", "KPIGREEN.NS", "NEWGEN.NS", "SILVERIETF.NS", "GOLDIETF.NS"]

print("--- 🤖 RUNNING FINAL AI ANALYSIS ---")

final_results = []

for ticker in my_stocks:
    print(f"🔄 Processing {ticker}...")
    stock = yf.Ticker(ticker)
    
    # 1. Get Price
    hist = stock.history(period="5d")
    if hist.empty: continue
    current_price = hist['Close'].iloc[-1]
    
    # 2. Get News and Sentiment
    news_list = stock.news
    total_sentiment = 0
    count = 0
    
    for article in news_list[:3]:
        # Path found in your Raw Dump: article -> content -> title/summary
        content = article.get('content', {})
        headline = content.get('title') or content.get('summary') or ""
        
        if headline:
            score = analyzer.polarity_scores(headline)['compound']
            total_sentiment += score
            count += 1
            
    avg_score = total_sentiment / count if count > 0 else 0
    
    # Define Market Mood
    mood = "Bullish 🚀" if avg_score > 0.05 else "Bearish 📉" if avg_score < -0.05 else "Neutral ⚖️"
    
    final_results.append({
        "Ticker": ticker,
        "Price": round(current_price, 2),
        "AI Score": round(avg_score, 2),
        "Mood": mood
    })

# Output
df = pd.DataFrame(final_results)
print("\n", df)
df.to_csv("final_investment_report.csv", index=False)
print("\n✅ DONE! Open 'final_investment_report.csv' to see your results.")

#to open file in excel directly

df.to_csv("final_investment_report.csv", index=False, encoding="utf-8-sig")
import os
os.startfile("final_investment_report.csv")