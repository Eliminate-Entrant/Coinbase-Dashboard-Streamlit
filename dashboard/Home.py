import streamlit as st

from api.coinbase import all_trading_pairs_available
from api.live_updates import fetch_ticker
from models.trading_pairs import TradingPair
from threading import Thread
import asyncio
import time

# Global variable to store WebSocket data
wss_data = []


def launch_dashboard():
    global wss_data
    st.title("Coinbase Dashboard")
    st.sidebar.success(
        """
        Welcome to the Coinbase Dashboard.
        This dashboard provides real-time updates for trading pairs available on Coinbase.
        It has three main sections:
            1. Trading Pairs: Displays all trading pairs available on Coinbase.
            2. Displayes historical prices of selected symbols.
            3. Trading Accounts: Displays trading accounts available on Coinbase.
        Tried implementing live updates using WebSocket but it's not working due to threading issues that need to be resolved.
        """
    )

    # Fetch trading pairs
    all_trading_pairs = all_trading_pairs_available.get_trading_symbols()
    st.metric("Total Trading Pairs available", len(all_trading_pairs))
    st.dataframe(all_trading_pairs.values())

    # all_symbols = list(all_trading_pairs.keys())

    #! Threading and WebSocket implementation not working
    # st.header(f"Live Updates for {all_symbols}")

    # Define a callback function to update data when WebSocket receives new data
    # def websocket_data(data):
    #     global wss_data

    #     print(data["type"])
    #     wss_data.append("uu")

    # # Start the WebSocket connection in a separate thread
    # fetch_thread = Thread(
    #     target=lambda: asyncio.run(fetch_ticker(all_symbols, websocket_data))
    # )
    # fetch_thread.daemon = True
    # fetch_thread.start()
    # # time.sleep(1)
    # fetch_thread.join()

    # st.write(wss_data)
    # # Continuously update the main Streamlit page with WebSocket data
    # while True:
    #     if wss_data:
    #         st.write("Live Updates:")
    #         st.write(wss_data)
    #         wss_data = []  # Clear the WebSocket data after displaying it
    #     else:
    #         st.write("Waiting for live updates...")
    #     st.empty()  # Add an empty element to force the UI to update


if __name__ == "__main__":
    launch_dashboard()
