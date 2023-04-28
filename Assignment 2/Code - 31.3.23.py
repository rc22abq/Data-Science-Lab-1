# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:06:12 2023

@author: User
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# Loading the CSV file with the needed columns
df = pd.read_csv('climate_change.csv', skiprows=4,
                 usecols=[0, 2, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                          50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65])

# Removing spaces from column names
df = df.rename(columns={"Country Name": "Country_Name"})
df = df.rename(columns={"Indicator Name": "Indicator_Name"})






# CO2 EMISSIONS


# Selecting all the CO2 emissions (kt) data
df2 = df.query("Indicator_Name == 'CO2 emissions (kt)'")


# Plotting CO2 emissions for high income countries
years = list(range(1990, 2020))
years_2d = [years[i:i+30] for i in range(0, len(years), 30)]
selected_years_high_income_data = df2.iloc[95:96, 2:-2]
data_list_high_income = selected_years_high_income_data.values.tolist()
years_2d = np.array(years_2d)
data_list_high_income = np.array(data_list_high_income)
x1_high_income = years_2d[0, :]
y1_high_income = data_list_high_income[0, :]
plt.plot(x1_high_income, y1_high_income, "r.")
a, b, c, = np.polyfit(x1_high_income, y1_high_income, 2)
plt.plot(x1_high_income, a*x1_high_income**2+b*x1_high_income+c)
plt.xlabel("Years")
plt.ylabel("CO2 emissions (kt)")
plt.title("CO2 emissions (kt) for High Income Countries (HIC)")
plt.show()

# Plotting CO2 emissions for low income countries
years = list(range(1990, 2020))
years_2d = [years[i:i+30] for i in range(0, len(years), 30)]
selected_years_low_income_data = df2.iloc[135:136, 2:-2]
data_list_low_income = selected_years_low_income_data.values.tolist()
years_2d = np.array(years_2d)
data_list_low_income = np.array(data_list_low_income)
x1_low_income = years_2d[0, :]
y1_low_income = data_list_low_income[0, :]
plt.plot(x1_low_income, y1_low_income, "r.")
a, b, c, = np.polyfit(x1_low_income, y1_low_income, 2)
plt.plot(x1_low_income, a*x1_low_income**2+b*x1_low_income+c)
plt.xlabel("Years")
plt.ylabel("CO2 emissions (kt)")
plt.title("CO2 emissions (kt) for Low Income Countries (LIC)")
plt.show()

# Plotting CO2 emissions for middle income countries
years = list(range(1990, 2020))
years_2d = [years[i:i+30] for i in range(0, len(years), 30)]
selected_years_middle_income_data = df2.iloc[156:157, 2:-2]
data_list_middle_income = selected_years_middle_income_data.values.tolist()
years_2d = np.array(years_2d)
data_list_middle_income = np.array(data_list_middle_income)
x1_middle_income = years_2d[0, :]
y1_middle_income = data_list_middle_income[0, :]
plt.plot(x1_middle_income, y1_middle_income, "r.")
a, b, c, = np.polyfit(x1_middle_income, y1_middle_income, 2)
plt.plot(x1_middle_income, a*x1_middle_income**2+b*x1_middle_income+c)
plt.xlabel("Years")
plt.ylabel("CO2 emissions (kt)")
plt.title("CO2 emissions (kt) for Middle Income Countries (MIC)")
plt.show()

# Plotting CO2 emissions for United Kingdom (HIC)
years = list(range(1990, 2020))
years_2d = [years[i:i+30] for i in range(0, len(years), 30)]
selected_years_uk_data = df2.iloc[81:82, 2:-2]
data_list_uk = selected_years_uk_data.values.tolist()
years_2d = np.array(years_2d)
data_list_uk = np.array(data_list_uk)
x1_uk = years_2d[0, :]
y1_uk = data_list_uk[0, :]
plt.plot(x1_uk, y1_uk, "r.")
a, b, c, = np.polyfit(x1_uk, y1_uk, 2)
plt.plot(x1_uk, a*x1_uk**2+b*x1_uk+c)
plt.xlabel("Years")
plt.ylabel("CO2 emissions (kt)")
plt.title("CO2 emissions (kt) for United Kingdom (HIC)")
plt.show()

