import requests
import pandas as pd

url = "https://finance.yahoo.com/quote/TSLA/history?period1=1523836800&period2=1681603200&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

df = pd.read_html(resp.text)[0]

df = df.drop(df.index[-1])

df.Date = pd.to_datetime(df.Date, format="%b %d, %Y")
df["Close*"] = df["Close*"].astype(float)

df.drop(columns=["Open", "High", "Low", "Volume", "Adj Close**"], inplace=True)

df.to_csv("tesla.csv", index=False)