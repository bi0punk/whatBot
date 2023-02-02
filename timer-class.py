import threading
import time



class Timer(threading.Thread):
    def __init__(self):
        #definimos atributo timer runs que seria la inicializacion del evento threa
        self._timer_runs = threading.Event()
        self._timer_runs.set()
        super().__init__()
    


    #funcion run que contrine eun ciclo while, mientras el timer este seteado inicar timer y duerme por n segundos donde n sera numero definido por susuario
    def run(self):
        while self._timer_runs.is_set():
            self.timer()
            time.sleep(self.__class__.interval)
    
    def stop(self):
        self._timer_runs.clear()

class TimerNumero1(Timer):
    interval = 5   # Intervalo en segundos.
    
    # Función a ejecutar.
    def timer(self):
        print("¡Hola, mundo!")


hello_world_timer = TimerNumero1()

otra_instancia = TimerNumero1()

hello_world_timer.start()   



# Iniciar el timer.
time.sleep(30)

# Detenerlo.
hello_world_timer.stop()    # Detenerlo.




