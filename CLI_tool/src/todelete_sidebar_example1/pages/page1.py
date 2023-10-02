import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)
dash.register_page(__name__, path="/", name="Page 1")


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 42,
    "left": 0,
    "bottom": 0,
    "background-color": "#f8f9fa",
    "overflowY": "auto",
}

CONTENT_STYLE = {"display": "inline-block"}

content = dcc.RadioItems(
    ["New York City", "Montreal", "San Francisco"],
    "Montreal",
    labelStyle={"display": "block"},
)


def layout():
    sidebar = html.Div(
        [
            html.H2("Sidebar", className="display-4"),
            html.Hr(),
            html.P("A simple sidebar layout with navigation linkasdasdasdasdassdss"),
            content,
        ],
        style=SIDEBAR_STYLE,
    )
    return sidebar
