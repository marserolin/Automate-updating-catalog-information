#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
user = os.environ.get("USER")
dir = '/home/{}/supplier-data/images/'.format(user)
for file in os.listdir(dir):
    if file.endswith('.jpeg'):
        with open(dir + file, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
