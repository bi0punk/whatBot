import threading
import time
def timer(timer_runs):
    while timer_runs.is_set():
        print("¡Hola, mundo!")
        time.sleep(3)   # 3 segundos.
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()
# Esperar 10 segundos y luego detener el timer.
time.sleep(10)
timer_runs.clear()
print("¡El timer ha sido detenido!")



