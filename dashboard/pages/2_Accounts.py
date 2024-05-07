import streamlit as st

from config import settings
from api.coinbase import get_account_info
from components.custom_card import show_trading_accounts

st.title("Trading Accounts")

if (
    settings.API_KEY.get_secret_value() == ""
    or settings.API_SECRET.get_secret_value() == ""
    or settings.API_PASSPHRASE.get_secret_value() == ""
):
    st.sidebar.status("🔒 Unauthorized")
    st.sidebar.info(
        "Please make sure that all API environment variables are non-empty. And then restart the Streamlit server."
    )
else:
    st.sidebar.success("🔓 Authorized")
    st.sidebar.info("You are authorized to access the Coinbase API.")


accounts_ = get_account_info()

show_trading_accounts(accounts_)
