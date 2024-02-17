import yfinance as yf
import streamlit as st
from datetime import date
from PIL import Image

today = date.today()
splitted = str(today).split('-')
year, month, day = splitted[0], splitted[1], splitted[2]
# print(f"{year} {month} {day}")

ten_years = ('-').join([str(int(year) - 10), str(month), str(day)])
# print(ten_years)


#define the ticker symbol

st.write(
"""
# Simple Stock Price App

 **Select from a range of companies and visualize their closing prices and trading volumes over the past decade.**
"""
)

st.divider()

companies = {
    'Alibaba Group Holding Limited': 'BABA',
    'Amazon': 'AMZN',
    'Apple': 'AAPL',
    'Coca-Cola Company': 'KO',
    'Johnson & Johnson': 'JNJ',
    'JPMorgan Chase & Co.': 'JPM',
    'Meta Platforms, Inc.': 'META',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'NVIDIA Corporation': 'NVDA',
    'PepsiCo, Inc.': 'PEP',
    'Tesla, Inc.': 'TSLA',
    'The Walt Disney Company': 'DIS',
}
selected_cmp = st.selectbox('Select a Company:', companies.keys(), index=None, placeholder="Choose an option...")

if selected_cmp:

    st.write(f"""
    # {selected_cmp}
    Shown are the stock ***closing price*** and ***volume*** of
    """, selected_cmp)
    tickerSymbol = companies[selected_cmp] 

    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start=ten_years, end=today)

    # tickerDf -- Simply shows the data

    st.write("""
    ## Closing Price
    """)
    st.line_chart(tickerDf.Close)

    st.write("""
    ## Volume Price
    """)
    st.line_chart(tickerDf.Volume)

    st.write(
            """
            Made By **_Jaweria Batool_**
            """
        )

        # link to GitHub README file
    st.write("For more information about how the app works, please check out the [GitHub README](https://github.com/Jaweria-B/simple-stock-price) file.")




# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75