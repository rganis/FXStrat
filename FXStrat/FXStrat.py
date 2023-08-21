# Description: This script will download Forex data from Yahoo Finance and compute a correlation matrix
#
# Do the imports
import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
# Get the data and store as an array of dataframes
tickers = ["EURUSD=X", "GBPUSD=X", "AUDUSD=X", "NZDUSD=X", "USDCAD=X", "USDCHF=X", "USDJPY=X", "EURGBP=X", "EURJPY=X", "EURCHF=X", "EURCAD=X", "EURAUD=X", "EURNZD=X", "GBPJPY=X",
           "GBPCHF=X", "GBPCAD=X", "GBPAUD=X", "GBPNZD=X", "AUDJPY=X", "AUDCHF=X", "AUDCAD=X", "AUDNZD=X", "NZDJPY=X", "NZDCHF=X", "NZDCAD=X", "CADJPY=X", "CADCHF=X", "CHFJPY=X"]
y = 0
arr_len = len(tickers)
t1arr = []
for y in range (0, arr_len):
    tix = yf.Ticker(tickers[y])
    df1 = pd.DataFrame(tix.history(period="1mo")).reset_index(drop=True)["Close"]
    df1.name = tickers[y]
    t1arr.append(df1)
    y += 1

# compute the correlation matrix
df = pd.DataFrame(data = t1arr).transpose()

# Print the dataframe
#print("Data Frame")
#print(df)
#print()

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
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=True)
    return au_corr[0:n]

print("Top Correlations")
print(get_top_abs_correlations(df, 3))

# Retrieve the close data for the top 2 pairs
top_pairs = get_top_abs_correlations(df, 3)
group1pair1 = top_pairs.index[0][0]
group1pair2 = top_pairs.index[0][1]

for each in t1arr:
    if each.name == group1pair1:
        pair1 = each
    if each.name == group1pair2:
        pair2 = each
# Confirm correlation is positive or negative
print("Correlation between", group1pair1, "and", group1pair2, "is", pair1.corr(pair2))

# Index price changes to 100 and compare
calcdf1 = pd.DataFrame(pair1.pct_change())
calcdf1['Series'] = 100*np.exp(np.nan_to_num(calcdf1.cumsum()))
df1data = calcdf1['Series']
calcdf2 = pd.DataFrame(pair2.pct_change())
if pair1.corr(pair2) < 0:
    calcdf2 = pd.DataFrame(pair2.pct_change())*-1
    calcdf2['Series'] = 100*np.exp(np.nan_to_num(calcdf2.cumsum()))
else:
    calcdf2 = pd.DataFrame(pair2.pct_change())
    calcdf2['Series'] = 100*np.exp(np.nan_to_num(calcdf2.cumsum()))
df2data = calcdf2['Series']
print(df1data-df2data)