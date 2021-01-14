import pandas as pd
import yfinance as yf
import streamlit as st

### first streamlit web app

st.write("""
#Simple Stock Price App

Shown are the stock closing price and volume of Google and Yandex for instance


""")

tickerSymbol1 = 'GOOGL'
tickerSymbol2 = 'YNDX'

tickerData1 = yf.Ticker(tickerSymbol1)
tickerData2 = yf.Ticker(tickerSymbol2)

tickerDf1 = tickerData1.history(period='1d', start = '2010-1-12', end = '2020-1-12')
tickerDf2 = tickerData1.history(period='1d', start = '2010-1-12', end = '2020-1-12')

st.line_chart(tickerDf1.Close)
st.line_chart(tickerDf1.Volume)
st.line_chart(tickerDf2.Close)
st.line_chart(tickerDf2.Volume)

