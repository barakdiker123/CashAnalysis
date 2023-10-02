from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import yfinance as yf

leumi = yf.download("LUMI.TA", period="15y", interval="1d")
# Incorporate data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                html.Div(
                    "My First App with Data, Graph, and Controls",
                    className="text-primary text-center fs-3",
                )
            ]
        ),
        dbc.Row(
            [
                dbc.RadioItems(
                    options=[
                        {"label": x, "value": x}
                        for x in ["pop", "lifeExp", "gdpPercap"]
                    ],
                    value="lifeExp",
                    inline=True,
                    id="radio-buttons-final",
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dash_table.DataTable(
                            data=df.to_dict("records"),
                            page_size=12,
                            style_table={"overflowX": "auto"},
                        )
                    ],
                    width=6,
                ),
                dbc.Col([dcc.Graph(figure={}, id="my-first-graph-final")], width=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col([dcc.Graph(figure={}, id="my-first-graph-final1")], width=6),
                dbc.Col([dcc.Graph(figure={}, id="my-first-graph-final2")], width=6),
            ]
        ),
    ],
    fluid=True,
)


# Add controls to build the interaction
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


# Run the app

if __name__ == "__main__":
    app.run(debug=True)
