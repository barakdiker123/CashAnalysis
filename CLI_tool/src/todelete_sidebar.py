"""
This app creates a simple sidebar layout using inline style arguments and the
dbc.Nav component.

dcc.Location is used to track the current location, and a callback uses the
current location to render the appropriate page content. The active prop of
each NavLink is set automatically according to the current pathname. To use
this feature you must install dash-bootstrap-components >= 0.11.0.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dash_table, dcc, callback, Output, Input

import pandas as pd
import plotly.express as px
import yfinance as yf

leumi = yf.download("LUMI.TA", period="15y", interval="1d")
# Incorporate data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "8rem",
    # "margin-right": "2rem",
    "padding": "2rem 1rem",
}
sidebar_list_data = [
    dbc.NavLink("Home", href="/", active="exact"),
    dbc.NavLink("Page 1", href="/page-1", active="exact"),
    dbc.NavLink("Page 2", href="/page-2", active="exact"),
]


sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P("A simple sidebar layout with navigation links", className="lead"),
        dbc.Nav(
            sidebar_list_data,
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


################################################################
# content = html.Div(id="page-content", style=CONTENT_STYLE)

content = html.Div(
    # content = dbc.Container(
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
                # dbc.Col(
                #     [
                #         dash_table.DataTable(
                #             data=df.to_dict("records"),
                #             # page_size=12,
                #             style_table={"overflowX": "auto"},
                #         )
                #     ],
                #     # width=6,
                # ),
                dbc.Col(
                    [dcc.Graph(figure={}, id="my-first-graph-final")]
                ),  # , width=6),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [dcc.Graph(figure={}, id="my-first-graph-final1")]
                ),  # , width=6),
                dbc.Col(
                    [dcc.Graph(figure={}, id="my-first-graph-final2")]
                ),  # , width=6),
            ]
        ),
    ],
    id="page-content",
    style=CONTENT_STYLE,
    # fluid=True,
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


################################################################


app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        # return html.P("This is the content of the home page!")
        return content
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run_server(port=8888)
