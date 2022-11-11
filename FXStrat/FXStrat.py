# Description: This script will download Forex data from Yahoo Finance and compute a correlation matrix
#
# Do the imports
import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
# Get the data and store as an array of pandas dataframes
tickers = ["EURUSD=X", "GBPUSD=X", "AUDUSD=X", "NZDUSD=X", "USDCAD=X", "USDCHF=X", "USDJPY=X", "EURGBP=X", "EURJPY=X", "EURCHF=X", "EURCAD=X", "EURAUD=X", "EURNZD=X", "GBPJPY=X",
           "GBPCHF=X", "GBPCAD=X", "GBPAUD=X", "GBPNZD=X", "AUDJPY=X", "AUDCHF=X", "AUDCAD=X", "AUDNZD=X", "NZDJPY=X", "NZDCHF=X", "NZDCAD=X", "CADJPY=X", "CADCHF=X", "CHFJPY=X"]
y = 0
arr_len = len(tickers)
t1arr = []
for y in range (0, arr_len):
    tix = yf.Ticker(tickers[y])
    df1 = pd.DataFrame(tix.history(period="1mo"))
    df2 = df1.reset_index(drop=True)
    df3 = df2["Close"]
    t1arr.append(df3)
    y += 1
# compute the correlation matrix
dft = pd.DataFrame(data = t1arr)
df = dft.transpose()

# Print the dataframe
print("Data Frame")
print(df)
print()

# Print the correlation matrix
print("Correlation Matrix")
print(df.corr())
print()

# Drop self-correlations
def get_redundant_pairs(df):
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

# Get top 3 correlated pairs
def get_top_abs_correlations(df, n=5):
    au_corr = df.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]

print("Top Correlations")
print(get_top_abs_correlations(df, 3))