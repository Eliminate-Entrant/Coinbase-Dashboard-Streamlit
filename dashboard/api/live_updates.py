import asyncio
from threading import Thread
import websockets
import json
import sys
import time

from config import settings

# Define a global variable to keep track of the number of threads
thread_counter = 0


async def fetch_ticker(product_ids: list[str], callback=None, stop=False):
    """
    Websocket client to fetch ticker data for product IDs to get live updates.
    :param product_ids: List of product IDs to fetch ticker data for.
    :param callback: Callback function to run when data is received.
    :param stop: Boolean to stop the websocket connection.
    Function works by subscribing to the ticker channel for the specified product IDs.
    However, there is an issue with threading in Streamlit,
    so the function is not implemented and will be fixed if had more time.
    """
    uri = settings.API_BASE_URL_WSS

    async def websocket_handler():
        async with websockets.connect(uri) as websocket:
            # Subscribe to the ticker channel for the specified product
            await websocket.send(
                json.dumps(
                    {
                        "type": "subscribe",
                        "product_ids": product_ids,
                        "channels": ["ticker"],
                    }
                )
            )

            # Continuously listen for messages from the websocket
            while True:
                try:
                    response = await websocket.recv()
                    data = json.loads(response)
                    if "type" in data and data["type"] == "ticker":
                        if callback:
                            print("running callback...")
                            callback(data)
                        # print(data)
                    if stop:
                        break
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break
            print("finished")

    await websocket_handler()
