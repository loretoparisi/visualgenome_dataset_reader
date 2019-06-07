#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from smart_open import open
import  json

from io import BytesIO
from zipfile import ZipFile
import requests

def get_zip(file_url):
    '''
        read zip 
        https://stackoverflow.com/a/34863053/758836
    '''
    url = requests.get(file_url)
    zipfile = ZipFile(BytesIO(url.content))
    zip_names = zipfile.namelist()
    if len(zip_names) == 1:
        file_name = zip_names.pop()
        extracted_file = zipfile.open(file_name)
        return extracted_file
    return [zipfile.open(file_name) for file_name in zip_names]

# to download from zip
uri = 'https://visualgenome.org/static/data/dataset/region_descriptions.json.zip'

# grab zip file and deflate
zipfile = get_zip(uri)
# open deflated zip
with open(zipfile, encoding="ISO-8859-1") as fin:
    text = fin.read()
    print(len(text))
    json_data = json.loads( text )
    print( len(json_data) )
    print( json.dumps(json_data) ) 
    #print( json.dumps(json_data, indent=4, sort_keys=True) ) 




