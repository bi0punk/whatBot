
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



# initializing date
test_date = datetime.datetime.strptime("01-7-2022", "%d-%m-%Y")

# initializing K
K = 5

date_generated = pd.date_range(test_date, periods=K)
print(date_generated.strftime("%d-%m-%Y"))


def generador_fechas():

    print("Ingrese  de inicio")
    fecha_consultar = input()
    fecha_data = datetime.datetime.now()
    anio = (fecha_data.year)
    mes = (fecha_data.strftime("%m"))
    dia = (fecha_data.strftime("%d"))
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
        if status == 403:
            time.sleep(5000)
            print("esperando")
            return timer()
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


