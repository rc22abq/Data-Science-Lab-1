# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:48:15 2023

@author: rc22abq
"""

import numpy as np

X = np.arange(1,101)

Y = []
index = np.arange(1,51)

for i in index:
    x=2*i
    Y.append(x)
    
z1 = []

for x in X:
    z1.append(x)
    
for y in Y:
    if y not in z1:
        z1.append(y)
        
        
        
z2 = []

for x in X:
    if x in Y:
        z2.append(x)
        
for y in Y:
    if y in X and y not in z2:
        z2.append(y)
        




z3 = []

for x in X:
    if x not in Y:
        z3.append(x)
        
print(z3)