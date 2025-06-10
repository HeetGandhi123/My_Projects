import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt

st.title("📈 EMA Crossover Trading Strategy Backtester")

# Sidebar inputs
stock = st.sidebar.text_input("Enter Stock Ticker", value="AAPL").upper()
start = st.sidebar.date_input("Start Date", dt.date(2023, 1, 1))
end = st.sidebar.date_input("End Date", dt.date(2025, 1, 1))

if start >= end:
    st.error("End date must be after start date.")
    st.stop()

# Download data
df = yf.download(stock, start=start, end=end)

if df.empty:
    st.error("No data fetched. Please check the stock ticker or date range.")
    st.stop()

if 'Date' in df.columns:
    df = df.set_index('Date')

# Flatten multi-level columns if present
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

# Select only the required columns (protect against missing columns)
required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
df = df[[col for col in required_cols if col in df.columns]]

# Sort by date
df = df.sort_index()

# Calculate EMAs
emaUsed = [3,5,8,10,12,15,30,35,40,45,50,60]
for x in emaUsed:
    df[f"Ema_{x}"] = df["Close"].ewm(span=x, adjust=False).mean()

# Backtest logic
pos = 0
percentchange = []
bp = sp = 0
for i in range(len(df)):
    row = df.iloc[i]
    cmin = min([row[f"Ema_{x}"] for x in [3,5,8,10,12,15]])
    cmax = max([row[f"Ema_{x}"] for x in [30,35,40,45,50,60]])
    close = row['Close']

    if cmin > cmax:
        if pos == 0:
            bp = close
            pos = 1
            st.write(f"📥 Buying at {bp:.2f} on {df.index[i].date()}")

    elif cmin < cmax and pos == 1:
        sp = close
        pos = 0
        pc = ((sp / bp) - 1) * 100
        percentchange.append(pc)
        st.write(f"📤 Selling at {sp:.2f} on {df.index[i].date()} — Return: {pc:.2f}%")

# Final trade
if pos == 1:
    sp = df["Close"].iloc[-1]
    pc = ((sp / bp) - 1) * 100
    percentchange.append(pc)
    st.write(f"📤 Selling at {sp:.2f} on {df.index[-1].date()} — Return: {pc:.2f}%")

# Performance Stats
gains = sum(i for i in percentchange if i > 0)
losses = sum(i for i in percentchange if i <= 0)
number_of_gains = sum(1 for i in percentchange if i > 0)
number_of_losses = sum(1 for i in percentchange if i <= 0)
total_return = round((np.prod([(i/100)+1 for i in percentchange]) - 1) * 100, 2)

avgGain = round(gains / number_of_gains, 2) if number_of_gains else 0
avgLoss = round(losses / number_of_losses, 2) if number_of_losses else 0
maxR = round(max(percentchange), 2) if percentchange else 'Undefined'
maxL = round(min(percentchange), 2) if percentchange else 'Undefined'
ratio = round(-avgGain / avgLoss, 2) if avgLoss != 0 else 'inf'
battingAvg = round(number_of_gains / (number_of_gains + number_of_losses), 2) if (number_of_gains + number_of_losses) else 0

# Show metrics
st.subheader("📊 Strategy Performance Summary")
st.write(f"**Stock:** {stock}")
st.write(f"**Date Range:** {start} to {end}")
st.write(f"**Number of Trades:** {number_of_gains + number_of_losses}")
st.write(f"**Batting Average:** {battingAvg}")
st.write(f"**Gain/Loss Ratio:** {ratio}")
st.write(f"**Average Gain:** {avgGain}%")
st.write(f"**Average Loss:** {avgLoss}%")
st.write(f"**Max Return in a Trade:** {maxR}%")
st.write(f"**Max Loss in a Trade:** {maxL}%")
st.write(f"**Total Return:** {total_return}%")

# Optional: Line chart
st.subheader("📈 Closing Price & EMAs")
ema_cols = [f"Ema_{x}" for x in emaUsed]
st.line_chart(df[["Close"] + ema_cols])
