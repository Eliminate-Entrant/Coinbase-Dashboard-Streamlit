import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

from api.coinbase import get_historical_data, all_trading_pairs_available
from components.candlestick_plot import candlestick_plot
from components.line_plots import line_plot


TICKERS = ["open", "high", "low", "close"]

_trading_pairs = all_trading_pairs_available.get_trading_symbols()

if not _trading_pairs:
    st.warning("Nothing to show as NO trading pairs found.")
    st.stop()


symbol = st.sidebar.selectbox("Select Symbol", _trading_pairs.keys())

st.header(f"Historical Prices of {symbol}")

today = datetime.today()
last_year = today - timedelta(days=365)
granularity_dict = {
    "1m": 60,
    "5m": 300,
    "15m": 900,
    "1h": 3600,
    "6h": 21600,
    "1d": 86400,
}

granularity = st.sidebar.selectbox(
    "Select time frame granularity", granularity_dict.keys(), index=5
)

start_date = st.sidebar.date_input("Start Date", None)
end_date = st.sidebar.date_input("End Date", today)

candle_data = get_historical_data(
    trading_pair=symbol,
    start_time=start_date,
    end_time=end_date,
    granularity=granularity_dict[granularity],
)

if not candle_data:
    st.error("No historical data found.", icon="❗️")
    st.stop()

candle_data_df = pd.DataFrame(candle_data)

st.metric("Total Volume", value=candle_data_df["volume"].sum())


quote_currency = _trading_pairs[symbol].quote_currency

show_select = False

# Create tabs for "Candle Plot" and "Line Plot"
candle_graph_tab, line_graph_tab = st.tabs(["Candle Plot", "Line Plot"])


# Display the plots based on the selected tab
with candle_graph_tab:
    # For the "Candle Plot" tab, set show_select to False
    fig: go.Figure = candlestick_plot(
        symbol_candles=candle_data_df, quote_currency=quote_currency
    )
    st.plotly_chart(fig, theme="streamlit")

with line_graph_tab:

    # if line_graph_tab:
    show_select = True
    # For the "Line Plot" tab, show the ticker selection if show_select is True
    if show_select:
        show_tickers = st.multiselect("Select Tickers", TICKERS, default=TICKERS)
    fig = line_plot(
        symbol_candles=candle_data_df,
        quote_currency=quote_currency,
        ticker=show_tickers,
    )
    st.plotly_chart(fig)
