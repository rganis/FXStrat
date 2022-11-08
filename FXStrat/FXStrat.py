# Description: This script will download the EURUSD data from Yahoo Finance
#
# do the imports
import pandas as pd;
import numpy as np;
import yfinance as yf;
import datetime as dt;
# get the data
tickers = ["EURUSD=X", "GBPUSD=X"]

for y in tickers:
    tix = yf.Ticker(tickers[y])
    hist = tix.history(period="1mo")
    df = pd.DataFrame(hist)
    c = np.average(df['Close'])
    print(c)
#tix = yf.Ticker("EURUSD=X")
# get the historical prices for this ticker
# 1mo is 1 calendar month, approx 20 trading days
#hist = eu.history(period="1mo")
#df = pd.DataFrame(hist)
#c = np.average(df['Close'])
#print(c)