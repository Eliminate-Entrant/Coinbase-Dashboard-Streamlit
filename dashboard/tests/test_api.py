import pytest
from unittest.mock import patch
from api.coinbase import TradingSymbolsManager


@pytest.fixture
def trading_symbols_manager():
    return TradingSymbolsManager()


@patch("requests.get")
def test_fetch_trading_symbols_success(
    trading_symbols_manager,
):
    assert trading_symbols_manager.fetch_trading_symbols()
    assert len(trading_symbols_manager.get_trading_symbols()) == 0


def test_get_trading_symbols_filled(trading_symbols_manager):
    assert trading_symbols_manager.get_trading_symbols() != []
    assert len(trading_symbols_manager.get_trading_symbols()) == 12
