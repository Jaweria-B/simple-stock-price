# Simple Stock Price Tracker

This repository contains a simple application built with Streamlit that tracks the closing price and volume of major publicly traded companies from **2013-5-31** to **2024-1-31**. The application fetches real-time stock price data using the Yahoo Finance API (yfinance).

## Companies Tracked
The application currently tracks the following companies:

1. Google (GOOGL)
2. Apple (AAPL)
3. Amazon (AMZN)
4. Meta Platforms, Inc. (formerly Facebook) (META)
5. Microsoft (MSFT)
6. Tesla (TSLA)
7. The Walt Disney Company (DIS)

## Features

- **Real-Time Data**: Fetches stock price data using the Yahoo Finance API.
- **Interactive Interface**: Streamlit provides an intuitive UI for easy interaction.
- **Customizable**: Users can select from a list of major companies to track.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Jaweria-B/simple-stock-price.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:

    ```bash
    streamlit run myapp.py
    ```

## Demo

[Live Demo](https://simple-stock-price.streamlit.app/)

