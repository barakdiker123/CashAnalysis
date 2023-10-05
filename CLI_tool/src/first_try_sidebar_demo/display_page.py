"""Create a Page Element sidebar."""

import dash_bootstrap_components as dbc
from dash import html, dcc
import yfinance as yf
import css
import plotly.express as px
import research_algorithm_near_area

# import database
import database_ticker

# database_ticker = {}


class DataAnalysisTicker:
    """Save the data and calculation of each Ticker."""

    def __init__(self, name_ticker):
        """Calculate and create display object of each element"""
        self.name_ticker = name_ticker
        current_ticker_name = self.name_ticker
        self.ticker_data = yf.download(current_ticker_name, period="10y", interval="1d")
        if self.ticker_data.empty:
            print("Empty DataFrame ", name_ticker)
        self.ticker_data["Dates"] = self.ticker_data.index

        self.fig = px.line(
            self.ticker_data,
            x="Dates",
            y=["High", "Low"],
            hover_data={"Dates": "|%B %d, %Y"},
            title="Ticker " + self.name_ticker + " displaying High low in days",
        )

        # self.fig_with_regression = (
        #    research_algorithm_near_area.get_fig_with_regression_algo(
        #        self.ticker_data, self.name_ticker
        #    )
        # )
        ##################################################################
        # (
        #    self.fig_hist_global_minimum,
        #    self.fig_plot_global_minimum,
        #    self.global_regression_std,
        #    self.global_regression_skew,
        #    self.global_distance_from_regression_to_current_day,
        #    self.global_distance_from_regression_to_current_day_in_std,
        #    self.global_regression_date,
        # ) = research_algorithm_near_area.get_fig_hist_from_regression_global(
        #    self.ticker_data, self.name_ticker
        # )
        ##################################################################
        # (
        #    self.fig_hist_local_minimum,
        #    self.fig_plot_local_minimum,
        #    self.local_regression_std,
        #    self.local_regression_skew,
        #    self.local_distance_from_regression_to_current_day,
        #    self.local_distance_from_regression_to_current_day_in_std,
        #    self.local_regression_date,
        # ) = research_algorithm_near_area.get_fig_hist_from_regression_local(
        #    self.ticker_data, self.name_ticker
        # )
        #################################################################
        #################################################################
        #################################################################
        #################################################################

        # Optimize Algo
        (
            self.fig_with_regression,
            self.fig_hist_global_minimum,
            self.fig_plot_global_minimum,
            self.global_regression_std,
            self.global_regression_skew,
            self.global_distance_from_regression_to_current_day,
            self.global_distance_from_regression_to_current_day_in_std,
            self.global_regression_date,
            self.fig_hist_local_minimum,
            self.fig_plot_local_minimum,
            self.local_regression_std,
            self.local_regression_skew,
            self.local_distance_from_regression_to_current_day,
            self.local_distance_from_regression_to_current_day_in_std,
            self.local_regression_date,
        ) = research_algorithm_near_area.auto_calculation_production(
            self.ticker_data, self.name_ticker
        )


