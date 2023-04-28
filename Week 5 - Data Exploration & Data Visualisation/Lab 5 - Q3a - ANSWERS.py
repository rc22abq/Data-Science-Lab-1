# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:51:47 2023

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


columns = ["A", "B", "C", "D"]
x = np.random.randint(0, 100, (10,4))
plt.figure()
plt.plot(x.cumsum(0), label=columns)
plt.legend()
plt.show()

df = pd.DataFrame(x.cumsum(0), columns=columns)

df.plot()



