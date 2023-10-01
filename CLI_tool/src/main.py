import plotly.express as px
import pandas as pd

import yfinance as yf
import backend.fifth_demo_backend as be
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def smooth_plot(ticker, field):
    ticker_regression_data = ticker[field]
    ticker_regression_data = (
        ticker_regression_data.rolling(70).mean().rolling(70).mean()
    )
    ticker_regression_data = ticker_regression_data.dropna()  # drops the NaN elements
    return ticker_regression_data


def pretty_display(ticker, fields):
    df = ticker
    df["Dates"] = df.index
    # df["High Original"] = leumi["High"]
    fig = px.line(
        df,
        x="Dates",
        y=fields,
        hover_data={"Dates": "|%B %d, %Y"},
        title="custom tick labels",
    )
    fig.show()


def demo1():
    """Create a new demo"""
    leumi = yf.download("LUMI.TA", period="15y", interval="1d")
    df = pd.DataFrame(smooth_plot(leumi, "High"))
    # df = pd.DataFrame(leumi)
    df["Dates"] = df.index
    # df["High Original"] = leumi["High"]
    fig = px.line(
        df,
        x="Dates",
        y=["High"],
        hover_data={"Dates": "|%B %d, %Y"},
        title="custom tick labels",
    )
    fig.show()


def demo2():
    leumi = yf.download("LUMI.TA", period="15y", interval="1d")
    df = pd.DataFrame(smooth_plot(leumi, "High"))
    # df = pd.DataFrame(leumi)
    df["Dates"] = df.index
    fig = make_subplots(rows=1, cols=2)
    # example
    # fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]), row=1, col=1)
    # fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]), row=1, col=2)
    fig.add_trace(
        go.Scatter(x=df["Dates"], y=df["High"]),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=df["Dates"], y=df["High"]),
        row=1,
        col=2,
    )

    fig.update_layout(title_text="Side By Side Subplots")  # height=600, width=800,
    fig.show()


def example1():
    df = px.data.stocks()
    fig = px.line(
        df,
        x="date",
        y=df.columns,
        hover_data={"date": "|%B %d, %Y"},
        title="custom tick labels",
    )
    fig.show()


# example1()
# demo1()


def example2():
    leumi = yf.download("LUMI.TA", period="15y", interval="1d")
    pretty_display(leumi, ["High"])
    be.todelete()


def example3():
    demo2()


example3()
