import pywhatkit
import requests
from bs4 import BeautifulSoup
import csv
from datetime import time, date
import pandas as pd
import urllib.request



def fecha_efemerides():

    today = date.today()
    print("año:", today.year)
    print("mes:", today.month)
    print("dia:", today.day)
    link = 'https://es.wikipedia.org/wiki/'+ str(today.day) + '_de_enero'
    print(link)


def trends_scrapper():

    URL = 'https://www.litoralpress.cl/sitio/trendings.cshtml'
    website_url = requests.get(URL).text   
    soup = BeautifulSoup(website_url,'lxml')
    section = soup.find('ul', class_ = 'numeros').parent

    lista_trendings = []
    for x in section.find_next('ul').select('li'):
            lista_trendings.append(x.get('title'))
    print('\n')
    print(lista_trendings)
    print('\n')



def envia_mensaje():
    pywhatkit.sendwhatmsg_to_group("GROUP ID", "Hey All!", 14, 00)
    


fecha_efemerides()
trends_scrapper()
envia_mensaje()