# Plotting CO2 emissions for Afghanistan (LIC)
years = list(range(1990, 2020))
years_2d = [years[i:i+30] for i in range(0, len(years), 30)]
selected_years_afg_data = df2.iloc[2:3, 2:-2]
data_list_afg = selected_years_afg_data.values.tolist()
years_2d = np.array(years_2d)
data_list_afg = np.array(data_list_afg)
x1_afg = years_2d[0, :]
y1_afg = data_list_afg[0, :]
plt.plot(x1_afg, y1_afg, "r.")
a, b, c, = np.polyfit(x1_afg, y1_afg, 2)
plt.plot(x1_afg, a*x1_afg**2+b*x1_afg+c)
plt.xlabel("Years")
plt.ylabel("CO2 emissions (kt)")
plt.title("CO2 emissions (kt) for Afghanistan (LIC)")
plt.show()

# Plotting CO2 emissions for India (MIC)
years = list(range(1990, 2020))
years_2d = [years[i:i+30] for i in range(0, len(years), 30)]
selected_years_ind_data = df2.iloc[109:110, 2:-2]
data_list_ind = selected_years_ind_data.values.tolist()
years_2d = np.array(years_2d)
data_list_ind = np.array(data_list_ind)
x1_ind = years_2d[0, :]
y1_ind = data_list_ind[0, :]
plt.plot(x1_ind, y1_ind, "r.")
a, b, c, = np.polyfit(x1_ind, y1_ind, 2)
plt.plot(x1_ind, a*x1_ind**2+b*x1_ind+c)
plt.xlabel("Years")
plt.ylabel("CO2 emissions (kt)")
plt.title("CO2 emissions (kt) for India (MIC)")
plt.show()

# Plotting CO2 emissions for UK, Afghanistan and India
plt.plot(x1_uk, y1_uk, "r.", label="United Kingdom (HIC)")
plt.plot(x1_afg, y1_afg, "b.", label="Afghanistan (LIC)")
plt.plot(x1_ind, y1_ind, "g.", label="India (MIC)")
a_uk, b_uk, c_uk, = np.polyfit(x1_uk, y1_uk, 2)
plt.plot(x1_uk, a_uk*x1_uk**2+b_uk*x1_uk+c_uk, "r-")
a_afg, b_afg, c_afg, = np.polyfit(x1_afg, y1_afg, 2)
plt.plot(x1_afg, a_afg*x1_afg**2+b_afg*x1_afg+c_afg, "b-")
a_ind, b_ind, c_ind, = np.polyfit(x1_ind, y1_ind, 2)
plt.plot(x1_ind, a_ind*x1_ind**2+b_ind*x1_ind+c_ind, "g-")
plt.yscale("log")
plt.xlabel("Years")
plt.ylabel("CO2 emissions (kt)")
plt.title("CO2 emissions (kt) for United Kingdom (HIC), Afghanistan (LIC) & India (MIC) on a Log Scale")
plt.legend()
plt.show()





# POPULATION TOTALS


# Selecting all the Population, total data
df3 = df.query("Indicator_Name == 'Population growth (annual %)'")


# Plotting Population Totals for high income countries
years = list(range(1990, 2020))
years_2d = [years[i:i+30] for i in range(0, len(years), 30)]
selected_years_high_income_data = df3.iloc[95:96, 2:-2]
data_list_high_income = selected_years_high_income_data.values.tolist()
years_2d = np.array(years_2d)
data_list_high_income = np.array(data_list_high_income)
x1_high_income = years_2d[0, :]
y1_high_income = data_list_high_income[0, :]
selected_years_high_income_data_1 = df3.iloc[95:96, 2:-6]
data_list_high_income_1 = selected_years_high_income_data_1.values.tolist()
data_list_high_income_1 = np.array(data_list_high_income_1)
y1_high_income_1 = data_list_high_income_1[0, :]
y1_high_income_population = y1_high_income_1
plt.plot(x1_high_income, y1_high_income, "r.")
a, b, c, = np.polyfit(x1_high_income, y1_high_income, 2)
plt.plot(x1_high_income, a*x1_high_income**2+b*x1_high_income+c)
plt.xlabel("Years")
plt.ylabel("Population Growth (annual %)")
plt.title("Population Growth (annual %) for High Income Countries (HIC)")
plt.show()

