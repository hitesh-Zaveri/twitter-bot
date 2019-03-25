# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 03:08:42 2019

@author: Hitesh Javeri
"""

import tweepy as tp
import time
import os

consumer_key="DcQYb2OpGFtvj8NniULMiKvAa"
consumer_secret="o2yKzQhUuNSjX2Cv2grNfZsdtMFmJ6KlRpXgDg3RhNgCZlRqv8"
access_token="1092178457096671233-Ae2qHWsyfFOSR2Z0RU77pykHmn2cMk"
access_secret="MfE3wTHZRwj4Dc4FnnceqRsE5VjtnXdlF3sgWMeYAjnlU"

auth=tp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tp.API(auth)

os.chdir("car")

for img in os.listdir("."):
    api.update_with_media(img)
    time.sleep(5)
    
    
    