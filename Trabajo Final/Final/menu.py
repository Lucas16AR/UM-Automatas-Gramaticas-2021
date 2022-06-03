'''
El programa debe tener un menú para poder obtener un informe con los siguientes 
filtros: 
1.  Listar todas las sesiones de un usuario mediante su ID. 
2.  Listar  los  inicios  de  sesión  en  un  usuario  en  un  periodo  de  tiempo 
determinado (permitir rango de fecha). 
3.  Tiempo total de la sesión de un usuario. 
4.  MAC de un usuario, para identificar si se conectó con un dispositivo o varios. 
5.  Listar los usuarios conectados a un AP, mediante la MAC del AP, en una 
determinada fecha o rango de fecha.
'''
'''
El archivo este compuesto por registros que tienen como 
@encabezado, @Id conexión, @usuario, @inicio y @fin de la conexión, @tiempo de la sesión, 
@cantidad de bytes recibidos y @enviados, @ap al que se conecta y @MAC del cliente. 
'''


import session_id
import session_time
import session_total
import mac_user
import ap_time

def menu():

    while True:

        print("""
    [1] Listar sesiones ordenados por ID
    [2] Listar inicios de sesion, por periodo de tiempo
    [3] Mostrar tiempo total de sesion
    [4] Mostrar MAC del Usuario
    [5] Listar usuarios conectados a una AP, por periodo de tiempo
    [6] Salir
    """)
        opc = int(input("Opción: "))
        
        if (opc == 1):
            session_id.sessionID()
            input("\nPresione enter para continuar ")

        elif (opc == 2):
            session_time.time()
            input("\nPresione enter para continuar ")

        elif (opc == 3):
            session_total.total()
            input("\nPresione enter para continuar ")

        elif (opc == 4):
            mac_user.user()
            input("\nPresione enter para continuar ")

        elif (opc == 5):
            ap_time.time()

        elif (opc == 6):
            exit(print("""Gracias por usar este programa
        Un trabajo realizado por Lucas Galdame"""))

        else:
            print("La opcion ingresada es incorrecta")

menu()