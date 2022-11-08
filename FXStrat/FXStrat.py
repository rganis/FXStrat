# Description: This script will download Forex data from Yahoo Finance and compute a correlation matrix
#
# do the imports
import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
# get the data
tickers = ["EURUSD=X", "GBPUSD=X", "AUDUSD=X", "NZDUSD=X", "USDCAD=X", "USDCHF=X", "USDJPY=X", "EURGBP=X", "EURJPY=X", "EURCHF=X", "EURCAD=X", "EURAUD=X", "EURNZD=X", "GBPJPY=X",
           "GBPCHF=X", "GBPCAD=X", "GBPAUD=X", "GBPNZD=X", "AUDJPY=X", "AUDCHF=X", "AUDCAD=X", "AUDNZD=X", "NZDJPY=X", "NZDCHF=X", "NZDCAD=X", "CADJPY=X", "CADCHF=X", "CHFJPY=X"]
y = 0
arr_len = len(tickers)
t1arr = []
for y in range(0, arr_len):
    if y < arr_len-1:
        tix = yf.Ticker(tickers[y])
        df1 = pd.DataFrame(tix.history(period="1mo"))
        df2 = pd.DataFrame(yf.Ticker(tickers[y+1]).history(period="1mo"))
        c = np.correlate(df1['Close'], df2['Close'])
        y += 1
        t1arr.append(c)
    else:
        break
print(t1arr)
