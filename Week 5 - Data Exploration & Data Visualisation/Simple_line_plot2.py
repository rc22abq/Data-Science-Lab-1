# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 13:07:20 2023

@author: jdpev
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4).cumsum(0),
                  columns=['A','B','C','D'],
                  index=np.arange(0,100,10))
# The 0 in cumsum(0) means that is adding over axis=0

df.plot()