# Plotting Population Totals for low income countries
years = list(range(1990, 2020))
years_2d = [years[i:i+30] for i in range(0, len(years), 30)]
selected_years_low_income_data = df3.iloc[135:136, 2:-2]
data_list_low_income = selected_years_low_income_data.values.tolist()
years_2d = np.array(years_2d)
data_list_low_income = np.array(data_list_low_income)
x1_low_income = years_2d[0, :]
y1_low_income = data_list_low_income[0, :]
plt.plot(x1_low_income, y1_low_income, "r.")
a, b, c, = np.polyfit(x1_low_income, y1_low_income, 2)
plt.plot(x1_low_income, a*x1_low_income**2+b*x1_low_income+c)
plt.xlabel("Years")
plt.ylabel("Population Growth (annual %)")
plt.title("Population Growth (annual %) for Low Income Countries (LIC)")
plt.show()

# Plotting Population Totals for middle income countries
years = list(range(1990, 2020))
years_2d = [years[i:i+30] for i in range(0, len(years), 30)]
selected_years_middle_income_data = df3.iloc[156:157, 2:-2]
data_list_middle_income = selected_years_middle_income_data.values.tolist()
years_2d = np.array(years_2d)
data_list_middle_income = np.array(data_list_middle_income)
x1_middle_income = years_2d[0, :]
y1_middle_income = data_list_middle_income[0, :]
selected_years_middle_income_data_1 = df3.iloc[95:96, 2:-7]
data_list_middle_income_1 = selected_years_middle_income_data_1.values.tolist()
data_list_middle_income_1 = np.array(data_list_middle_income_1)
y1_middle_income_1 = data_list_middle_income_1[0, :]
y1_middle_income_population = y1_middle_income_1
plt.plot(x1_middle_income, y1_middle_income, "r.")
a, b, c, = np.polyfit(x1_middle_income, y1_middle_income, 2)
plt.plot(x1_middle_income, a*x1_middle_income**2+b*x1_middle_income+c)
plt.xlabel("Years")
plt.ylabel("Population Growth (annual %)")
plt.title("Population Growth (annual %) for Middle Income Countries (MIC)")
plt.show()

# Plotting Population Totals for United Kingdom (HIC)
years = list(range(1990, 2020))
years_2d = [years[i:i+30] for i in range(0, len(years), 30)]
selected_years_uk_data = df3.iloc[81:82, 2:-2]
data_list_uk = selected_years_uk_data.values.tolist()
years_2d = np.array(years_2d)
data_list_uk = np.array(data_list_uk)
x1_uk = years_2d[0, :]
y1_uk = data_list_uk[0, :]
selected_years_uk_data_1 = df3.iloc[95:96, 2:-7]
data_list_uk_1 = selected_years_uk_data_1.values.tolist()
data_list_uk_1 = np.array(data_list_uk_1)
y1_uk_1 = data_list_uk_1[0, :]
y1_uk_population = y1_uk_1
plt.plot(x1_uk, y1_uk, "r.")
a, b, c, = np.polyfit(x1_uk, y1_uk, 2)
plt.plot(x1_uk, a*x1_uk**2+b*x1_uk+c)
plt.xlabel("Years")
plt.ylabel("Population Growth (annual %)")
plt.title("Population Growth (annual %) for United Kingdom (HIC)")
plt.show()

# Plotting Population Totals for Afghanistan (LIC)
years = list(range(1990, 2020))
years_2d = [years[i:i+30] for i in range(0, len(years), 30)]
selected_years_afg_data = df3.iloc[2:3, 2:-2]
data_list_afg = selected_years_afg_data.values.tolist()
years_2d = np.array(years_2d)
data_list_afg = np.array(data_list_afg)
x1_afg = years_2d[0, :]
y1_afg = data_list_afg[0, :]
plt.plot(x1_afg, y1_afg, "r.")
a, b, c, = np.polyfit(x1_afg, y1_afg, 2)
plt.plot(x1_afg, a*x1_afg**2+b*x1_afg+c)
plt.xlabel("Years")
plt.ylabel("Population Growth (annual %)")
plt.title("Population Growth (annual %) for Afghanistan (LIC)")
plt.show()

# Plotting Population Totals for India (MIC)
years = list(range(1990, 2020))
years_2d = [years[i:i+30] for i in range(0, len(years), 30)]
selected_years_ind_data = df3.iloc[109:110, 2:-2]
data_list_ind = selected_years_ind_data.values.tolist()
years_2d = np.array(years_2d)
data_list_ind = np.array(data_list_ind)
x1_ind = years_2d[0, :]
y1_ind = data_list_ind[0, :]
selected_years_ind_data_1 = df3.iloc[95:96, 2:-7]
data_list_ind_1 = selected_years_ind_data_1.values.tolist()
data_list_ind_1 = np.array(data_list_ind_1)
y1_ind_1 = data_list_ind_1[0, :]
y1_ind_population = y1_ind_1
plt.plot(x1_ind, y1_ind, "r.")
a, b, c, = np.polyfit(x1_ind, y1_ind, 2)
plt.plot(x1_ind, a*x1_ind**2+b*x1_ind+c)
plt.xlabel("Years")
plt.ylabel("Population Growth (annual %)")
plt.title("Population Growth (annual %) for India (MIC)")
plt.show()

