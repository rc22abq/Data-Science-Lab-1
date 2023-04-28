# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 11:27:36 2023

@author: User
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


# Loading the CSV file with the needed columns
df = pd.read_csv('covid_cases.csv', usecols=[3, 4, 5, 6, 7, 8, 9])
#print(df)






# NUMBER OF NEW CASES PER DAY


# Selecting the newCasesBySpecimenDate data column
df2 = df[["date", "newCasesBySpecimenDate"]]
#print(df2)


# Plotting
newCasesBySpecimenDate_data = df2.iloc[:, 1:2]
#print(newCasesBySpecimenDate_data)
#date_data = df2.iloc[:, 0:1]
#print(date_data)
newCasesBySpecimenDate_data = np.array(newCasesBySpecimenDate_data)
#print(newCasesBySpecimenDate_data)
newCasesBySpecimenDate_data = newCasesBySpecimenDate_data[:, 0]
#print(newCasesBySpecimenDate_data)
newCasesBySpecimenDate_data_reversed = newCasesBySpecimenDate_data[::-1]
#date_data = np.array(date_data)
#date_data = date_data[:, 0]
#print(date_data)
plt.figure(figsize=(20, 8))
plt.plot(newCasesBySpecimenDate_data_reversed, label="Original Data")
plt.xticks(rotation=40)
# The "Number of Days" axis is measured from the starting date of 30.03.2020
plt.xlabel("Number of Days")
plt.ylabel("Number of cases")
plt.title("Number of COVID-19 Cases per day")
y = newCasesBySpecimenDate_data_reversed
window = 7
average_y = []
for ind in range(len(y) - window + 1):
    average_y.append(np.mean(y[ind:ind+window]))
for ind in range(window - 1):
    average_y.insert(0, np.nan)
plt.plot(average_y, 'r-', label='Running 7-day average')
plt.legend()
plt.show()


# Least square test- LINEAR
x = np.linspace(0.,10,1169)
# Define our model with two parameters
def model_v1(x,m,c):
    return m*x + c
# Use the optimize curve_fit() function to fit. We also supply the estimate of 
# the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
popt, pcov = optimize.curve_fit(model_v1, x, 
                                newCasesBySpecimenDate_data_reversed)
# Plot the ground truth input and the best fit
xs = np.linspace(0,10,1169)
plt.plot(x, newCasesBySpecimenDate_data_reversed, linestyle="solid", 
          label="Ground truth")
plt.plot(xs, model_v1(xs, *popt), linestyle="dashed", label="Best fit")
plt.title("Least squares - LINEAR.")
plt.xlabel("Number of Days")
plt.ylabel("Number of Cases")
plt.legend(loc="upper left")
plt.show()
print("POPT =", popt)
print("PCOV =", np.diag(pcov)**0.5)



# Least square test - QUADRATIC
x = np.linspace(0.,10,1169)
# Define our model with two parameters
def model_v2(x,a,b,c):
    return a*x**2 + b*x + c
# Use the optimize curve_fit() function to fit. We also supply the estimate of 
# the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
popt, pcov = optimize.curve_fit(model_v2, x, 
                                newCasesBySpecimenDate_data_reversed)
# Plot the ground truth input and the best fit
xs = np.linspace(0,10,1169)
plt.plot(x, newCasesBySpecimenDate_data_reversed, linestyle="solid", 
          label="Ground truth")
plt.plot(xs, model_v2(xs, *popt), linestyle="dashed", label="Best fit")
plt.title("Least squares - QUADRATIC.")
plt.xlabel("Number of Days")
plt.ylabel("Number of Cases")
plt.legend(loc="upper left")
plt.show()
print("POPT =", popt)
print("PCOV =", np.diag(pcov)**0.5)



