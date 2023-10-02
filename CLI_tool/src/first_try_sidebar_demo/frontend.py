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
import css

import plotly.express as px
import yfinance as yf
import backend
import display_page
import auxiliry
from auxiliry import leumi

# leumi = yf.download("LUMI.TA", period="15y", interval="1d")
# Incorporate data

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
sidebar_list_data = [
    dbc.NavLink("Demo", href="/", active="exact"),
    dbc.NavLink("Tick LUMI.TA", href="/LUMI", active="exact"),
    dbc.NavLink("Tick CEL.TA", href="/CEL", active="exact"),
    dbc.NavLink("Page 3", href="/LEUMI", active="exact"),
]


sidebar = html.Div(
    [
        html.H2("Tickers", className="display-4"),
        html.Hr(),
        html.P("Please select your Ticker from the sidebar layout", className="lead"),
        dbc.Nav(
            sidebar_list_data,
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


################################################################


################################################################

content = html.Div(id="page-content", style=css.CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        # return html.P("This is the content of the home page!")
        return backend.get_content()
    elif pathname == "/LUMI":
        print(pathname[1:])
        return display_page.get_content_html_ticker(pathname[1:])  # "LUMI"
        # html.P("This is the content of page 1. Yay!")
    elif pathname == "/CEL":
        print(pathname[1:])
        return display_page.get_content_html_ticker(pathname[1:])  # "LUMI"
    elif pathname == "/LEUMI":
        return html.P("Oh cool, this is page 3!" + pathname[1:])
        # return display_page.get_content_html_ticker_custom(pathname[1:])
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
