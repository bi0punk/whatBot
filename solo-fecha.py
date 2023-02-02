
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
    fecha_data = datetime.datetime.now()

    dia = (fecha_data.year)
    mes = (fecha_data.strftime("%m"))
    año = (fecha_data.strftime("%m"))

    link = 'https://es.wikipedia.org/wiki/'+ str(today.day) + '_de_enero'
    link_sismos = 'https://www.sismologia.cl/sismicidad/catalogo/' +str(today.year) + '/' +str(today.month) + '/' +str(today.year) +str(today.month) +str(today.day) + '.html'
    print(link)
    print(link_sismos)
generador_fechas()


