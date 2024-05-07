import plotly.graph_objects as go
import pandas as pd

COLORS = {
    "open": "lightskyblue",
    "high": "lightgreen",
    "low": "red",
    "close": "black",
}


def line_plot(
    symbol_candles: pd.DataFrame,
    quote_currency: str,
    ticker: list[str],
    colors: dict[str, str] = COLORS,
) -> go.Figure:
    """
    Plots the line chart for the given symbol candles.
    :param symbol_candles: List of SymbolCandle objects.
    """
    fig = go.Figure()
    for i in ticker:
        fig.add_trace(
            go.Scatter(
                x=symbol_candles["time"],
                y=symbol_candles[i],
                mode="lines",
                name=i,
                line=dict(color=colors[i], width=1.5),
            )
        )

    fig.update_layout(
        xaxis_title="Time",
        yaxis_title=f"Price in {quote_currency}",
        hovermode="x unified",
    )
    return fig
