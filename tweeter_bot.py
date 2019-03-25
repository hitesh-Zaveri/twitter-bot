# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 03:08:42 2019

@author: Hitesh Javeri
"""

import tweepy as tp
import time
import os

consumer_key=""
consumer_secret=""
access_token=""
access_secret=""

auth=tp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tp.API(auth)

os.chdir("car")

for img in os.listdir("."):
    api.update_with_media(img)
    time.sleep(5)
    
    
    