# Plotting Population Totals for UK, Afghanistan and India
plt.plot(x1_uk, y1_uk, "r.", label="United Kingdom (HIC)")
plt.plot(x1_afg, y1_afg, "b.", label="Afghanistan (LIC)")
plt.plot(x1_ind, y1_ind, "g.", label="India (MIC)")
a_uk, b_uk, c_uk, = np.polyfit(x1_uk, y1_uk, 2)
plt.plot(x1_uk, a_uk*x1_uk**2+b_uk*x1_uk+c_uk, "r-")
a_afg, b_afg, c_afg, = np.polyfit(x1_afg, y1_afg, 2)
plt.plot(x1_afg, a_afg*x1_afg**2+b_afg*x1_afg+c_afg, "b-")
a_ind, b_ind, c_ind, = np.polyfit(x1_ind, y1_ind, 2)
plt.plot(x1_ind, a_ind*x1_ind**2+b_ind*x1_ind+c_ind, "g-")
plt.yscale("log")
plt.xlabel("Years")
plt.ylabel("Population Growth (annual %)")
plt.title("Population Growth (annual %) for United Kingdom (HIC), Afghanistan (LIC) & India (MIC) on a Log Scale")
plt.legend()
plt.show()






# Energy use (kg of oil equivalent per capita)


# Selecting all the Energy use data
df4 = df.query("Indicator_Name == 'Energy use (kg of oil equivalent per capita)'")

# Plotting Energy use for high income countries
years = list(range(1990, 2016))
years_2d = [years[i:i+26] for i in range(0, len(years), 26)]
selected_years_high_income_data = df4.iloc[95:96, 2:-6]
data_list_high_income = selected_years_high_income_data.values.tolist()
years_2d = np.array(years_2d)
data_list_high_income = np.array(data_list_high_income)
x1_high_income = years_2d[0, :]
y1_high_income = data_list_high_income[0, :]
y1_high_income_energy = y1_high_income
plt.plot(x1_high_income, y1_high_income, "r.")
a, b, c, = np.polyfit(x1_high_income, y1_high_income, 2)
plt.plot(x1_high_income, a*x1_high_income**2+b*x1_high_income+c)
plt.xlabel("Years")
plt.ylabel("Energy use (kg of oil equivalent per capita)")
plt.title("Energy use for High Income Countries (HIC)")
plt.show()

# Plotting Energy use for middle income countries
years = list(range(1990, 2015))
years_2d = [years[i:i+25] for i in range(0, len(years), 25)]
selected_years_middle_income_data = df4.iloc[156:157, 2:-7]
data_list_middle_income = selected_years_middle_income_data.values.tolist()
years_2d = np.array(years_2d)
data_list_middle_income = np.array(data_list_middle_income)
x1_middle_income = years_2d[0, :]
y1_middle_income = data_list_middle_income[0, :]
y1_middle_income_energy = y1_middle_income
plt.plot(x1_middle_income, y1_middle_income, "r.")
a, b, c, = np.polyfit(x1_middle_income, y1_middle_income, 2)
plt.plot(x1_middle_income, a*x1_middle_income**2+b*x1_middle_income+c)
plt.xlabel("Years")
plt.ylabel("Energy use (kg of oil equivalent per capita)")
plt.title("Energy use for Middle Income Countries (MIC)")
plt.show()

# Plotting Energy use for United Kingdom (HIC)
years = list(range(1990, 2015))
years_2d = [years[i:i+25] for i in range(0, len(years), 25)]
selected_years_uk_data = df4.iloc[81:82, 2:-7]
data_list_uk = selected_years_uk_data.values.tolist()
years_2d = np.array(years_2d)
data_list_uk = np.array(data_list_uk)
x1_uk = years_2d[0, :]
y1_uk = data_list_uk[0, :]
y1_uk_energy = y1_uk
plt.plot(x1_uk, y1_uk, "r.")
a, b, c, = np.polyfit(x1_uk, y1_uk, 2)
plt.plot(x1_uk, a*x1_uk**2+b*x1_uk+c)
plt.xlabel("Years")
plt.ylabel("Energy use (kg of oil equivalent per capita)")
plt.title("Energy use for United Kingdom (HIC)")
plt.show()

