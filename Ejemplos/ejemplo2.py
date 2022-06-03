import time                                # Librería o Módulo implementado para llevar el tiempo del semáforo
from fysom import Fysom                    # Libreria o Módulo que contiene las funciones para la máquina

semaforo = Fysom({ 'initial': 'verde',     # Estado inicial de la máquina.
             'events': [                   # Lista de transiciones (eventos) de la máquina
                  {'name': 'precaucion', 'src': 'verde', 'dst': 'amarillo'}, 
                  {'name': 'stop', 'src': 'amarillo', 'dst': 'rojo'},
                  {'name': 'go', 'src': 'rojo', 'dst': 'verde'} ] })

while True:
  if semaforo.current == "verde":  # 'semaforo.current' almacena el estado actual de la máquina
    print(semaforo.current)
    time.sleep(15)                 # 'time.sleep(n)' espera 'n' segundos para continuar con la ejecución del programa
    semaforo.precaucion()
  if semaforo.current == "amarillo":
    print(semaforo.current)
    time.sleep(5)
    semaforo.stop()
  if semaforo.current == "rojo":
    print(semaforo.current)
    time.sleep(10)
    semaforo.go()