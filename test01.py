import pywhatkit
import requests
from bs4 import BeautifulSoup
import csv
from datetime import time, date
import pandas as pd
import urllib.request
import threading
import time
import urllib.request
import pandas as pd
import datetime
import emoji

import requests
from bs4 import BeautifulSoup
import pandas as pd



def trends_scrapper():

    URL = 'https://es.wikipedia.org/wiki/5_de_febrero'
    website_url = requests.get(URL).text   
    soup = BeautifulSoup(website_url,'lxml')
    section = soup.find('ul').parent
    global lista_trendings
    lista_trendings = []
    for x in section.find_next('ul').select('li'):
            lista_trendings.append(x.get('title'))
    print('\n')
    print(lista_trendings)
    global string_trending
    string_trending = "\n".join(lista_trendings)
    print(string_trending)
    return string_trending

trends_scrapper