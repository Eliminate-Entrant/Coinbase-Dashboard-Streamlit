import streamlit as st
from models.trading_accounts import TradingAccount


def custom_wallet_card(account: TradingAccount):
    """
    Custom card for the trading account.
    """
    card_style = """
        <div style="border: 1px solid #ccc; border-radius: 10px; padding: 15px; margin-bottom: 20px;">
            <h3 style="margin-bottom: 10px;color: {display_color}">{display_name}</h3>
            <div><strong>Balance:</strong> {balance}</div>
            <div><strong>Hold:</strong> {hold}</div>
            <div><strong>Available:</strong> {available}</div>
            <div><strong>Pending Deposit:</strong> {pending_deposit}</div>
        </div>
    """
    display_color = "#4CAF50" if account.trading_enabled else "#F44336"
    return card_style.format(
        display_name=account.display_name,
        balance=account.balance,
        hold=account.hold,
        available=account.available,
        pending_deposit=account.pending_deposit,
        display_color=display_color,
    )


def show_trading_accounts(accounts: list[TradingAccount]):
    """
    Generates custom wallet cards for the trading accounts.
    Max 3 cards per row.
    :param accounts: List of TradingAccount objects.
    """
    for i in range(0, len(accounts), 3):
        row_data = accounts[i : i + 3]
        cols = st.columns(3)
        for col, account in zip(cols, row_data):
            col.markdown(custom_wallet_card(account), unsafe_allow_html=True)
