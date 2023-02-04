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



def trends_scrapper():

    URL = 'https://www.litoralpress.cl/sitio/trendings.cshtml'
    website_url = requests.get(URL).text   
    soup = BeautifulSoup(website_url,'lxml')
    section = soup.find('ul', class_ = 'numeros').parent
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



def envia_mensaje():
    global emoji
    emoji3 = "🔥"
    print(emoji3)
    emoji2 = (emoji.emojize(":grinning_face_with_big_eyes:"))
    print(emoji.emojize(":winking_face_with_tongue:"))
    print(emoji.emojize(":zipper-mouth_face:"))

    title = "*Top 10 Trending Topic Chile*\n"
    pywhatkit.sendwhatmsg_to_group(f"token",(emoji3)+"🔥"+(title)+(string_trending), 20, 2)









""" generador_fechas() """
trends_scrapper()
envia_mensaje()

