import re
import os

menu = True
while menu:
    
    opcion = str(input("""
    Ingrese 1 para (a|b)*
    Ingrese 2 para (aa|b)*(a|bb)*
    Ingrese 'salir' para finalizar  
Opción: """))

    if opcion == '1':
        ejer1 = True
        while ejer1:
            print("""

Ingrese una cadena compatible con la expresión: (a|b)*
Ingrese 'atras' para volver al menú.

            """)
            cadena = input("Cadena: ")
            if re.match(r'(a|b)*$', cadena):
                print("La cadena: ", cadena, " es válida.")
            
            elif str.lower(cadena) == str("atras"):
                ejer1 = False
            else:
                    print("La cadena: ", cadena, "no es valiida.")
                   
    elif opcion == '2':
        ejer2 = True
        while ejer2:
            print("""
Ingrese una cadena compatible con la expresión: (aa|b)*(a|bb)*
Ingrese \"atras\" para volver al menú.
            """)
            cadena = input("Cadena: ")
            if re.match(r'(aa|b)*(a|bb)*$', cadena):
                print("La cadena: ", cadena, " es válida.")
         
            elif str.lower(cadena) == str("atras"):
                    ejer2 = False
            else:
                print("La cadena: ", cadena, " no es válida.")
                    
    elif str.lower(opcion) == 'salir':
        os.system('cls')
        menu = False
    else: 
        print("\nOpción incorrecta")