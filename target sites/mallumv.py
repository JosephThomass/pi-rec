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

search = input('enter movie name')
url = "https://mallumv.cc/search.php?q="+search
web_data = requests.get(url, headers=headers, timeout=40).text
soup = BeautifulSoup(web_data,'html.parser')
rows =soup.find_all('div', {'body.div=$0'})
# print(rows[0])
# data_list = []
for i in rows:
    print(i.h2.text,i.a['href'])
# print(data_list)