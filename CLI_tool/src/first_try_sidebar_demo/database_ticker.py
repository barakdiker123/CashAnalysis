# Here I'll store the DataFrames from yfinance
# "Ticker_name" : df
database_ticker = {}
database_ticker_new = {}


# Download 15 years of historical stocks using the daily time frame
# tickers = [
#    "TA35.TA",
#    "TA90.TA",
#    "LUMI.TA",
#    "DSCT.TA",
#    "BEZQ.TA",
#    "CEL.TA",
#    "ESLT.TA",
#    "NICE.TA",
#    "TEVA.TA",
#    "POLI.TA",
#    "MZTF.TA",
#    "FIBI.TA",
#    "HARL.TA",
#    "MGDL.TA",
#    "CLIS.TA",
#    "PHOE.TA",
#    "MMHD.TA",
#    "DRS.TA",
#    "BSEN.TA",
#    "HLAN.TA",
#    "FTAL.TA",
#    "DANE.TA",
#    "ONE.TA",
#    "MTRX.TA",
#    "ALHE.TA",
#    "UWAY.TA",
#    "TRAN.TA",
# ]

ticker_indexes = [
    "TA35.TA",
    # "TA90.TA",
    # "DSCT.TA",
]
ticker_stocks = [
    "LUMI.TA",
    "DSCT.TA",
    "BEZQ.TA",
    "CEL.TA",
    "ESLT.TA",
    "NICE.TA",
    "TEVA.TA",
    "POLI.TA",
    "MZTF.TA",
    "FIBI.TA",
    "HARL.TA",
    "MGDL.TA",
    "CLIS.TA",
    "PHOE.TA",
    "MMHD.TA",
    "DRS.TA",
    "BSEN.TA",
    "HLAN.TA",
    "FTAL.TA",
    "DANE.TA",
    "ONE.TA",
    "MTRX.TA",
    "ALHE.TA",
    "UWAY.TA",
    "TRAN.TA",
    "ICL.TA",
]

ticker_stocks = sorted(ticker_stocks)
