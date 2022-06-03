import re

def mail():
    entrada = str(input("Ingrese un email, con un formato xxxxxx@xxxxx.com: "))
    if re.search('^[a-z0-9-._]+@[a-z0-9]+\.[a-z]+$', entrada):
        print(f"El mail: {entrada}, esta permitido")
        print("Gracias por usar este analizador")
    else:
        print(f'El mail: {entrada}, no esta permitido')
        print("Gracias por usar este analizador")