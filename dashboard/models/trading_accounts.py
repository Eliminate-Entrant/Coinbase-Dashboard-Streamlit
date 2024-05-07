from dataclasses import dataclass
from typing import List
import pandas as pd


@dataclass
class TradingAccount:
    """
    Dataclass to represent the trading accounts on Coinbase.
    """

    id: str
    currency: str
    balance: float
    hold: float
    available: int
    profile_id: str
    trading_enabled: bool
    pending_deposit: float
    display_name: str


def convert_json_to_trading_accounts(json_data: list[dict]) -> List[TradingAccount]:
    """
    Converts the JSON data to a set of TradingAccounts objects.
    :param json_data: JSON data from the API.
    :return: Set of TradingAccounts objects.
    """
    trading_accounts = []
    for data in json_data:
        trading_account = TradingAccount(
            id=data["id"],
            currency=data["currency"],
            balance=float(data["balance"]),
            hold=float(data["hold"]),
            available=int(data["available"]),
            profile_id=data["profile_id"],
            trading_enabled=data["trading_enabled"],
            pending_deposit=float(data["pending_deposit"]),
            display_name=data["display_name"],
        )
        trading_accounts.append(trading_account)
    return trading_accounts
