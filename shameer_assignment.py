import pandas as pd
import streamlit as st
import requests

st.header("Bitcoin Trend")

API_URL = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?'
currency = st.radio("Select your currency", ('usd', 'cad', 'inr'))
days = st.slider('Select no. of days', 0, 365, 1)
interval = 'daily'
payload = {'vs_currency':currency, 'days':days, 'interval':interval}

req=requests.get(API_URL,payload)

if req.status_code == 200:
    data = req.json()
    
df=pd.DataFrame(data=data['prices'], columns=['date','price'])
df['date'] = pd.to_datetime(df['date'],unit='ms')
average=df['price'].mean()

st.line_chart(df['price'])
st.write(f'Average Bitcoin price = {float(average)}')