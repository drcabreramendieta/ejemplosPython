from threading import Thread

def hilo():
    print("Se ejecuta el hilo...")

obj_hilo = Thread(target=hilo)
obj_hilo.start() # Inicia el hilo
obj_hilo.join() # Espera la ejecución del hilo