from streamlit.testing.v1 import AppTest


def test_historical_prices_page():
    at = AppTest.from_file("./dashboard/pages/1_Historical_Prices.py").run()

    assert not at.exception
    assert at.metric
    assert at.get("plotly_chart")
