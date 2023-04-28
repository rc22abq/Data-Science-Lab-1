# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 12:16:09 2023

@author: User
"""

# Lab 6 Practical Challenges
# Question 1


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("listings.csv")
columns = ["price", "availability_365"]
print(df[columns])

# Histogram
print("Max price = £", np.max(df["price"]))
plt.figure()
plt.hist(df["price"], bins=1000)
plt.xlim(0,1500)
plt.show()

# Summary Statistics
print("Mean price = £", round(df["price"].mean(),2))
print("Median price = £", df["price"].median())
print("Sum of prices = £", df["price"].sum())
print("Standard deviation of price = £", round(df["price"].std(),2))
print("99th percentile of price = £", round(np.percentile(df["price"],99.99),2))

# Kendall's Tau
# Values range from 1 to -1.
# Values closer to 1 indicate strong agreement.
# Values closer to -1 indicate a strong disagreement.
# res: SignificantResult
# statistic: float (the tau statistic)
# pvalue: float (the p-value for a hypothesis test whose null hypothesis is an absence of association, tau=0)
print("Kendall's Tau between price and availability = ", 
      stats.kendalltau(df["price"], df["availability_365"],
      nan_policy="omit"))