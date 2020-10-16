#!/usr/bin/env python3

import os
from PIL import Image

user = os.environ.get("USER")
dir = '/home/{}/supplier-data/images/'.format(user)
for infile in os.listdir(dir):
    filename = os.path.splitext(infile)[0]
    outfile = filename + ".jpeg"
    if infile.endswith(".tiff"):
        with Image.open(dir + infile) as im:
            im.resize((600,400)).convert('RGB').save(dir + outfile)
