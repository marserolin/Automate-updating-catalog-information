#!/usr/bin/env python3
import os
import requests

user = os.environ.get('USER')
dir = '/home/{}/supplier-data/descriptions/'.format(user)
descriptions = {}
url = 'http://localhost/fruits/'
for file in os.listdir(dir):
    with open(dir + file, 'r') as txt:
        descriptions['name'] = txt.readline()
        weight = txt.readline()
        lbs = weight[:-4]
        int_weight = int(lbs)
        descriptions['weight'] = int_weight
        descriptions['description'] = txt.readline()
        f = os.path.splitext(file)[0]
        img_file = f + ".jpeg"
        descriptions['image_name'] = img_file
        response = requests.post(url, data=descriptions)
        response.raise_for_status()
        print(response.request.url)
        print(response.status_code)