# Least square test - CUBIC
x = np.linspace(0.,10,1169)
# Define our model with two parameters
def model_v3(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d
# Use the optimize curve_fit() function to fit. We also supply the estimate of 
# the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
popt, pcov = optimize.curve_fit(model_v3, x, 
                                newCasesBySpecimenDate_data_reversed)
# Plot the ground truth input and the best fit
xs = np.linspace(0,10,1169)
plt.plot(x, newCasesBySpecimenDate_data_reversed, linestyle="solid", 
          label="Ground truth")
plt.plot(xs, model_v3(xs, *popt), linestyle="dashed", label="Best fit")
plt.title("Least squares - CUBIC.")
plt.xlabel("Number of Days")
plt.ylabel("Number of Cases")
plt.legend(loc="upper left")
plt.show()
print("POPT =", popt)
print("PCOV =", np.diag(pcov)**0.5)



# Least square test - QUARTIC
x = np.linspace(0.,10,1169)
# Define our model with two parameters
def model_v4(x,a,b,c,d,e):
    return a*x**4 + b*x**3 + c*x**2 + d*x + e
# Use the optimize curve_fit() function to fit. We also supply the estimate of 
# the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
popt, pcov = optimize.curve_fit(model_v4, x, 
                                newCasesBySpecimenDate_data_reversed)
# Plot the ground truth input and the best fit
xs = np.linspace(0,10,1169)
plt.plot(x, newCasesBySpecimenDate_data_reversed, linestyle="solid", 
          label="Ground truth")
plt.plot(xs, model_v4(xs, *popt), linestyle="dashed", label="Best fit")
plt.title("Least squares - QUARTIC.")
plt.xlabel("Number of Days")
plt.ylabel("Number of Cases")
plt.legend(loc="upper left")
plt.show()
print("POPT =", popt)
print("PCOV =", np.diag(pcov)**0.5)



# Least square test - QUINTIC
x = np.linspace(0.,10,1169)
# Define our model with two parameters
def model_v5(x,a,b,c,d,e,f):
    return a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
# Use the optimize curve_fit() function to fit. We also supply the estimate of 
# the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
popt, pcov = optimize.curve_fit(model_v5, x, 
                                newCasesBySpecimenDate_data_reversed)
# Plot the ground truth input and the best fit
xs = np.linspace(0,10,1169)
plt.plot(x, newCasesBySpecimenDate_data_reversed, linestyle="solid", 
          label="Ground truth")
plt.plot(xs, model_v5(xs, *popt), linestyle="dashed", label="Best fit")
plt.title("Least squares - QUINTIC.")
plt.xlabel("Number of Days")
plt.ylabel("Number of Cases")
plt.legend(loc="upper left")
plt.show()
print("POPT =", popt)
print("PCOV =", np.diag(pcov)**0.5)



# # Least square test - SEXTIC
# x = np.linspace(0.,10,1169)
# # Define our model with two parameters
# def model_v6(x,a,b,c,d,e,f,g):
#     return a*x**6 + b*x**5 + c*x**4 + d*x**3 + e*x**2 + f*x + g
# # Use the optimize curve_fit() function to fit. We also supply the estimate of 
# # the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
# popt, pcov = optimize.curve_fit(model_v6, x, 
#                                 newCasesBySpecimenDate_data_reversed)
# # Plot the ground truth input and the best fit
# xs = np.linspace(0,10,1169)
# plt.plot(x, newCasesBySpecimenDate_data_reversed, linestyle="solid", 
#           label="Ground truth")
# plt.plot(xs, model_v6(xs, *popt), linestyle="dashed", label="Best fit")
# plt.title("Least squares - SEXTIC.")
# plt.xlabel("Number of Days")
# plt.ylabel("Number of Cases")
# plt.legend(loc="upper left")
# plt.show()
# print("POPT =", popt)
# print("PCOV =", np.diag(pcov)**0.5)



# # Least square test - SEPTIC
# x = np.linspace(0.,10,1169)
# # Define our model with two parameters
# def model_v7(x,a,b,c,d,e,f,g,h):
#     return a*x**7 + b*x**6 + c*x**5 + d*x**4 + e*x**3 + f*x**2 + g*x + h
# # Use the optimize curve_fit() function to fit. We also supply the estimate of 
# # the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
# popt, pcov = optimize.curve_fit(model_v7, x, 
#                                 newCasesBySpecimenDate_data_reversed)
# # Plot the ground truth input and the best fit
# xs = np.linspace(0,10,1169)
# plt.plot(x, newCasesBySpecimenDate_data_reversed, linestyle="solid", 
#           label="Ground truth")
# plt.plot(xs, model_v7(xs, *popt), linestyle="dashed", label="Best fit")
# plt.title("Least squares - SEPTIC.")
# plt.xlabel("Number of Days")
# plt.ylabel("Number of Cases")
# plt.legend(loc="upper left")
# plt.show()
# print("POPT =", popt)
# print("PCOV =", np.diag(pcov)**0.5)



# # Least square test - OCTIC
# x = np.linspace(0.,10,1169)
# # Define our model with two parameters
# def model_v8(x,a,b,c,d,e,f,g,h,i):
#     return a*x**8 + b*x**7 + c*x**6 + d*x**5 + e*x**4 + f*x**3 + g*x**2 + h*x + i
# # Use the optimize curve_fit() function to fit. We also supply the estimate of 
# # the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
# popt, pcov = optimize.curve_fit(model_v8, x, 
#                                 newCasesBySpecimenDate_data_reversed)
# # Plot the ground truth input and the best fit
# xs = np.linspace(0,10,1169)
# plt.plot(x, newCasesBySpecimenDate_data_reversed, linestyle="solid", 
#           label="Ground truth")
# plt.plot(xs, model_v8(xs, *popt), linestyle="dashed", label="Best fit")
# plt.title("Least squares - OCTIC.")
# plt.xlabel("Number of Days")
# plt.ylabel("Number of Cases")
# plt.legend(loc="upper left")
# plt.show()
# print("POPT =", popt)
# print("PCOV =", np.diag(pcov)**0.5)



# # Least square test - NONIC
# x = np.linspace(0.,10,1169)
# # Define our model with two parameters
# def model_v9(x,a,b,c,d,e,f,g,h,i,j):
#     return a*x**9 + b*x**8 + c*x**7 + d*x**6 + e*x**5 + f*x**4 + g*x**3 + h*x**2 + i*x + j
# # Use the optimize curve_fit() function to fit. We also supply the estimate of 
# # the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
# popt, pcov = optimize.curve_fit(model_v9, x, 
#                                 newCasesBySpecimenDate_data_reversed)
# # Plot the ground truth input and the best fit
# xs = np.linspace(0,10,1169)
# plt.plot(x, newCasesBySpecimenDate_data_reversed, linestyle="solid", 
#           label="Ground truth")
# plt.plot(xs, model_v9(xs, *popt), linestyle="dashed", label="Best fit")
# plt.title("Least squares - NONIC.")
# plt.xlabel("Number of Days")
# plt.ylabel("Number of Cases")
# plt.legend(loc="upper left")
# plt.show()
# print("POPT =", popt)
# print("PCOV =", np.diag(pcov)**0.5)



# # Least square test - DECIC
# x = np.linspace(0.,10,1169)
# # Define our model with two parameters
# def model_v10(x,a,b,c,d,e,f,g,h,i,j,k):
#     return a*x**10 + b*x**9 + c*x**8 + d*x**7 + e*x**6 + f*x**5 + g*x**4 + h*x**3 + i*x**2 + j*x + k
# # Use the optimize curve_fit() function to fit. We also supply the estimate of 
# # the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
# popt, pcov = optimize.curve_fit(model_v10, x, 
#                                 newCasesBySpecimenDate_data_reversed)
# # Plot the ground truth input and the best fit
# xs = np.linspace(0,10,1169)
# plt.plot(x, newCasesBySpecimenDate_data_reversed, linestyle="solid", 
#           label="Ground truth")
# plt.plot(xs, model_v10(xs, *popt), linestyle="dashed", label="Best fit")
# plt.title("Least squares - DECIC.")
# plt.xlabel("Number of Days")
# plt.ylabel("Number of Cases")
# plt.legend(loc="upper left")
# plt.show()
# print("POPT =", popt)
# print("PCOV =", np.diag(pcov)**0.5)



# Least square test between days 650-715 - LINEAR
newCasesBySpecimenDate_data_v1 = newCasesBySpecimenDate_data_reversed[650:715]
#print(newCasesBySpecimenDate_data_v1)
x = np.linspace(0.,10,65)
# Define our model with two parameters
def model_v1(x,m,c):
    return m*x + c
# Use the optimize curve_fit() function to fit. We also supply the estimate of 
# the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
popt, pcov = optimize.curve_fit(model_v1, x, newCasesBySpecimenDate_data_v1)
# Plot the ground truth input and the best fit
xs = np.linspace(0,10,65)
plt.plot(x, newCasesBySpecimenDate_data_v1, linestyle="solid", 
          label="Ground truth")
plt.plot(xs, model_v1(xs, *popt), linestyle="dashed", label="Best fit")
plt.title("Least squares on data between days 650-715 - LINEAR.")
plt.xlabel("Number of Days")
plt.ylabel("Number of Cases")
plt.legend(loc="upper left")
plt.show()
print("POPT =", popt)
print("PCOV =", np.diag(pcov)**0.5)



# Least square test between days 650-715 - QUADRATIC
newCasesBySpecimenDate_data_v1 = newCasesBySpecimenDate_data_reversed[650:715]
#print(newCasesBySpecimenDate_data_v1)
x = np.linspace(0.,10,65)
# Define our model with two parameters
def model_v2(x,a,b,c):
    return a*x**2 + b*x + c
# Use the optimize curve_fit() function to fit. We also supply the estimate of 
# the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
popt, pcov = optimize.curve_fit(model_v2, x, newCasesBySpecimenDate_data_v1)
# Plot the ground truth input and the best fit
xs = np.linspace(0,10,65)
plt.plot(x, newCasesBySpecimenDate_data_v1, linestyle="solid", 
          label="Ground truth")
plt.plot(xs, model_v2(xs, *popt), linestyle="dashed", label="Best fit")
plt.title("Least squares on data between days 650-715 - QUADRATIC.")
plt.xlabel("Number of Days")
plt.ylabel("Number of Cases")
plt.legend(loc="upper left")
plt.show()
print("POPT =", popt)
print("PCOV =", np.diag(pcov)**0.5)



# Least square test between days 650-715 - CUBIC
newCasesBySpecimenDate_data_v1 = newCasesBySpecimenDate_data_reversed[650:715]
#print(newCasesBySpecimenDate_data_v1)
x = np.linspace(0.,10,65)
# Define our model with two parameters
def model_v3(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d
# Use the optimize curve_fit() function to fit. We also supply the estimate of 
# the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
popt, pcov = optimize.curve_fit(model_v3, x, newCasesBySpecimenDate_data_v1)
# Plot the ground truth input and the best fit
xs = np.linspace(0,10,65)
plt.plot(x, newCasesBySpecimenDate_data_v1, linestyle="solid", 
          label="Ground truth")
plt.plot(xs, model_v3(xs, *popt), linestyle="dashed", label="Best fit")
plt.title("Least squares on data between days 650-715 - CUBIC.")
plt.xlabel("Number of Days")
plt.ylabel("Number of Cases")
plt.legend(loc="upper left")
plt.show()
print("POPT =", popt)
print("PCOV =", np.diag(pcov)**0.5)



# Least square test between days 650-715 - QUARTIC
newCasesBySpecimenDate_data_v1 = newCasesBySpecimenDate_data_reversed[650:715]
#print(newCasesBySpecimenDate_data_v1)
x = np.linspace(0.,10,65)
# Define our model with two parameters
def model_v4(x,a,b,c,d,e):
    return a*x**4 + b*x**3 + c*x**2 + d*x + e
# Use the optimize curve_fit() function to fit. We also supply the estimate of 
# the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
popt, pcov = optimize.curve_fit(model_v4, x, newCasesBySpecimenDate_data_v1)
# Plot the ground truth input and the best fit
xs = np.linspace(0,10,65)
plt.plot(x, newCasesBySpecimenDate_data_v1, linestyle="solid", 
          label="Ground truth")
plt.plot(xs, model_v4(xs, *popt), linestyle="dashed", label="Best fit")
plt.title("Least squares on data between days 650-715 - QUARTIC.")
plt.xlabel("Number of Days")
plt.ylabel("Number of Cases")
plt.legend(loc="upper left")
plt.show()
print("POPT 8888888888888888888888888888=", popt)
print("PCOV 888888888888888888888888888=", np.diag(pcov)**0.5)



# Least square test between days 650-715 - QUINTIC
newCasesBySpecimenDate_data_v1 = newCasesBySpecimenDate_data_reversed[650:715]
#print(newCasesBySpecimenDate_data_v1)
x = np.linspace(0.,10,65)
# Define our model with two parameters
def model_v5(x,a,b,c,d,e,f):
    return a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
# Use the optimize curve_fit() function to fit. We also supply the estimate of 
# the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
popt, pcov = optimize.curve_fit(model_v5, x, newCasesBySpecimenDate_data_v1)
# Plot the ground truth input and the best fit
xs = np.linspace(0,10,65)
plt.plot(x, newCasesBySpecimenDate_data_v1, linestyle="solid", 
          label="Ground truth")
plt.plot(xs, model_v5(xs, *popt), linestyle="dashed", label="Best fit")
plt.title("Least squares on data between days 650-715 - QUINTIC.")
plt.xlabel("Number of Days")
plt.ylabel("Number of Cases")
plt.legend(loc="upper left")
plt.show()
print("POPT =", popt)
print("PCOV =", np.diag(pcov)**0.5)



# # Least square test between days 650-715 - SEXTIC
# newCasesBySpecimenDate_data_v1 = newCasesBySpecimenDate_data_reversed[650:715]
# #print(newCasesBySpecimenDate_data_v1)
# x = np.linspace(0.,10,65)
# # Define our model with two parameters
# def model_v6(x,a,b,c,d,e,f,g):
#     return a*x**6 + b*x**5 + c*x**4 + d*x**3 + e*x**2 + f*x + g
# # Use the optimize curve_fit() function to fit. We also supply the estimate of 
# # the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
# popt, pcov = optimize.curve_fit(model_v6, x, newCasesBySpecimenDate_data_v1)
# # Plot the ground truth input and the best fit
# xs = np.linspace(0,10,65)
# plt.plot(x, newCasesBySpecimenDate_data_v1, linestyle="solid", 
#           label="Ground truth")
# plt.plot(xs, model_v6(xs, *popt), linestyle="dashed", label="Best fit")
# plt.title("Least squares on data between days 650-715 - SEXTIC.")
# plt.xlabel("Number of Days")
# plt.ylabel("Number of Cases")
# plt.legend(loc="upper left")
# plt.show()
# print("POPT =", popt)
# print("PCOV =", np.diag(pcov)**0.5)



# # Least square test between days 650-715 - SEPTIC
# newCasesBySpecimenDate_data_v1 = newCasesBySpecimenDate_data_reversed[650:715]
# #print(newCasesBySpecimenDate_data_v1)
# x = np.linspace(0.,10,65)
# # Define our model with two parameters
# def model_v7(x,a,b,c,d,e,f,g,h):
#     return a*x**7 + b*x**6 + c*x**5 + d*x**4 + e*x**3 + f*x**2 + g*x + h
# # Use the optimize curve_fit() function to fit. We also supply the estimate of 
# # the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
# popt, pcov = optimize.curve_fit(model_v7, x, newCasesBySpecimenDate_data_v1)
# # Plot the ground truth input and the best fit
# xs = np.linspace(0,10,65)
# plt.plot(x, newCasesBySpecimenDate_data_v1, linestyle="solid", 
#           label="Ground truth")
# plt.plot(xs, model_v7(xs, *popt), linestyle="dashed", label="Best fit")
# plt.title("Least squares on data between days 650-715 - SEPTIC.")
# plt.xlabel("Number of Days")
# plt.ylabel("Number of Cases")
# plt.legend(loc="upper left")
# plt.show()
# print("POPT =", popt)
# print("PCOV =", np.diag(pcov)**0.5)



# # Least square test between days 650-715 - OCTIC
# newCasesBySpecimenDate_data_v1 = newCasesBySpecimenDate_data_reversed[650:715]
# #print(newCasesBySpecimenDate_data_v1)
# x = np.linspace(0.,10,65)
# # Define our model with two parameters
# def model_v8(x,a,b,c,d,e,f,g,h,i):
#     return a*x**8 + b*x**7 + c*x**6 + d*x**5 + e*x**4 + f*x**3 + g*x**2 + h*x + i
# # Use the optimize curve_fit() function to fit. We also supply the estimate of 
# # the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
# popt, pcov = optimize.curve_fit(model_v8, x, newCasesBySpecimenDate_data_v1)
# # Plot the ground truth input and the best fit
# xs = np.linspace(0,10,65)
# plt.plot(x, newCasesBySpecimenDate_data_v1, linestyle="solid", 
#           label="Ground truth")
# plt.plot(xs, model_v8(xs, *popt), linestyle="dashed", label="Best fit")
# plt.title("Least squares on data between days 650-715 - OCTIC.")
# plt.xlabel("Number of Days")
# plt.ylabel("Number of Cases")
# plt.legend(loc="upper left")
# plt.show()
# print("POPT =", popt)
# print("PCOV =", np.diag(pcov)**0.5)



# # Least square test between days 650-715 - NONIC
# newCasesBySpecimenDate_data_v1 = newCasesBySpecimenDate_data_reversed[650:715]
# #print(newCasesBySpecimenDate_data_v1)
# x = np.linspace(0.,10,65)
# # Define our model with two parameters
# def model_v9(x,a,b,c,d,e,f,g,h,i,j):
#     return a*x**9 + b*x**8 + c*x**7 + d*x**6 + e*x**5 + f*x**4 + g*x**3 + h*x**2 + i*x + j
# # Use the optimize curve_fit() function to fit. We also supply the estimate of 
# # the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
# popt, pcov = optimize.curve_fit(model_v9, x, newCasesBySpecimenDate_data_v1)
# # Plot the ground truth input and the best fit
# xs = np.linspace(0,10,65)
# plt.plot(x, newCasesBySpecimenDate_data_v1, linestyle="solid", 
#           label="Ground truth")
# plt.plot(xs, model_v9(xs, *popt), linestyle="dashed", label="Best fit")
# plt.title("Least squares on data between days 650-715 - NONIC.")
# plt.xlabel("Number of Days")
# plt.ylabel("Number of Cases")
# plt.legend(loc="upper left")
# plt.show()
# print("POPT =", popt)
# print("PCOV =", np.diag(pcov)**0.5)



# # Least square test between days 650-715 - DECIC
# newCasesBySpecimenDate_data_v1 = newCasesBySpecimenDate_data_reversed[650:715]
# #print(newCasesBySpecimenDate_data_v1)
# x = np.linspace(0.,10,65)
# # Define our model with two parameters
# def model_v10(x,a,b,c,d,e,f,g,h,i,j,k):
#     return a*x**10 + b*x**9 + c*x**8 + d*x**7 + e*x**6 + f*x**5 + g*x**4 + h*x**3 + i*x**2 + j*x + k
# # Use the optimize curve_fit() function to fit. We also supply the estimate of 
# # the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
# popt, pcov = optimize.curve_fit(model_v10, x, newCasesBySpecimenDate_data_v1)
# # Plot the ground truth input and the best fit
# xs = np.linspace(0,10,65)
# plt.plot(x, newCasesBySpecimenDate_data_v1, linestyle="solid", 
#           label="Ground truth")
# plt.plot(xs, model_v10(xs, *popt), linestyle="dashed", label="Best fit")
# plt.title("Least squares on data between days 650-715 - DECIC.")
# plt.xlabel("Number of Days")
# plt.ylabel("Number of Cases")
# plt.legend(loc="upper left")
# plt.show()
# print("POPT =", popt)
# print("PCOV =", np.diag(pcov)**0.5)



# Least square test between days 650-715 - EXPONENTIAL
newCasesBySpecimenDate_data_v2 = newCasesBySpecimenDate_data_reversed[650:715]
x = np.linspace(0.,10,65)
# Define our model with two parameters
def model_v11(x,l,m):
    return l*np.exp(m*x)
# Use the optimize curve_fit() function to fit. We also supply the estimate of 
# the uncertainty on each point. Our first guess of the parameters is m=0, c=0.
popt, pcov = optimize.curve_fit(model_v11, x, newCasesBySpecimenDate_data_v2)
# Plot the ground truth input and the best fit
xs = np.linspace(0,10,65)
plt.plot(x, newCasesBySpecimenDate_data_v2, linestyle="solid", 
          label="Ground truth")
plt.plot(xs, model_v11(xs, *popt), linestyle="dashed", label="Best fit")
plt.title("Least squares on data between days 650-715 - EXPONENTIAL.")
plt.xlabel("Number of Days")
plt.ylabel("Number of Cases")
plt.legend(loc="upper left")
plt.show()
print("POPT =", popt)
print("PCOV =", np.diag(pcov)**0.5)