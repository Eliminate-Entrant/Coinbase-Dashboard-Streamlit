import requests
import streamlit as st
from typing import List, Optional, Dict
from datetime import datetime
from requests.exceptions import HTTPError
import base64
import hmac
import hashlib
import time

from models.trading_pairs import TradingPair, convert_json_to_trading_pairs
from models.symbols import SymbolCandle, convert_json_to_symbol_candles
from models.trading_accounts import (
    TradingAccount,
    convert_json_to_trading_accounts,
)
from config import settings


class TradingSymbolsManager:
    """
    Class to get all trading symbols available on the Coinbase API.
    Has a method to fetch trading symbols and another to get them.
    Has error handling.
    """

    def __init__(self):
        self.trading_pairs = self.fetch_trading_symbols()

    def fetch_trading_symbols(_self, url: str = settings.API_BASE_URL):
        try:
            response = requests.get(f"{url}/products")
            response.raise_for_status()
            if response.json() == []:
                st.error("No trading symbols found.", icon="❗️")
                return []
            _self.trading_pairs = convert_json_to_trading_pairs(response.json())
            st.session_state.trading_pairs = _self.trading_pairs
            st.toast("Trading symbols fetched successfully.", icon="🚀")
        except Exception as e:
            st.error(f"An error occurred fetching trading symbols: {e}", icon="❗️")
            st.clear_cache()

    # @st.cache_data()
    def get_trading_symbols(_self) -> Dict[str, TradingPair]:
        if not _self.trading_pairs:
            _self.fetch_trading_symbols()
        return _self.trading_pairs


all_trading_pairs_available = TradingSymbolsManager()


@st.cache_data()
def get_historical_data(
    trading_pair: str,
    start_time: Optional[datetime] | None = None,
    end_time: Optional[datetime] | None = None,
    granularity: Optional[int] | None = None,
) -> List[SymbolCandle]:
    """
    Fetches historical data for the given trading pair.
    :param trading_pair: Trading pair for which to fetch the data.
    :param start_time: Start time for the historical data.
    :param end_time: End time for the historical data.
    :param granularity: Granularity of the data.
    """
    try:
        response = requests.get(
            f"{settings.API_BASE_URL}/products/{trading_pair}/candles",
            params={
                "start": str(start_time) if start_time else None,
                "end": str(end_time) if end_time else None,
                "granularity": granularity if granularity else None,
            },
        )
        response.raise_for_status()
    except HTTPError as http_err:
        st.error(
            f"An error occurred fetching historical data: {http_err.response.text}",
            icon="❗️",
        )
        st.clear_cache()
        return []
    return convert_json_to_symbol_candles(response.json())


class AuthenticatedCoinbase:
    """
    Class to handle authenticated requests to the Coinbase API.
    Generates the signature for the request.
    """

    def __init__(self, method: str, requestPath: str, message: str = ""):
        self.api_key: str = settings.API_KEY.get_secret_value()
        self.api_secret = settings.API_SECRET.get_secret_value()
        self.api_passphrase = settings.API_PASSPHRASE.get_secret_value()
        self.method = method
        self.requestPath = requestPath
        self.message = message
        self.cb_access_timestamp = str(int(time.time()))
        self.signature = self.get_signature()

    def get_signature(self) -> str:
        key = base64.b64decode(self.api_secret)
        message = (
            self.cb_access_timestamp + self.method + self.requestPath + self.message
        )
        hmac_sha256 = hmac.new(key, message.encode(), hashlib.sha256)
        return base64.b64encode(hmac_sha256.digest()).decode()

    def get_headers(self) -> dict[str, str]:
        return {
            "CB-ACCESS-KEY": self.api_key,
            "CB-ACCESS-SIGN": self.signature,
            "CB-ACCESS-PASSPHRASE": self.api_passphrase,
            "CB-ACCESS-TIMESTAMP": self.cb_access_timestamp,
            "Content-Type": "application/json",
        }


def get_account_info() -> List[TradingAccount]:
    """
    Fetches account info from the Coinbase API.
    Uses the AuthenticatedCoinbase class to get the headers.
    """
    url = settings.API_BASE_URL + "/accounts"
    auth = AuthenticatedCoinbase(method="GET", requestPath="/accounts")
    headers = auth.get_headers()
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        if response.json() == []:
            st.warning("No account info found.", icon="❗️")
            return []
        return convert_json_to_trading_accounts(response.json())
    except HTTPError as http_err:
        st.error(
            f"An error occurred fetching account info: {http_err.response.text}",
            icon="❗️",
        )
        return []
