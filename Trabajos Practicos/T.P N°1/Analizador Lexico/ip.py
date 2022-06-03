import re

def direccion():
    entrada = str(input("Ingrese la dirección IP, con un formato XXX.XXX.XXX.XXX. Recuerde que las direcciones IPv4 van desde 0.0.0.0 hasta 255.255.255.255: "))
    if re.search("^([0-1]?[0-9]?[0-9]|[0-2][0-4][0-9]|[0-2][0-5][0-5])\."
            "([0-1]?[0-9]?[0-9]|[0-2][0-4][0-9]|[0-2][0-5][0-5])\."
            "([0-1]?[0-9]?[0-9]|[0-2][0-4][0-9]|[0-2][0-5][0-5])\."
            "([0-1]?[0-9]?[0-9]|[0-2][0-4][0-9]|[0-2][0-5][0-5])$", entrada):
        print(f"La Dirección IP: {entrada}, esta permitido")
        print("Gracias por usar este analizador")
    else:
        print(f"Dirección IP: {entrada}, no permitida")
        print("Gracias por usar este analizador")