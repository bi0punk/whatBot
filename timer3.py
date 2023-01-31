import threading
import time
def timer(timer_runs):
    # (4) El código corre mientras el booleano sea verdadero.
    while timer_runs.is_set():
        print("¡Hola, mundo!")
        time.sleep(3)   # 3 segundos.
# (1) Creación del booleano que indica si el hilo secundario
# debe correr o no.
timer_runs = threading.Event()
# (2) Iniciarlo con el valor True.
timer_runs.set()
# (3) Pasarlo como argumento al timer para que pueda leerlo.
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()