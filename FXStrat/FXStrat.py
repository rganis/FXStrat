# Description: This script will download the EURUSD data from Yahoo Finance
#
# do the imports
import pandas as pd;
import numpy as np;
import yfinance as yf;
import datetime as dt;
# get the data
aapl = yf.Ticker("EURUSD=X")
# get the historical prices for this ticker
hist = aapl.history(period="1mo")
print(hist)