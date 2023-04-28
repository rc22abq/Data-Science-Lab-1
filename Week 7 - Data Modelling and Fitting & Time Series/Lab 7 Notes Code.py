# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 12:20:50 2023

@author: User
"""

# Lab 7 Notes

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Fremont_Bridge_Bicycle_Counter.csv")
columns = ["Date", "Fremont Bridge Total",
           "Fremont Bridge East Sidewalk",
           "Fremont Bridge West Sidewalk"]
print(df[columns])

# Summary Statistics
print("\n\nSUMMARY STATISTICS:")
print(df["Fremont Bridge Total"].describe())

# Plotting
plt.figure()
plt.plot(df["Fremont Bridge Total"])
plt.title("Plot of number of bicycles crossing the Fremont Bridge")
plt.show()

# Finding the rolling mean of previous 24 hours
plt.figure()
plt.plot(df["Fremont Bridge Total"].rolling(24).mean())
plt.title("Rolling Mean of the previous 24 hours")
plt.show()

# Finding the rolling mean of previous week (168 hours)
plt.figure()
plt.plot(df["Fremont Bridge Total"].rolling(168).mean())
plt.title("Rolling Mean of the previous week")
plt.show()




