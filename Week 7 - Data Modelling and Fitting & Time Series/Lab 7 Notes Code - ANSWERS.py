# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 12:39:29 2023

@author: User
"""

# Lab 7 Notes - ANSWERS

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Fremont_Bridge_Bicycle_Counter.csv")

print(df.describe())

plt.figure()
plt.plot(df["Fremont Bridge East Sidewalk"], label = "East")
plt.plot(df["Fremont Bridge West Sidewalk"], label = "West", alpha=0.4)
plt.plot(df["Fremont Bridge Total"], label = "Total", alpha=0.2)
plt.legend()
plt.show()

plt.figure()
plt.hist(df["Fremont Bridge Total"], bins=200)
plt.show()

plt.figure()
plt.plot(df["Fremont Bridge Total"].rolling(window=24).mean(), label="Total")
plt.show()

plt.figure()
plt.plot(df["Fremont Bridge Total"].rolling(window=168).mean(), label="Total")
plt.show()

