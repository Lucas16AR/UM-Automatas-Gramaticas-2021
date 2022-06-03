import re
    
def contra():
    entrada = str(input("""Por favor ingrese una contraseña que cumpla las siguientes condiciones:
    - Que comience con una letra mayúscula
    - Que contenga al menos una letra minúscula
    - Que contenga al menos dos números
    - Que contenga entre 8 y 16 caracteres
Ingrese una contraseña: """))
    if re.search(r'(?=.*[a-z])(?=.*^[A-Z])(?=.+\d{2})(?=.+\d{2})([A-Za-z]|[^ ]){8,16}$', entrada):
        print(f"La contraseña: {entrada}, esta permitida")
        print("Gracias por usar este analizador")
    else:
        print(f"La contraseña: {entrada}, no esta permitida")
        print("Gracias por usar este analizador")