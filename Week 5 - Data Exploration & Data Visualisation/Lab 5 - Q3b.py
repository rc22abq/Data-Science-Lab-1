# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:21:30 2023

@author: User
"""

import matplotlib.pyplot as plt
import numpy as np
from pandas import Series

num = np.random.uniform(0,1,(16))

s3 = Series(num, 
            index = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                     'n','o','p'])
print('Series s3 =\n', s3, '\n')

plt.figure()
plt.bar(s3,num)
plt.legend()
plt.show()