def get_content_from_DataAnalysisTicker(data: DataAnalysisTicker):
    content = html.Div(
        [
            dbc.Row(
                [
                    html.Div(
                        "The Name of the Ticker is:" + data.name_ticker,
                        className="text-primary text-center fs-3",
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(
                                figure=data.fig,
                            )
                        ]
                    )
                ]
            ),
            dbc.Row([dbc.Col([dcc.Graph(figure=data.fig_with_regression)])]),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col([dcc.Graph(figure=data.fig_hist_global_minimum)]),
                    dbc.Col([dcc.Graph(figure=data.fig_plot_global_minimum)]),
                ]
            ),
            dbc.Row(
                html.Table(
                    children=[
                        html.Thead(
                            children=[
                                html.Tr(
                                    children=[
                                        html.Th("Property "),
                                        html.Th("Data "),
                                    ]
                                )
                            ]
                        ),
                        html.Tbody(
                            children=[
                                html.Tr(
                                    children=[
                                        html.Td(
                                            "Global Regression std:",
                                        ),
                                        html.Td(str(data.global_regression_std)),
                                    ]
                                ),
                                html.Tr(
                                    children=[
                                        html.Td(
                                            "Global Regression skew:",
                                        ),
                                        html.Td(str(data.global_regression_skew)),
                                    ]
                                ),
                                html.Tr(
                                    children=[
                                        html.Td(
                                            "According to Global regression your distance is:",
                                        ),
                                        html.Td(
                                            str(
                                                data.global_distance_from_regression_to_current_day
                                            )
                                        ),
                                    ]
                                ),
                                html.Tr(
                                    className="active-row"
                                    if 0.5
                                    < data.global_distance_from_regression_to_current_day_in_std
                                    < 1.5
                                    or -0.5
                                    > data.global_distance_from_regression_to_current_day_in_std
                                    > -1.5
                                    else "",
                                    children=[
                                        html.Td(
                                            "According to Global regression in std your distance is:",
                                        ),
                                        html.Td(
                                            str(
                                                data.global_distance_from_regression_to_current_day_in_std
                                            )
                                        ),
                                    ],
                                ),
                                html.Tr(
                                    children=[
                                        html.Td(
                                            "Regression from Date: ",
                                        ),
                                        html.Td(str(data.global_regression_date)),
                                    ]
                                ),
                            ]
                        ),
                    ],
                    className="styled-table",
                )
            ),
            #    dbc.Row(
            #        [
            #            dbc.Col(
            #                [
            #                    html.Div(
            #                        "Global Regression std:"
            #                        + str(data.global_regression_std),
            #                        className="text-center",
            #                    ),
            #                    html.Div(
            #                        "Global Regression skew:"
            #                        + str(data.global_regression_skew),
            #                        className="text-center",
            #                    ),
            #                    html.Div(
            #                        "According to Global regression your distance is:"
            #                        + str(
            #                            data.global_distance_from_regression_to_current_day
            #                        ),
            #                        className="text-center",
            #                    ),
            #                    html.Div(
            #                        "According to Global regression in std your distance is:"
            #                        + str(
            #                            data.global_distance_from_regression_to_current_day_in_std
            #                        ),
            #                        className="text-center",
            #                    ),
            #                    html.Div(
            #                        "Regression from Date: "
            #                        + str(data.global_regression_date),
            #                        className="text-center",
            #                    ),
            #                ]
            #            )
            #        ]
            #    ),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col([dcc.Graph(figure=data.fig_hist_local_minimum)]),
                    dbc.Col([dcc.Graph(figure=data.fig_plot_local_minimum)]),
                ]
            ),
            dbc.Row(
                html.Table(
                    children=[
                        html.Thead(
                            children=[
                                html.Tr(
                                    children=[
                                        html.Th("Property "),
                                        html.Th("Data "),
                                    ]
                                )
                            ]
                        ),
                        html.Tbody(
                            children=[
                                html.Tr(
                                    children=[
                                        html.Td(
                                            "Local Regression std:",
                                        ),
                                        html.Td(str(data.local_regression_std)),
                                    ]
                                ),
                                html.Tr(
                                    children=[
                                        html.Td(
                                            "Local Regression skew:",
                                        ),
                                        html.Td(str(data.local_regression_skew)),
                                    ]
                                ),
                                html.Tr(
                                    children=[
                                        html.Td(
                                            "According to Local regression your distance is:",
                                        ),
                                        html.Td(
                                            str(
                                                data.local_distance_from_regression_to_current_day
                                            )
                                        ),
                                    ]
                                ),
                                html.Tr(
                                    className="active-row"
                                    if 0.5  # minimum distance from std to current day
                                    < data.local_distance_from_regression_to_current_day_in_std
                                    < 1.5  # maximum distance from std to current day
                                    or -0.5
                                    > data.local_distance_from_regression_to_current_day_in_std
                                    > -1.5
                                    else "",
                                    children=[
                                        html.Td(
                                            "According to Local regression in std your distance is:",
                                        ),
                                        html.Td(
                                            str(
                                                data.local_distance_from_regression_to_current_day_in_std
                                            )
                                        ),
                                    ],
                                ),
                                html.Tr(
                                    children=[
                                        html.Td(
                                            "Regression from Date: ",
                                        ),
                                        html.Td(str(data.local_regression_date)),
                                    ]
                                ),
                            ]
                        ),
                    ],
                    className="styled-table",
                )
            ),
            #    dbc.Row(
            #        [
            #            dbc.Col(
            #                [
            #                    html.Div(
            #                        "local Regression std:"
            #                        + str(data.local_regression_std),
            #                        className="text-center",
            #                    ),
            #                    html.Div(
            #                        "local Regression skew:"
            #                        + str(data.local_regression_skew),
            #                        className="text-center",
            #                    ),
            #                    html.Div(
            #                        "According to local regression your distance is:"
            #                        + str(
            #                            data.local_distance_from_regression_to_current_day
            #                        ),
            #                        className="text-center",
            #                    ),
            #                    html.Div(
            #                        "According to local regression in std your distance is:"
            #                        + str(
            #                            data.local_distance_from_regression_to_current_day_in_std
            #                        ),
            #                        className="text-center",
            #                    ),
            #                    html.Div(
            #                        "Regression from Date: "
            #                        + str(data.local_regression_date),
            #                        className="text-center",
            #                    ),
            #                ]
            #            )
            #        ]
            #    ),
        ],
        style=css.CONTENT_STYLE,
    )
    return content


def process_data():
    tickers = database_ticker.ticker_indexes + database_ticker.ticker_stocks

    tickers_DataAnalysisTicker = map(
        lambda ticker_name: DataAnalysisTicker(ticker_name), tickers
    )
    tickers_content = map(
        lambda obj_DataAnalysisTicker: get_content_from_DataAnalysisTicker(
            obj_DataAnalysisTicker
        ),
        tickers_DataAnalysisTicker,
    )
    # Given a name of ticker return the required displayed object
    dict_display_data = dict(map(lambda i, j: (i, j), tickers, tickers_content))
    return dict_display_data


# Deprecated !
def get_content_html_ticker(name_ticker):
    """Create a Page Element one side bar."""
    current_ticker_name = name_ticker + ".TA"
    if current_ticker_name in database_ticker.database_ticker:
        ticker_data = database_ticker.database_ticker[current_ticker_name]
    else:
        ticker_data = yf.download(current_ticker_name, period="15y", interval="1d")
        database_ticker.database_ticker[current_ticker_name] = ticker_data
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
