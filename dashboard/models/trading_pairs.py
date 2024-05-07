from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, Set


@dataclass
class TradingPair:
    """
    Dataclss to represent all the trading pairs on Coinbase.
    """

    id: str
    base_currency: str
    quote_currency: str
    quote_increment: float
    base_increment: float
    display_name: str
    min_market_funds: float
    margin_enabled: bool
    post_only: bool
    limit_only: bool
    cancel_only: bool
    status: str
    status_message: str
    trading_disabled: bool
    fx_stablecoin: bool
    max_slippage_percentage: float
    auction_mode: bool
    high_bid_limit_percentage: str


def convert_json_to_trading_pairs(json_data: list[dict]) -> Dict[str, TradingPair]:
    """
    Converts the JSON data to a set of TradingPair objects.
    :param json_data: JSON data from the API.
    :return: Set of TradingPair objects.
    """
    trading_pairs = {}
    for data in json_data:
        trading_pair = TradingPair(
            id=data["id"],
            base_currency=data["base_currency"],
            quote_currency=data["quote_currency"],
            quote_increment=float(data["quote_increment"]),
            base_increment=float(data["base_increment"]),
            display_name=data["display_name"],
            min_market_funds=float(data["min_market_funds"]),
            margin_enabled=data["margin_enabled"],
            post_only=data["post_only"],
            limit_only=data["limit_only"],
            cancel_only=data["cancel_only"],
            status=data["status"],
            status_message=data["status_message"],
            trading_disabled=data["trading_disabled"],
            fx_stablecoin=data["fx_stablecoin"],
            max_slippage_percentage=float(data["max_slippage_percentage"]),
            auction_mode=data["auction_mode"],
            high_bid_limit_percentage=data["high_bid_limit_percentage"],
        )
        trading_pairs[trading_pair.id] = trading_pair
    return trading_pairs
