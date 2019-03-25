# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 00:53:54 2019

@author: Hitesh Javeri
"""
import os
import requests
from bs4 import BeautifulSoup as bs

page=requests.get("https://pixabay.com/en/photos/car/")
soup=bs(page.content,"lxml")
#print(soup.prettify())
img_tags=soup.find_all("img")
#print(soup)
if not os.path.exists("car"):
    os.makedirs("car")

os.chdir("car")

x=0

for image in img_tags:
        url=image.attrs["src"]
        source=requests.get(url)
        if source.status_code==200:
            with open("pic-"+str(x)+".jpg","wb") as f:
                f.write(source.content)
            
                f.close
                x+=1