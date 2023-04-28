# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 16:32:26 2023

@author: jdpev
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy.stats.kde import gaussian_kde

# Create the noise
# More generally, we could use x, y = image.shape
mean = 0
var = 0.01
sigma = np.sqrt(var)
g_noise = np.random.normal(loc=mean, scale=sigma, size=(512,512))

# The original image
image = cv2.imread('goodgirl.jpg', 0)

# Resize the image
dim = (512,512)
image = cv2.resize(image, dim)

# Normalise
image = image/255

cv2.imshow('original image', image)
cv2.waitKey(0) 


cv2.imshow('Gaussian noise', g_noise)
cv2.waitKey(0)

# Display the probability density function
kde = gaussian_kde(g_noise.reshape(int(512*512)))
dist_space = np.linspace(np.min(g_noise), np.max(g_noise), 100)
plt.plot(dist_space, kde(dist_space))


# Add Gaussian noise

g = image + g_noise

cv2.imshow('Corrupted Image', g)
cv2.waitKey(0)

# Display all

cv2.imshow('original image', image)
cv2.imshow('Gaussian noise', g_noise)
cv2.imshow('Corrupted Image', g)
cv2.waitKey(0)

plt.show()