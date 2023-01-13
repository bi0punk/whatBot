import pywhatkit
import requests
from bs4 import BeautifulSoup
import csv
from datetime import time, date
import pywhatkit

def fecha_efemerides():
    today = date.today()
    print("año:", today.year)
    print("mes:", today.month)
    print("dia:", today.day)
    link = 'https://es.wikipedia.org/wiki/'+ str(today.day) + '_de_enero'
    print(link)


def trends_scrapper(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    """ soup = BeautifulSoup(r.content, 'html5lib') """
    data = soup.find_all('li', class_ = 'trend-card')
    contador = 0
    lista = []
    for i in data:
        if contador < 50:
            lista.append(i)
        else:
            break
        contador += 1
    print(lista)
    global trends_texto
    trends_mostrar = lista[0:5]
    trends_texto = ' '.join(trends_mostrar)
    print(trends_mostrar)
    """ print('[ʙᴏᴛ] ᴛᴏᴘ 5 ᴄʜɪʟᴇ ᴛʀᴇɴᴅɪɴɢ') """


trends_scrapper('https://trends24.in/chile/')   
fecha_efemerides()

def envia_mensaje(trends_texto):
    # Send a WhatsApp Message to a Contact at 1:30 PM
    first = trends_texto[0]
    second = trends_texto[1]
    third = trends_texto[2]
    fourth = trends_texto[3]
    fifth = trends_texto[4]
    pywhatkit.sendwhatmsg("+56975423355", "hola", 20, 45)

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

envia_mensaje(trends_texto)