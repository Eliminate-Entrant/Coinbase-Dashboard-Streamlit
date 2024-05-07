from streamlit.testing.v1 import AppTest


def test_title():
    at = AppTest.from_file("./dashboard/Home.py").run()
    assert at.title[0].value == "Coinbase Dashboard"


def test_launch_dashboard():
    at = AppTest.from_file("./dashboard/Home.py").run()
    assert not at.exception


def test_trading_pairs():
    at = AppTest.from_file("./dashboard/Home.py").run()
    assert at.metric


def test_data_frame_display():
    at = AppTest.from_file("./dashboard/Home.py").run()
    assert at.dataframe  # Check if a dataframe is displayed
