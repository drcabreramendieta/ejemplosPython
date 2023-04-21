from threading import Thread
import time

def hilo():
    for i in range(100):
        print(str(i)+": Se ejecuta el hilo...")
        time.sleep(1)

obj_hilo = Thread(target=hilo)
obj_hilo.start() # Inicia el hilo
obj_hilo.join() # Espera la ejecución del hilo