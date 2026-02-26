import streamlit as st
import pandas as pd
import plotly.express as px

# Setup the page
st.set_page_config(page_title="AI Stock Pulse", layout="wide")
st.title("📈 AI Stock Sentiment Pulse")

# Load your report
df = pd.read_csv("final_investment_report.csv")

# Create a Sidebar for selection
ticker = st.sidebar.selectbox("Select a Stock to Analyze:", df['Ticker'])

# Filter data for the chosen stock
stock_data = df[df['Ticker'] == ticker].iloc[0]

# Display big metrics
col1, col2, col3 = st.columns(3)
col1.metric("Current Price", f"₹{stock_data['Price']}")
col2.metric("AI Sentiment Score", stock_data['AI Score'])
col3.write(f"### Market Mood: {stock_data['Mood']}")

# Create a visual chart
fig = px.bar(df, x='Ticker', y='AI Score', color='Mood',
             title="Sentiment Comparison Across Portfolio",
             color_discrete_map={"Bullish 🚀": "green", "Bearish 📉": "red", "Neutral ⚖️": "gray"})

st.plotly_chart(fig, use_container_width=True)