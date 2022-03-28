# data from https://directory.ifoam.bio/affiliates
# need to collect page by page
from bs4 import BeautifulSoup
import pandas as pd
import requests
# import ipywidgets as widgets
# from ipywidgets import interact
import time
import json
import csv
import re
headers = { 
    'User-Agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
    'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
    'Accept-Language' : 'en-US,en;q=0.5',
    'DNT'             : '1', # Do Not Track Request Header
    'Connection'      : 'close'
}

search = input('enter movie name:')
url = "https://9xmovies.plus/?s="+search
web_data = requests.get(url, headers=headers, timeout=40).text
soup = BeautifulSoup(web_data,'html.parser')
rows =soup.find_all('div', {'class': "thumb col-md-2 col-sm-4 col-xs-6"})
# print(rows[0])
data_list = []
for i in rows:
    
    data_list.append({
        "name":(re.sub(' +',' ',i.figure.figcaption.find('p').get_text())).strip(),
        "url":(re.sub(' +',' ',i.figure.figcaption.a['href'])).strip()
    })
print (url)
# print(data_list)