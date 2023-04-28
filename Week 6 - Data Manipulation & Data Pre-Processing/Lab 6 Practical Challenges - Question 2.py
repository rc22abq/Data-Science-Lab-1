# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 17:57:10 2023

@author: User
"""

# Lab 6 Practical Challenges
# Question 2


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("iris.csv")
columns = ["class", "sepal_length", "sepal_width", "petal_length", "petal_width"]
print(df[columns])


# Histograms
fig = plt.figure()

plt.subplot(2, 2, 1)
plt.hist(df["sepal_length"], bins=15)
plt.title("Histogram of Sepal Length")

plt.subplot(2, 2, 2)
plt.hist(df["sepal_width"], bins=15)
plt.title("Histogram of Sepal Width")

plt.subplot(2, 2, 3)
plt.hist(df["petal_length"], bins=15)
plt.title("Histogram of Petal Length")

plt.subplot(2, 2, 4)
plt.hist(df["petal_width"], bins=15)
plt.title("Histogram of Petal Width")

plt.show()


# Summary Statistics
print("MEAN:")
print("Mean Sepal Length =", round(df["sepal_length"].mean(),2))
print("Mean Sepal Width =", round(df["sepal_width"].mean(),2))
print("Mean Petal Length =", round(df["petal_length"].mean(),2))
print("Mean Petal Width =", round(df["petal_width"].mean(),2))

print("\nMEDIAN:")
print("Median Sepal Length =", round(df["sepal_length"].median(),2))
print("Median Sepal Width =", round(df["sepal_width"].median(),2))
print("Median Petal Length =", round(df["petal_length"].median(),2))
print("Median Petal Width =", round(df["petal_width"].median(),2))

print("\nSUM:")
print("Sum Sepal Length =", round(df["sepal_length"].sum(),2))
print("Sum Sepal Width =", round(df["sepal_width"].sum(),2))
print("Sum Petal Length =", round(df["petal_length"].sum(),2))
print("Sum Petal Width =", round(df["petal_width"].sum(),2))

print("\nSTANDARD DEVIATION:")
print("Standard deviation Sepal Length =", round(df["sepal_length"].std(),2))
print("Standard deviation Sepal Width =", round(df["sepal_width"].std(),2))
print("Standard deviation Petal Length =", round(df["petal_length"].std(),2))
print("Standard deviation Petal Width =", round(df["petal_width"].std(),2))

print("\nVARIANCE:")
print("Variance Sepal Length =", round(df["sepal_length"].var(),2))
print("Variance Sepal Width =", round(df["sepal_width"].var(),2))
print("Variance Petal Length =", round(df["petal_length"].var(),2))
print("Variance Petal Width =", round(df["petal_width"].var(),2))


# Kendall's Tau
# Values range from 1 to -1.
# Values closer to 1 indicate strong agreement.
# Values closer to -1 indicate a strong disagreement.
# res: SignificantResult
# statistic: float (the tau statistic)
# pvalue: float (the p-value for a hypothesis test whose null hypothesis is an absence of association, tau=0)
print("\n\nKENDALL'S TAU:")
print("\nKendall's Tau between Sepal Length and Sepal Width = ", 
      stats.kendalltau(df["sepal_length"], df["sepal_width"], 
                       nan_policy="omit"))
print("\nKendall's Tau between Sepal Length and Petal Length = ", 
      stats.kendalltau(df["sepal_length"], df["petal_length"], 
                       nan_policy="omit"))
print("\nKendall's Tau between Petal Length and Petal Width = ", 
      stats.kendalltau(df["petal_length"], df["petal_width"], 
                       nan_policy="omit"))
print("\nKendall's Tau between Sepal Width and Petal Width = ", 
      stats.kendalltau(df["sepal_width"], df["petal_width"], 
                       nan_policy="omit"))

# KS Test

print("\n\nKS TEST:")
print("\nKS Test between Sepal Length and Sepal Width = ", 
      stats.kstest(df["sepal_length"], df["sepal_width"]))
print("\nKS Test between Sepal Length and Petal Width = ", 
      stats.kstest(df["sepal_length"], df["petal_width"]))
print("\nKS Test between Petal Length and Petal Width = ", 
      stats.kstest(df["petal_length"], df["petal_width"]))
print("\nKS Test between Sepal Width and Petal Width = ", 
      stats.kstest(df["sepal_width"], df["petal_width"]))