# Plotting Energy use for Bangladesh (LIC)
years = list(range(1990, 2015))
years_2d = [years[i:i+25] for i in range(0, len(years), 25)]
selected_years_ban_data = df4.iloc[20:21, 2:-7]
data_list_ban = selected_years_ban_data.values.tolist()
years_2d = np.array(years_2d)
data_list_ban = np.array(data_list_ban)
x1_ban = years_2d[0, :]
y1_ban = data_list_ban[0, :]
y1_ban_energy = y1_ban
plt.plot(x1_ban, y1_ban, "r.")
a, b, c, = np.polyfit(x1_ban, y1_ban, 2)
plt.plot(x1_ban, a*x1_ban**2+b*x1_ban+c)
plt.xlabel("Years")
plt.ylabel("Energy use (kg of oil equivalent per capita)")
plt.title("Energy use for Bangladesh (LIC)")
plt.show()

# Plotting Energy use for India (MIC)
years = list(range(1990, 2015))
years_2d = [years[i:i+25] for i in range(0, len(years), 25)]
selected_years_ind_data = df4.iloc[109:110, 2:-7]
data_list_ind = selected_years_ind_data.values.tolist()
years_2d = np.array(years_2d)
data_list_ind = np.array(data_list_ind)
x1_ind = years_2d[0, :]
y1_ind = data_list_ind[0, :]
y1_ind_energy = y1_ind
plt.plot(x1_ind, y1_ind, "r.")
a, b, c, = np.polyfit(x1_ind, y1_ind, 2)
plt.plot(x1_ind, a*x1_ind**2+b*x1_ind+c)
plt.xlabel("Years")
plt.ylabel("Energy use (kg of oil equivalent per capita)")
plt.title("Energy use for India (MIC)")
plt.show()

# Plotting Energy use for UK and India
plt.plot(x1_uk, y1_uk, "r.", label="United Kingdom (HIC)")
plt.plot(x1_ban, y1_ban, "b.", label="Bangladesh (LIC)")
plt.plot(x1_ind, y1_ind, "g.", label="India (MIC)")
a_uk, b_uk, c_uk, = np.polyfit(x1_uk, y1_uk, 2)
plt.plot(x1_uk, a_uk*x1_uk**2+b_uk*x1_uk+c_uk, "r-")
a_ban, b_ban, c_ban, = np.polyfit(x1_ban, y1_ban, 2)
plt.plot(x1_ban, a_ban*x1_ban**2+b_ban*x1_ban+c_ban, "b-")
a_ind, b_ind, c_ind, = np.polyfit(x1_ind, y1_ind, 2)
plt.plot(x1_ind, a_ind*x1_ind**2+b_ind*x1_ind+c_ind, "g-")
plt.xlabel("Years")
plt.ylabel("Energy use (kg of oil equivalent per capita)")
plt.title("Energy use for United Kingdom (HIC), Bangladesh (LIC) & India (MIC)")
plt.legend()
plt.show()





# Correlation between Population Totals and Energy use

# -1: a perfect negative relationship between two variables
# 0: no relationship between two variables
# 1: a perfect positive relationship between two variables


# Correlation for HIC
r, p = stats.pearsonr(y1_high_income_population, y1_high_income_energy)
print("Spearman's Rank Correlation Coefficient for HICs between Population Growth and Energy Use = {:.4f}.".format(r))
print("The corresponding p-value = {}.".format(round(p, 4)))

# Correlation for MIC
r, p = stats.pearsonr(y1_middle_income_population, y1_middle_income_energy)
print("\nSpearman's Rank Correlation Coefficient for MICs between Population Growth and Energy Use = {:.4f}.".format(r))
print("The corresponding p-value = {}.".format(round(p, 12)))

# Correlation for United Kingdom (HIC)
r, p = stats.pearsonr(y1_uk_population, y1_uk_energy)
print("\nSpearman's Rank Correlation Coefficient for the United Kingdom between Population Growth and Energy Use = {:.4f}.".format(r))
print("The corresponding p-value = {}.".format(round(p, 10)))

# Correlation for India (MIC)
r, p = stats.pearsonr(y1_ind_population, y1_ind_energy)
print("\nSpearman's Rank Correlation Coefficient for India between Population Growth and Energy Use = {:.4f}.".format(r))
print("The corresponding p-value = {}.".format(round(p, 17)))













