import dash_bootstrap_components as dbc
import css
from dash import html, dcc


def get_content():
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
            # dbc.Row([dbc.Col([dcc.Graph(figure={}, id="my-first-graph-final3")])]),
        ],
        # id="page-content",
        style=css.CONTENT_STYLE,
        # fluid=True,
    )
    return content
