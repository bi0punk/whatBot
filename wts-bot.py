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
    """ print(section) """

    print('\n')
    print(lista_trendings)

    print('\n')





def envia_mensaje():
    # Send a WhatsApp Message to a Contact at 1:30 PM

    """ pywhatkit.sendwhatmsg("+56975423355", "hola", 20, 45) """

    pywhatkit.sendwhatmsg_to_group("BR1USpeswsw0JkhlSeu5GG", "Hey All!", 14, 00)
    








fecha_efemerides()
trends_scrapper()
envia_mensaje()





































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
#https://chat.whatsapp.com/KSWnhOCqnYR8kFVa7qMJ4y

""" envia_mensaje(trends_texto) """

"""BR1USpeswsw0JkhlSeu5GG"""