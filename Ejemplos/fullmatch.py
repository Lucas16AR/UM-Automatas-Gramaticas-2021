# Programa para detectar si un string contiene solo ceros y/o unos

import re

def es_binario(cadena_a_evaluar):
    expresion_regular = '(0|1)+'

    if re.fullmatch(expresion_regular, cadena_a_evaluar):
        print(f'La cadena "{cadena_a_evaluar}" contiene solo ceros y unos')
    else:
        print(f'La cadena "{cadena_a_evaluar}" contiene otros caracteres')
    

    
cadena_1 = '00000000'
cadena_2 = '11111111'
cadena_3 = '10011101'
cadena_4 = '1101015101'

es_binario(cadena_1)
es_binario(cadena_2)
es_binario(cadena_3)
es_binario(cadena_4)