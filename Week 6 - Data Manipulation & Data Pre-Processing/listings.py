# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:42:24 2023

@author: jdpev
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data set
df = pd.read_csv('listings.csv')

# Choose the  columns we are interested in
df2 = df[['price', 'accommodates', 'availability_30', 'availability_60',
          'availability_365']]

# As a sample, print the first 10 rows.
print(df2.head(10), '\n')

# Note 'price' is stored as an object. This is because of the $ signs and ','.
# Remove them. We will do this one at a time but you could do it all at once.

print(df2.dtypes, '\n')
df2['price'] = df2['price'].str.replace('$', '')
df2['price'] = df2['price'].str.replace(',','')

# No change strings to floats and check our answer.

df2['price'] = df2['price'].astype(float)
print(df2.dtypes, '\n')
print(df2.head(10), '\n')

# We can print some typical statistics using the describe method
print('\n', df2.describe(), '\n')

# Suppose we want to explore the columns separately
# Simple stats
mean1 = df2['price'].mean()
sum1 = df2['price'].sum()
max1 = df2['price'].max()
min1 = df2['price'].min()
count1 = df2['price'].count()
median1 = df2['price'].median() 
std1 = df2['price'].std() 
var1 = df2['price'].var() 

# print simple stats
print('mean price: ' + str(mean1))
print('sum of price: ' + str(sum1))
print('max price: ' + str(max1))
print('min price: ' + str(min1))
print('count of price: ' + str(count1))
print('median price: ' + str(median1))
print('std of price: ' + str(std1))
print('var of price: ' + str(var1)) 

# We can also produce various plots to highlight certain properties of the
# data. For example, we can plot accomodation numbers against price. If we
# plot too many on the figure it may be too crowded, so we look at just 50.

plt.figure(0)
plt.plot(df2['price'][0:50], df2['accommodates'][0:50],
         marker='o', linestyle='None', markerfacecolor='lightblue',
         markeredgecolor='black', markersize=4)
plt.xlabel('Price (first 50)')
plt.ylabel('Accommodates (first 50)')
plt.savefig('price_against_accomodation.png')

# We can plot a violin plot

plt.figure(1)
plt.violinplot(df2['availability_365'], showmedians=True)
plt.ylabel('Availability (over 365 days)')
plt.savefig('violin_plot_availability_365')

# Or a box plot

plt.figure(2)
plt.boxplot([df2['accommodates']],
            labels=['Sample'])
plt.ylabel('Accommodates')
plt.savefig('Box_plot_accommodates')

plt.show

