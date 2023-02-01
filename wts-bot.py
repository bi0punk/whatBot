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
import requests
import datetime


def generador_fechas():
    #funcion para obtener el dia, mes y año y formar ellink correspondiente para la consulta

    today = date.today()
    print("año:", today.year)
    print("mes:", today.month)
    print("dia:", today.day)

    a = len(str(today.month))
    print(a)

    if len(str(today.month)) == 1:
        mes = '0'+str(today.month)
        print(mes)
    else:
        mes = str(today.month)



    link = 'https://es.wikipedia.org/wiki/'+ str(today.day) + '_de_enero'
    link_sismos = 'https://www.sismologia.cl/sismicidad/catalogo/' +str(today.year) + '/' +str(today.month) + '/' +str(today.year) +str(today.month) +str(today.day) + '.html'
    print(link)
    print(link_sismos)


def scraping_sismos():
    while True:
        table_MN = pd.read_html('https://www.sismologia.cl/sismicidad/catalogo/2022/12/20221226.html')
        print(f'Total tables: {len(table_MN)}')
        global df
        df = table_MN[1]
        
        print(df)
        """ df.to_csv('file_name.csv', encoding='utf-8') """
        df.to_csv('datasismos.csv', mode='a', index=False, header=True, encoding='utf-8')
        fecha_data = datetime.datetime.now()
        print("\n")
        print(fecha_data)
        time.sleep(600)   # n segundos.
        
# Iniciar la ejecución en segundo plano.
t = threading.Thread(target=scraping_sismos)
t.start()





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

    string_trending = "-".join(lista_trendings)
    print(string_trending)

    print(*lista_trendings, sep = "\n")
    print('\n')
    """ return (lista_trendings)"""



def envia_mensaje(lista_trendings):
    pywhatkit.sendwhatmsg_to_group(f"KTDcC8Pe2XdLq1pgXEaKOj", "peo", 22, 33)


generador_fechas()
trends_scrapper()
envia_mensaje(lista_trendings)

#KTDcC8Pe2XdLq1pgXEaKOj
#I3PYrxw9eqFAXUELwcqJDU


""" # Same as above but Closes the Tab in 2 Seconds after Sending the Message
    pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)
    # Send an Image to a Group with the Caption as Hello
    pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")
    # Send an Image to a Contact with the no Caption
    pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")
    # Send a WhatsApp Message to a Group at 12:00 AM
    pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)
    # Send a WhatsApp Message to a Group instantly
    pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")
    # Play a Video on YouTube
    pywhatkit.playonyt("PyWhatKit") """


""" envia_mensaje(trends_texto) """
