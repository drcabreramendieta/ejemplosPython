from threading import Thread
from time import sleep

def sumador(monto, repeticiones):
    global contador
    for _ in range(repeticiones):
        tmp = contador
        sleep(0)
        tmp = tmp + monto
        sleep(0)
        contador = tmp

def restador(monto, repeticiones):
    global contador
    for _ in range(repeticiones):
        tmp = contador
        sleep(0)
        tmp = tmp - monto
        sleep(0)
        contador = tmp


contador = 0
hilo_sumador = Thread(target=sumador, args=(100, 1000000))
hilo_restador = Thread(target=restador, args=(100, 1000000))
hilo_sumador.start()
hilo_restador.start()
hilo_sumador.join()
hilo_restador.join()
print("El valor de contador es:", contador)