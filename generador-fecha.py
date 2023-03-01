from datetime import time, date
import urllib.request
import pandas as pd
import threading
import datetime
import requests
import time
import csv

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
        


def generador_fechas():
    inicio = datetime.date(2020,1,1)
    periods = 5
    daterange = []
    for day in range(periods):
        date = (inicio + datetime.timedelta(days = day)).isoformat()
        daterange.append(date)
    print(daterange[0])

    for i in daterange:
        print(i[0:4])
    """ fecha_data = datetime.datetime.now()
    mes = (fecha_data.strftime("%m"))
    dia = (fecha_data.strftime("%d")) """
    fecha_data= 2020
    mes = 1
    dia = 1
    zzero = '0'
    
    global link_sismos2
    link_sismos2 = f'https://www.sismologia.cl/sismicidad/catalogo/2020/01/202001{(zzero)}{(dia)}.html'



    #link_sismos2 = f'https://www.sismologia.cl/sismicidad/catalogo/{(fecha_data)}/{(mes)}/{(fecha_data.year)}{(mes)}{(dia)}.html'

    dia = dia + 1
    print(link_sismos2)
    return link_sismos2

generador_fechas()



# Iniciar la ejecución en segundo plano.
t = threading.Thread(target=timer)
t.start()


