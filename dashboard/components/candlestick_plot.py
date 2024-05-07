import plotly.graph_objects as go
import pandas as pd


def candlestick_plot(
    symbol_candles: pd.DataFrame,
    quote_currency: str,
    increase_color: str = "green",
    decrease_color: str = "red",
) -> go.Figure:
    """
    Plots the candlestick chart for the given symbol candles.
    :param symbol_candles: List of SymbolCandle objects.
    :param quote_currency: Quote currency of the trading pair.
    :param increase_color: Color for the increasing candles.
    :param decrease_color: Color for the decreasing candles.
    """
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=symbol_candles["time"],
                open=symbol_candles["open"],
                high=symbol_candles["high"],
                low=symbol_candles["low"],
                close=symbol_candles["close"],
                increasing_line_color=increase_color,
                decreasing_line_color=decrease_color,
            )
        ]
    )
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title=f"Price in {quote_currency}",
        hovermode="x unified",
    )
    return fig
