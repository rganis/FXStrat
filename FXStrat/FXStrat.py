# Description: This script will download the EURUSD data from Yahoo Finance
#
# do the imports
import pandas as pd;
from pandas import read_csv;
import numpy as np;
import yfinance as yf;
import datetime as dt;
# get the data
aapl = yf.Ticker("EURUSD=X")
# get the historical prices for this ticker
# 1mo is 1 calendar month, approx 20 trading days
hist = aapl.history(period="1mo")
print(hist)