"""Create a Page Element sidebar."""

import dash_bootstrap_components as dbc
from dash import html, dcc
import yfinance as yf
import first_try_sidebar_demo.css as css
import plotly.express as px
import first_try_sidebar_demo.research_algorithm_near_area as research_algorithm_near_area


def get_content_html_ticker(name_ticker):
    """Create a Page Element one side bar."""
    current_ticker_name = name_ticker + ".TA"
    ticker_data = yf.download(current_ticker_name, period="15y", interval="1d")
    ticker_data["Dates"] = ticker_data.index
    fig = px.line(
        ticker_data,
        x="Dates",
        y=["High", "Low"],
        hover_data={"Dates": "|%B %d, %Y"},
        title="custom tick labels",
    )
    fig_with_regression = research_algorithm_near_area.get_fig_with_regression_algo(
        ticker_data, name_ticker
    )
    #################################################################
    (
        fig_hist_global_minimum,
        fig_plot_global_minimum,
    ) = research_algorithm_near_area.get_fig_hist_from_regression_global(
        ticker_data, name_ticker
    )
    #################################################################
    (
        fig_hist_local_minimum,
        fig_plot_local_minimum,
    ) = research_algorithm_near_area.get_fig_hist_from_regression_local(
        ticker_data, name_ticker
    )
    #################################################################
    content = html.Div(
        [
            dbc.Row(
                [
                    html.Div(
                        "The Name of the Ticker is:" + name_ticker,
                        className="text-primary text-center fs-3",
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(
                                figure=fig,
                            )
                        ]
                    )
                ]
            ),
            dbc.Row([dbc.Col([dcc.Graph(figure=fig_with_regression)])]),
            dbc.Row(
                [
                    dbc.Col([dcc.Graph(figure=fig_hist_global_minimum)]),
                    dbc.Col([dcc.Graph(figure=fig_plot_global_minimum)]),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col([dcc.Graph(figure=fig_hist_local_minimum)]),
                    dbc.Col([dcc.Graph(figure=fig_plot_local_minimum)]),
                ]
            ),
            # dbc.Row(
            #     [
            #         dbc.Col(
            #             [
            #                 dcc.Graph(
            #                     figure=fig,
            #                 )
            #             ]
            #         ),
            #         dbc.Col(
            #             [
            #                 dcc.Graph(
            #                     figure=fig,
            #                 )
            #             ]
            #         ),
            #     ]
            # ),
            # dbc.Row(
            #     [
            #         dbc.Col(
            #             [
            #                 dcc.Graph(
            #                     figure=fig,
            #                 )
            #             ]
            #         ),
            #         dbc.Col(
            #             [
            #                 dcc.Graph(
            #                     figure=fig,
            #                 )
            #             ]
            #         ),
            #     ]
            # ),
        ],
        style=css.CONTENT_STYLE,
    )
    return content
