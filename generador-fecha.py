
import requests
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

    link = 'https://es.wikipedia.org/wiki/'+ str(fecha_data.day) + '_de_enero'
    link_sismos = 'https://www.sismologia.cl/sismicidad/catalogo/' +str(fecha_data.year) + '/' +str(fecha_data.month) + '/' +str(fecha_data.year) +str(fecha_data.month) +str(fecha_data.day) + '.html'
    print(link)
    print(link_sismos)
generador_fechas()


