# Add controls to build the interaction

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import yfinance as yf

leumi = yf.download("LUMI.TA", period="15y", interval="1d")

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)


@callback(
    Output(component_id="my-first-graph-final", component_property="figure"),
    Input(component_id="radio-buttons-final", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig


@callback(
    Output(component_id="my-first-graph-final1", component_property="figure"),
    Input(component_id="radio-buttons-final", component_property="value"),
)
def update_graph1(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig


@callback(
    Output(component_id="my-first-graph-final2", component_property="figure"),
    Input(component_id="radio-buttons-final", component_property="value"),
    Input(component_id="radio-buttons-final", component_property="value"),
)
def update_graph2(col_chosen, param):
    df1 = leumi
    # df1 = pd.DataFrame(leumi["High"])
    # df = pd.DataFrame(leumi)
    df1["Dates"] = df1.index
    # df["High Original"] = leumi["High"]
    fig = px.line(
        df1,
        x="Dates",
        y=["High", "Low"],
        hover_data={"Dates": "|%B %d, %Y"},
        title="custom tick labels",
    )

    return fig


@callback(
    Output(component_id="my-first-graph-final3", component_property="figure"),
    Input(component_id="radio-buttons-final", component_property="value"),
    Input(component_id="radio-buttons-final", component_property="value"),
)
def update_graph3(col_chosen, param):
    df1 = leumi
    # df1 = pd.DataFrame(leumi["High"])
    # df = pd.DataFrame(leumi)
    df1["Dates"] = df1.index
    # df["High Original"] = leumi["High"]
    fig = px.line(
        df1,
        x="Dates",
        y=["High", "Low"],
        hover_data={"Dates": "|%B %d, %Y"},
        title="custom tick labels",
    )
    return fig


# @callback(
#    Output(component_id="generic-graph", component_property="figure"),
#    [Input("url", "pathname")],
# )
# def update_generic_graph(pathname):
#    # pathname = ticker's name
#    current_ticker_name = pathname[1:]
#    current_ticker_name = current_ticker_name + ".TA"
#    ticker_data = yf.download(current_ticker_name, period="15y", interval="1d")
#    ticker_data["Dates"] = ticker_data.index
#    fig = px.line(
#        ticker_data,
#        x="Dates",
#        y=["High", "Low"],
#        hover_data={"Dates": "|%B %d, %Y"},
#        title="custom tick labels",
#    )
#    return fig
