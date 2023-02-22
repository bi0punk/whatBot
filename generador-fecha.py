
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

    print("Ingrese fecha")
    fecha_consultar = input()
    fecha_data = datetime.datetime.now()

    print(fecha_data)
    anio = (fecha_data.year)
    mes = (fecha_data.strftime("%m"))
    """ anio = (fecha_data.strftime("%y")) """
    dia = (fecha_data.strftime("%d"))
    print(anio)
    print(mes)
    global link_sismos2
    link_sismos2 = f'https://www.sismologia.cl/sismicidad/catalogo/{(fecha_data.year)}/{(mes)}/{(fecha_data.year)}{(mes)}{(dia)}.html'
    print(link_sismos2)
    return link_sismos2

generador_fechas()

def timer():
    while True:
        response= requests.get(link_sismos2)   
        status= response.status_code
        print(status)
        table_MN = pd.read_html(link_sismos2)
        

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
t = threading.Thread(target=timer)
t.start()

