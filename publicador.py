from paho.mqtt import client as cliente_mqtt
import time

broker = '172.28.127.134'
puerto = 1883
tema = "tema/test"

cliente = cliente_mqtt.Client()

def conectado(cliente, datos, flags, rc):
    print("Ingresa")
    if rc == 0:
        print("Conectado")
    else:
        print("Fallo en la conexión, ", rc)

cliente.on_connect = conectado
cliente.connect(broker,puerto)
cliente.loop_start()

cliente.publish(tema,"Prueba SE1v2")
cliente.disconnect()
time.sleep(1)