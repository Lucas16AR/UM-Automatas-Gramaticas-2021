# Programa para detectar si un string contiene la letra 'F'

import re

def contiene_s(cadena_a_evaluar):
    patron = 'F'

    if re.search(patron, cadena_a_evaluar):
        print(f'La cadena "{cadena_a_evaluar}" contiene el patron "{patron}"')
    else:
        print(f'La cadena "{cadena_a_evaluar}" NO contiene el patron "{patron}"')


cadena_1 = 'Universidad de Mendoza'
cadena_2 = 'Facultad de Ingeniería'
cadena_3 = 'FFFFFFFF'

contiene_s(cadena_1)
contiene_s(cadena_2)
contiene_s(cadena_3)