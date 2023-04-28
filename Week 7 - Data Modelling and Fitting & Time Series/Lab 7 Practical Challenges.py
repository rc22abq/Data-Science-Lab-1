# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 11:20:24 2023

@author: User
"""

# Lab 7 Practical Challenges

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

mean = 0
sigma = 10

# Random number generator based off of a Gaussian distribution
noise = np.random.normal(mean,sigma, [256,256])

# Plotting
plt.figure()
plt.imshow(noise)
plt.colorbar()
plt.show()

##############################################################################

image = Image.open("computer.png")
g_noise = np.ones_like(image)

# Plotting
plt.figure()
plt.imshow(image)
plt.show()
plt.title("Normal computer")
print(image)

for i in range(4):
    g_noise[:,:,i] = noise
noise_image = np.array(image) + g_noise

# Plotting
plt.figure()
plt.imshow(noise_image)
plt.title("Computer with noise")
plt.show()

######################################################################

three_sig = np.where(noise > 30,1,0)
print(100 * np.sum(three_sig)/(256*256))

######################################################################

noise_image = np.array(noise_image)
plt.figure()
plt.imshow(noise_image[:,:,0])
plt.title("Computer with 'greyscale'")
plt.show()

######################################################################

mask = np.where(noise_image[:,:,0] > 30,1,0)
plt.figure()
plt.imshow(mask)
plt.title("Computer with mask")
plt.show()