import yfinance as yf
import streamlit as st

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol

st.write(
"""
# Simple Stock Price App
"""
)
companies = [ ('GOOGL', 'Google'), ('AAPL', 'Apple'), ('AMZN', 'Amazon'), ('META', 'Meta'), ('MSFT', 'Microsoft'), ('TSLA', 'Tesla'), ('DIS', 'The Walt Disney Company')]

for ts, cmp in companies:

    st.write(f"""
    # {cmp}
    Shown are the stock ***closing price*** and ***volume*** of
    """, cmp)
    tickerSymbol = ts 

    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2013-5-31', end='2024-1-31')

    # tickerDf -- Simply shows the data

    st.write("""
    ## Closing Price
    """)
    st.line_chart(tickerDf.Close)

    st.write("""
    ## Volume Price
    """)
    st.line_chart(tickerDf.Volume)


st.write("""
Made By **_Jaweria Batool_**
""")