# Programa para extraer las vocales de un string

import re

def extraer_vocales(cadena) -> bool:
    vocales_regex = re.compile('[aeiouAEIOU]')
    return vocales_regex.findall(cadena)

resultado = extraer_vocales('NO existen grupos')

print(resultado)