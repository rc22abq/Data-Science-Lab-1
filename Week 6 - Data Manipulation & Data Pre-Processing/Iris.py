# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 17:06:35 2023

@author: jdpev
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# The .data file is a csv so we can load it as usual. However, it has no
# headers. BY looking on the UCI page we get the relevant information.

column_names = ['Sepal Length (cm)', 'Sepal Width (cm)',
                'Petal Length (cm)', 'Petal Width (cm)',
                'Species']

df = pd.read_csv('iris.data', names=column_names)
    
# Not all columns will be output, so we change that
pd.set_option('display.expand_frame_repr', False)        
print(df.head(10),
      '\n----------------------------------\n')

# Now print summary statistics
print(df.describe(),
      '\n----------------------------------\n')

# We can see if there are any duplicates. We should see just three unique
# species.
print(df.drop_duplicates(subset='Species'),
      '\n----------------------------------\n')

# We can also see that there are 50 of each species.
print(df.value_counts('Species'),
      '\n----------------------------------\n')

# Next, we can perform some basic visualisations. We will use seaborn this
# time, but matplotlib works fine too
plt.figure(0)
sns.scatterplot(x='Sepal Length (cm)', y='Sepal Width (cm)',
                hue='Species', data=df, )
plt.legend(bbox_to_anchor=(1, 1), loc=2)
 
plt.figure(1)
sns.scatterplot(x='Petal Length (cm)', y='Petal Width (cm)',
                hue='Species', data=df, )
plt.legend(bbox_to_anchor=(1, 1), loc=2)

plot = sns.FacetGrid(df, hue='Species')
plot.map(sns.distplot, 'Sepal Length (cm)').add_legend()

plot = sns.FacetGrid(df, hue='Species')
plot.map(sns.distplot, 'Sepal Width (cm)').add_legend()
 
plot = sns.FacetGrid(df, hue='Species')
plot.map(sns.distplot, 'Petal Length (cm)').add_legend()
 
plot = sns.FacetGrid(df, hue='Species')
plot.map(sns.distplot, 'Petal Width (cm)').add_legend()


# Finally, consider outliers.
plt.figure(7)
sns.boxplot(x='Sepal Width (cm)', data=df) # above 4 and below 2 are outliers

# First we look at IQR
Q1 = np.percentile(df['Sepal Width (cm)'], 25,
                interpolation = 'midpoint')
 
Q3 = np.percentile(df['Sepal Width (cm)'], 75,
                interpolation = 'midpoint')
IQR = Q3 - Q1
print('\nIQR is ', IQR)
 
print("\nOld Shape: ", df.shape)
 
# Now we compute upper bound.
upper = np.where(df['Sepal Width (cm)'] >= (Q3 + 1.5*IQR))
 
# and lower bound
lower = np.where(df['Sepal Width (cm)'] <= (Q1 - 1.5*IQR))
 
# Finally, we remove outliers
df.drop(upper[0], inplace = True)
df.drop(lower[0], inplace = True)
 
print("New Shape: ", df.shape)
 
plt.figure(8)
sns.boxplot(x='Sepal Width (cm)', data=df)

plt.show()