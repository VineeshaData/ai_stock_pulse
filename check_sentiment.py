import yfinance as yf
from textblob import TextBlob
import pandas as pd

my_stocks = ["NEWGEN.NS", "KPIGREEN.NS","SILVERIETF.NS", "GOLDIETF.NS","ADANIPORTS.NS"]

print("--- 🤖 Starting Advanced AI Analysis ---")

final_data = []

for ticker in my_stocks:
    print(f"🔄 Checking: {ticker}...")
    stock = yf.Ticker(ticker)
    
    # 1. Get Price Data (Using 5d to ensure we don't get an empty table)
    history = stock.history(period="5d")
    if history.empty:
        print(f"⚠️ No price data for {ticker}. Skipping.")
        continue
    
    current_price = history['Close'].iloc[-1]
    
    # 2. Get News Data
    news_list = stock.news
    total_sentiment = 0
    headlines_found = 0
    
    # 3. Analyze up to 3 headlines
    for article in news_list[:3]:
        # SAFETY GUARD: Check 'title' OR 'headline' OR 'text'
        headline = article.get('title') or article.get('headline') or article.get('text')
        
        if headline:
            analysis = TextBlob(headline)
            total_sentiment += analysis.sentiment.polarity
            headlines_found += 1
    
    # Calculate Average
    avg_score = total_sentiment / headlines_found if headlines_found > 0 else 0
    
    # Define the Market Mood
    if avg_score > 0.1:
        mood = "Bullish 🚀"
    elif avg_score < -0.1:
        mood = "Bearish 📉"
    else:
        mood = "Neutral ⚖️"
        
    final_data.append({
        "Ticker": ticker,
        "Price": round(current_price, 2),
        "AI Sentiment": round(avg_score, 2),
        "Mood": mood
    })

# --- 📊 SHOW FINAL RESULT ---
if final_data:
    df = pd.DataFrame(final_data)
    print("\n", df)
    df.to_csv("ai_investment_report.csv", index=False)
    print("\n✅ Report saved to 'ai_investment_report.csv'")
else:
    print("❌ Error: No data was collected.")