import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt  # To visualize
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np


def smooth_plot(ticker, field):
    ticker_regression_data = ticker[field]
    ticker_regression_data = (
        ticker_regression_data.rolling(70).mean().rolling(70).mean()
    )
    ticker_regression_data = ticker_regression_data.dropna()  # drops the NaN elements
    return ticker_regression_data


def change_alignment(ticker_series, a, b):
    ticker_indexes = pd.Series(range(ticker_series.shape[0]))
    X = ticker_indexes.values.reshape(-1, 1)  # values converts it into a numpy array
    Y = ticker_series.values.reshape(-1, 1)
    Y_normalized = Y - (X * a + b)
    # plt.plot(X, Y_normalized, color="red")
    df = pd.DataFrame(Y_normalized, index=ticker_series.index)
    return df


def finding_last_big_change_nelder_mead(ticker_series):
    err = pd.Series()
    indexing = pd.RangeIndex(start=0, stop=len(ticker_series), step=1)
    ticker_series["numbers"] = indexing
    leumi_regression_data_reversed = ticker_series.iloc[
        -45::-1
    ]  # drops the last 30 dates for regression
    count = 0
    for date in leumi_regression_data_reversed.index:  # remove [:1] after tests
        count += 1
        linear_regressor = LinearRegression()  # create object for the class
        current_date = "{}-{}-{}".format(date.year, date.month, date.day)
        current_regression = ticker_series.loc[current_date:]
        linear_regressor.fit(
            current_regression["numbers"].values.reshape(-1, 1),
            current_regression["High"].values.reshape(-1, 1),
        )
        reg = LinearRegression().fit(
            current_regression["numbers"].values.reshape(-1, 1),
            current_regression["High"].values.reshape(-1, 1),
        )
        # r2_score_data = reg.score(current_regression["numbers"].values.reshape(-1,1) , current_regression["High"].values.reshape(-1,1))
        r2_score_data = mean_squared_error(
            current_regression["numbers"].values.reshape(-1, 1),
            current_regression["High"].values.reshape(-1, 1),
        )
        # r2_score_data = mean_absolute_error(current_regression["numbers"].values.reshape(-1,1), current_regression["High"].values.reshape(-1,1))
        temp = pd.Series([r2_score_data], index=[current_date])
        err = pd.concat([err, temp])
    return err


def regression_from_date(ticker, date):
    indexing = pd.RangeIndex(start=0, stop=len(ticker), step=1)
    ticker["numbers"] = indexing
    current_date = "{}-{}-{}".format(date.year, date.month, date.day)
    current_regression = ticker.loc[current_date:]
    linear_regressor = LinearRegression()
    linear_regressor.fit(
        current_regression["numbers"].values.reshape(-1, 1),
        current_regression["High"].values.reshape(-1, 1),
    )
    b = linear_regressor.intercept_
    a = linear_regressor.coef_

    temp = pd.Series(
        linear_regressor.predict(ticker["numbers"].values.reshape(-1, 1)).reshape(-1)
    )
    ticker["Dates"] = ticker.index
    data = ticker.set_index("numbers")
    data["pred y"] = temp
    data = data.set_index("Dates")
    return a.item(), b.item(), data


def auto_calculation(ticker_series, name_ticker):
    df_nelder = smooth_plot(ticker_series, "High")
    df_nelder = pd.DataFrame(df_nelder)
    err = finding_last_big_change_nelder_mead(df_nelder)
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(14, 9))
    a, b, df = regression_from_date(ticker_series, pd.to_datetime(err.idxmin()))

    df["pred y"].plot(ax=axes[0][0], title=name_ticker)  # """ax=axes[0]"""
    df["High"].plot(ax=axes[0][0])  # """ax=axes[0]"""

    # Plot results
    pd_err = pd.DataFrame(err, columns=["err"])
    pd_err["min"] = pd_err.err[
        (pd_err.err.shift(1) > pd_err.err) & (pd_err.err.shift(-1) > pd_err.err)
    ]
    pd_err = pd_err.dropna()  # drops the NaN elements
    pd_err["min"] = pd_err["min"].apply(np.sqrt)
    # plt.scatter(pd_err.index, pd_err['min'], c='r')

    df1 = change_alignment(ticker_series["High"], a, b)
    df1[err.idxmin() :].plot(ax=axes[1][1], title="Global Minimum")
    df1[err.idxmin() :].plot(ax=axes[0][1], kind="hist", title="Global Minimum")

    if len(pd_err) > 0:
        another_date = pd.to_datetime(pd_err.index[0])
        print("Local Regression Date: ", another_date)
        a2, b2, another_reg = regression_from_date(ticker_series, another_date)
        another_reg["pred y"].plot(ax=axes[0][0])

        df2 = change_alignment(ticker_series["High"], a2, b2)
        df2[pd_err.index[0] :].plot(ax=axes[1][2], title="Last Local Minimum")
        df2[pd_err.index[0] :].plot(
            ax=axes[0][2], kind="hist", title="Last Local Minimum"
        )

        # axes[2].set_xlabel(r'Hello ' + txt + r'Hello ')
        # axes[2].text(0.1, 0.5, 'Begin text', horizontalalignment='center', verticalalignment='center', transform=axes[2].transAxes)
    plt.show()
    if len(pd_err) > 0:
        print("Local Regression std:")
        print(df2[pd_err.index[0] :][df2.columns[-1]].std())
        print("Local Regression skew:")
        print(df2[pd_err.index[0] :][df2.columns[-1]].skew())
        print(
            "According to Local Regression you are at ",
            df2[df2.columns[-1]][pd_err.index[0] :].iloc[-1],
        )
        print("Your distance is in std units ")
        print(
            df2[df2.columns[-1]][pd_err.index[0] :].iloc[-1]
            / df2[pd_err.index[0] :][df2.columns[-1]].std()
        )

    print()
    print("Global Regression std:")
    print(df1[err.idxmin() :][df1.columns[-1]].std())
    print("Global Regression skew:")
    print(df1[err.idxmin() :][df1.columns[-1]].skew())
    print(
        "According to Local Regression you are at ",
        df1[df1.columns[-1]][err.idxmin() :].iloc[-1],
    )
    print("Your distance is in std units ")
    print(
        df1[df1.columns[-1]][err.idxmin() :].iloc[-1]
        / df1[err.idxmin() :][df1.columns[-1]].std()
    )

    print()

    print(pd.to_datetime(err.idxmin()))
    print(pd_err)


if __name__ == "__main__":
    leumi = yf.Ticker("LUMI.TA")
    leumi_regression_data = leumi.history(start="2005-01-01", end="2023-09-20")

    auto_calculation(leumi_regression_data, "Leumi")


def todelete():
    print("barak")
