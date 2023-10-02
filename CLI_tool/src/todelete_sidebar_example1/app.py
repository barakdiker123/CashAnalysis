import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.SPACELAB],
    suppress_callback_exceptions=True,
)
sidebar = dbc.Nav(
    [
        dbc.NavLink(
            [
                html.Div(page["name"], className="ms-2"),
            ],
            href=page["path"],
            active="exact",
        )
        for page in dash.page_registry.values()
    ],
    vertical=False,
    pills=True,
    className="text-center border",
    justified=True,
    fill=True,
    style={"position": "fixed"},
)

app.layout = dbc.Container(
    [dbc.Row(sidebar), html.Hr(), dbc.Row(dash.page_container)], fluid=True
)


if __name__ == "__main__":
    app.run_server(debug=True)
