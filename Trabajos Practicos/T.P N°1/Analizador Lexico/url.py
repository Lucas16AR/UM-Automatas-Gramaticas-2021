import re

def dir():
    entrada = str(input("Ingrese una URL, con un formato http-s://www.......com: "))
    if re.search('^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-z]+$', entrada):
        print(f"La URL: {entrada}, esta permitida")
        print("Gracias por usar este analizador")
    else:
        print(f"La URL: {entrada}, no esta permitida")
        print("Gracias por usar este analizador")