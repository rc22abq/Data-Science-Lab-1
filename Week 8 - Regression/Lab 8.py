# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:13:00 2023

@author: User
"""

# Lab 8 notes: Regression

import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")
import numpy as np


# 8.1 Linear Regression
rng = np.random.RandomState(1)
x = 10*rng.rand(50)
y = (-1) * x + 2 + rng.randn(50)
plt.scatter(x, y)

from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
model.fit(x[:, np.newaxis], y)
xfit = np.linspace(0, 10, 1000)
yfit = model.predict(xfit[:, np.newaxis])
plt.scatter(x, y)
plt.plot(xfit, yfit)
print("Model slope:", model.coef_[0])
print("Model intercept:", model.intercept_)

rng = np.random.RandomState(1)
X = 10 * rng.rand(100, 3)
y = 0.5 * np.dot(X, [1.5, -2., 1.])
model.fit(x, y)
print(model.intercept_)
print(model.coef)


# 8.2 Polynomial Function Regresion
from sklearn.preprocessing import PolynomialFeatures
x = np.array([2, 3, 4])
poly = PolynomialFeatures(3, include_bias=False)
poly.fit_transform(x[:, None])

from sklearn.pipeline import make_pipeline
poly_model = make_pipeline(PolynomialFeatures(7), LinearRegression())
rng = np.random.RandomState(1)
x = 10 * rng.rand(50)
y = np.sin(x) + 0.1 * rng.randn(50)
poly_model.fit(x[:, np.newaxis], y)
yfit = poly_model.predict(xfit[:, np.newaxis])
plt.scatter(x, y)
plt.plot(xfit, yfit)