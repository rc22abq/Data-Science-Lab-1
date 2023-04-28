# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 10:04:45 2022

@author: jdpev
"""
import requests
from bs4 import BeautifulSoup

# Get our url
url = 'https://apod.nasa.gov/apod/astropix.html'

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# soup.findAll() returns a list of elements. We then iterate over the "image"
# variable and access the src attribute on it.
for img in soup.findAll('img'):
    src = img.get("src")
    if src:
        # resolve any relative urls to absolute urls using base URL
        src = requests.compat.urljoin(url, src)
        print('You have downloaded the following image:\n', src)
        # We now download the image
        response = requests.get(src)
        if response.status_code:
            fp = open('Astronomy_Picture_of_the_Day.jpeg', 'wb')
            fp.write(response.content)
            fp.close()