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
    pywhatkit.sendwhatmsg_to_group(f"BR1USpeswsw0JkhlSeu5GG",{lista_trendings[1]}, 23, 55)


fecha_efemerides()
trends_scrapper()
envia_mensaje(lista_trendings)



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
