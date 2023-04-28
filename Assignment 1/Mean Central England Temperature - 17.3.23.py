# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:41:49 2023

@author: User
"""

import requests
import numpy as np
import calendar
import statistics as stat
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import median_abs_deviation
from scipy import stats


# Define URL.
data = 'https://www.metoffice.gov.uk/hadobs/hadcet/data/meantemp_monthly_totals.txt'

# Use requests.
r = requests.get(data)

# Get the text.
data2 = r.text

# Split it into lines based on newline character.
lines = data2.split("\n")

# Lists to store months with highest temperatures, and the temperature itself
max_temp_month = []
max_temp_temp = []
min_temp_month = []
min_temp_temp = []



# MAXIMUMS
# Loop over lines - starting at index 4
# since there are 4 header lines to ignore
for line in lines[5:-2]:        # -1 as latest year has incomplete data for 2023
    # Split it into a list where the separator is any whitespace
    line_new = line.split()
    # Our list will be full of strings. We need to convert these into floats.
    line_new_float = [float(i) for i in line_new[1:13]]
    # Find the max temperature
    max_temp = max(line_new_float)
    # Find the month in which the max temperature is achieved
    index_max = line_new_float.index(max_temp)
    # Change number into month, accounting for the indexing
    month_max = calendar.month_name[index_max+1]
    # Add this month to the list of months with highest temperatures
    max_temp_month.append(month_max)
    max_temp_temp.append(max_temp)



# MINIMUMS
# Loop over lines - starting at index 4
# since there are 4 header lines to ignore
for line in lines[5:-2]:        # -1 as latest year has incomplete data for 2023
    # Split it into a list where the separator is any whitespace
    line_new = line.split()
    # Our list will be full of strings. We need to convert these into floats.
    line_new_float = [float(i) for i in line_new[1:13]]
    # Find the max temperature
    min_temp = min(line_new_float)
    # Find the month in which the max temperature is achieved
    index_min = line_new_float.index(min_temp)
    # Change number into month, accounting for the indexing
    month_min = calendar.month_name[index_min+1]
    # Add this month to the list of months with highest temperatures
    min_temp_month.append(month_min)
    min_temp_temp.append(min_temp)
    
    
    
# Now let's summarise what we have found    
#print("The months with the highest temperature are given as follows:\n\n",
      #max_temp_month)
#print("\nand the maximum temperatures respectively are:\n\n",max_temp_temp,
      #"degrees celsuis.")
print("\nThe most common month with highest temperature is",
      stat.mode(max_temp_month), ".")
print("The average temperature in", stat.mode(max_temp_month),
      "was", round((stat.mean(max_temp_temp)),1), "(\u00B0C).")
#print("The months with the lowest temperature are given as follows:\n\n",
      #min_temp_month)
#print("\nand the minimum temperatures respectively are:\n\n",min_temp_temp,
      #"degrees celsuis.")
print("\nThe most common month with lowest temperature is",
      stat.mode(min_temp_month), ".")
print("The average temperature in", stat.mode(min_temp_month),
      "was", round((stat.mean(min_temp_temp)),1), "(\u00B0C).")



# Finally, we print out the hottest & coldest month/year ever
hottest_temp = max(max_temp_temp)
hottest_month = max_temp_month[max_temp_temp.index(hottest_temp)]
hottest_year = 1659+max_temp_temp.index(hottest_temp)
print("\nThe hottest temperature recorded was", hottest_temp,
      "(\u00B0C) recorded in", hottest_month, hottest_year,".")
coldest_temp = min(min_temp_temp)
coldest_month = min_temp_month[min_temp_temp.index(coldest_temp)]
coldest_year = 1659+min_temp_temp.index(coldest_temp)
print("\nThe coldest temperature recorded was", coldest_temp,
      "(\u00B0C) recorded in", coldest_month, coldest_year,".")



# Scatter graph for the max temp for each month
x_max = np.linspace(0, 20, 364)
y_max = max_temp_temp
window = 28
average_y = []
for ind in range(len(y_max) - window + 1):
    average_y.append(np.mean(y_max[ind:ind+window]))
for ind in range(window - 1):
    average_y.insert(0, np.nan)
plt.figure()    
plt.plot(x_max, y_max, "k-", label="Original Data")
plt.plot(x_max, average_y, "r-", label="Four Year Running Average")
plt.title("Maximum Temperature per Year from 1659 to 2022.", 
          weight="bold")
plt.xlabel("Time")
plt.ylabel("Temperature (\u00B0C)")
z_max = np.polyfit(x_max, y_max, 1)
p_max = np.poly1d(z_max)
plt.plot(x_max, p_max(x_max), "b-", label="Trend Line")
plt.legend()
plt.show()



# Scatter graph for the min temp for each month
x_min = np.linspace(0, 20, 364)
y_min = min_temp_temp
window = 28
average_y = []
for ind in range(len(y_min) - window + 1):
    average_y.append(np.mean(y_min[ind:ind+window]))
for ind in range(window - 1):
    average_y.insert(0, np.nan)
plt.figure()    
plt.plot(x_min, y_min, "k-", label="Original Data")
plt.plot(x_min, average_y, "r-", label="Four Year Running Average")
plt.title("Minimum Temperature per Year from 1659 to 2022.", 
          weight="bold")
plt.xlabel("Time")
plt.ylabel("Temperature (\u00B0C)")
z_min = np.polyfit(x_min, y_min, 1)
p_min = np.poly1d(z_min)
plt.plot(x_min, p_min(x_min), "b-", label="Trend Line")
plt.legend()
plt.show()



# Histogram for the max temp for each month
max_temp_temp_mean = np.mean(max_temp_temp)
max_temp_temp_std = np.std(max_temp_temp)
max_temp_temp_median = stat.median(max_temp_temp)

plt.figure()
plt.hist(max_temp_temp, density=True)
plt.xlabel("Maximum Temperatures per Year")
plt.ylabel("Frequency Density")
plt.title("Histogram of the Maximum Temperatures per Year from 1659 to 2022.",
          weight="bold")
x = np.linspace(np.min(max_temp_temp), np.max(max_temp_temp))
plt.plot(x, norm.pdf(x, max_temp_temp_mean, max_temp_temp_std), linewidth=2)
plt.axvline(max_temp_temp_mean, color="k", linestyle="dashed", 
            linewidth=2, label="Mean = {:.1f}".format(max_temp_temp_mean))
max_min_ylim, max_max_ylim = plt.ylim()
plt.axvline(max_temp_temp_median, color="red", linestyle="dashed", 
            linewidth=2, label="Median = {:.1f}".format(max_temp_temp_median))
min_ylim, max_ylim = plt.ylim()
plt.legend()
plt.show()



# Histogram for the min temp for each month
min_temp_temp_mean = np.mean(min_temp_temp)
min_temp_temp_std = np.std(min_temp_temp)
min_temp_temp_median = stat.median(min_temp_temp)

plt.figure()
plt.hist(min_temp_temp, density=True)
plt.xlabel("Minimum Temperatures per Year")
plt.ylabel("Frequency Density")
plt.title("Histogram of the Minimum Temperatures per Year from 1659 to 2022.",
          weight="bold")
x = np.linspace(np.min(min_temp_temp), np.max(min_temp_temp))
plt.plot(x, norm.pdf(x, min_temp_temp_mean, min_temp_temp_std), linewidth=2)
plt.axvline(min_temp_temp_mean, color="k", linestyle="dashed", 
            linewidth=2, label="Mean = {:.1f}".format(min_temp_temp_mean))
min_min_ylim, min_max_ylim = plt.ylim()
plt.axvline(min_temp_temp_median, color="red", linestyle="dashed", 
            linewidth=2, label="Median = {:.1f}".format(min_temp_temp_median))
min_ylim, max_ylim = plt.ylim()
plt.legend()
plt.show()



# Summary Statistics
print("\n\n\nSUMMARY STATISTICS:")

print("\nMaximum Temperatures:")
print("Arithmetic mean = {:0.3f} (\u00B0C).".format(max_temp_temp_mean)) 
print("Standard deviation = {:0.3f} (\u00B0C).".format(max_temp_temp_std))
print("Variance = {:0.3f} (\u00B0C).".format(max_temp_temp_std**2))
max_midrange = max(max_temp_temp) - min(max_temp_temp)
print("Midrange = {:.3f} (\u00B0C).".format(max_midrange))
print("Median = {:.3f} (\u00B0C).".format(stat.median(max_temp_temp)))
print("25th percentile = {:.3f} (\u00B0C).".format(np.percentile(max_temp_temp, 25)))
print("75th percentile = {:.3f} (\u00B0C).".format(np.percentile(max_temp_temp, 75)))
print("Interquartile Range (IQR) = {:.3f} (\u00B0C).".format(np.percentile(max_temp_temp, 75) - np.percentile(max_temp_temp, 25)))
def max_aad(max_temp_temp, axis=None):
    return np.mean(np.absolute(max_temp_temp - np.mean(max_temp_temp, axis)), axis)
print("Absolute average deviation (AAD) = {:.3f} (\u00B0C).".format(max_aad(max_temp_temp)))
mad_max_temp_temp = median_abs_deviation(max_temp_temp)
print("Median abosolute deviation (MAD) = {:.3f} (\u00B0C).".format(mad_max_temp_temp))
max_cov_matrix = np.cov(max_temp_temp, bias=True)
print("Covariance matrix = {:.3f}.".format(max_cov_matrix))
print("Skewness = {:.3f}.".format(stats.skew(max_temp_temp)))
print("Kurtosis = {:.3f}.".format(stats.kurtosis(max_temp_temp)))

print("\nMinimum Temperatures:")
print("Arithmetic mean = {:0.3f} (\u00B0C).".format(min_temp_temp_mean)) 
print("Standard deviation = {:0.3f} (\u00B0C).".format(min_temp_temp_std))
print("Variance = {:0.3f} (\u00B0C).".format(min_temp_temp_std**2))
min_midrange = max(min_temp_temp) - min(min_temp_temp)
min_midrange = max(min_temp_temp) - min(min_temp_temp)
print("Midrange = {:.3f} (\u00B0C).".format(min_midrange))
print("Median = {:.3f} (\u00B0C).".format(stat.median(min_temp_temp)))
print("25th percentile = {:.3f} (\u00B0C).".format(np.percentile(min_temp_temp, 25)))
print("75th percentile = {:.3f} (\u00B0C).".format(np.percentile(min_temp_temp, 75)))
print("Interquartile Range (IQR) = {:.3f} (\u00B0C).".format(np.percentile(min_temp_temp, 75) - np.percentile(min_temp_temp, 25)))
def min_aad(max_temp_temp, axis=None):
    return np.mean(np.absolute(min_temp_temp - np.mean(min_temp_temp, axis)), axis)
print("Absolute average deviation (AAD) = {:.3f} (\u00B0C).".format(min_aad(min_temp_temp)))
mad_min_temp_temp = median_abs_deviation(min_temp_temp)
print("Median abosolute deviation (MAD) = {:.3f} (\u00B0C).".format(mad_min_temp_temp))
min_cov_matrix = np.cov(min_temp_temp, bias=True)
print("Covariance matrix = {:.3f}.".format(min_cov_matrix))
print("Skewness = {:.3f}.".format(stats.skew(min_temp_temp)))
print("Kurtosis = {:.3f}.".format(stats.kurtosis(min_temp_temp)))

print("\nOther Summary Statistics:")
r, p = stats.spearmanr(max_temp_temp, min_temp_temp)
# -1: a perfect negative relationship between two variables
# 0: no relationship between two variables
# 1: a perfect positive relationship between two variables
print("Spearman's Rank Correlation Coefficient = {:.4f}.".format(r))
print("The corresponding p-value = {:.4f}.".format(p))
