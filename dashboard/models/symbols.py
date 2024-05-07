from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class SymbolCandle:
    """
    Dataclass to represent the candles for a symbol.
    """

    time: datetime
    low: float
    high: float
    open: float
    close: float
    volume: float
    a: int


def convert_json_to_symbol_candles(json_data: list[dict]) -> List[SymbolCandle]:
    """
    Converts the JSON data to a set of SymbolCandle objects.
    :param json_data: JSON data from the API.
    :return: Set of SymbolCandle objects.
    """
    symbol_candles = []
    for data in json_data:
        symbol_candle = SymbolCandle(
            time=datetime.fromtimestamp(data[0]),
            low=data[1],
            high=data[2],
            open=data[3],
            close=data[4],
            volume=data[5],
            a=data[0],
        )
        symbol_candles.append(symbol_candle)
    return symbol_candles
