#!/usr/bin/env python3

# from pandas import *
import pandas as pd
import numpy as np


df = pd.read_excel("TLV22_7_23.xlsx")
# df.iloc[0:3 ,1] # get the second column first 3 rows

# First process
df["relative_diff"] = pd.Series(
    [(y - x) / x for x, y in zip(df["מדד נעילה"], df["מדד נעילה"][1:])]
)
# print(df['relative_diff']) # works !!

df["relative_rank_frac"] = df["relative_diff"].rank() / df["relative_diff"].count()
# print(df['relative_rank_frac']) # works !

k = 5
df["multiple"] = (df["relative_rank_frac"] * k).apply(np.floor) + 1
# print(df['multiple']) # works but missing MOD func

count = len(df[(df["multiple"] == 1) & (df["multiple"].shift(-1) == 1)])
# count = len(df[(df['multiple'] == 1)])
# print(count) # Output: 1
helper_mat = [
    [
        len(df[(df["multiple"] == i) & (df["multiple"].shift(-1) == j)])
        for j in range(1, 6)
    ]
    for i in range(1, 6)
]
# print(helper_mat[0][1]) #works!!
final_mat = [
    [helper_mat[i][j] / sum(helper_mat[i]) for j in range(5)] for i in range(5)
]
# print(final_mat[1][0]) # works !!
# print(final_mat)
for arr in final_mat:
    for elem in arr:
        print(elem, " ", end="")
    print("\n")
