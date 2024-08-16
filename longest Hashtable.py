# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 20:33:26 2023

@author: shade
"""

import pandas as pd 
import time 

df = pd.read_csv("both_covid_data.csv")
df = df.astype(str)


df["joined_row"] = df.apply(lambda row: ''.join(row), axis=1)


start_time = time.perf_counter()


def longestCommonSubsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    index = dp[m][n]
    lcs = [""] * index

    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs[index - 1] = str1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)

end_time = time.perf_counter()
  
print("Time taken for implementing (Longest String Matching algorithm) using Hash Table:",end_time-start_time)