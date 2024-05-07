import sys
import streamlit as st

from pydantic import ValidationError, SecretStr
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    API_BASE_URL: str
    API_BASE_URL_WSS: str = ""
    API_KEY: SecretStr = ""
    API_SECRET: SecretStr = ""
    API_PASSPHRASE: SecretStr = ""

    class Config:
        case_sensitive = True
        env_prefix = "COINBASE_"
        env_file = ".env"
        extra = "ignore"


try:
    settings = Settings()  # type: ignore
except ValidationError as e:
    print(e)
    st.error(
        """
        An error occurred loading the settings. 
        Please check your environment variables and that BASE URL is set correctly.
        """,
        icon="❗️",
    )
    st.stop()
    sys.exit(1)
