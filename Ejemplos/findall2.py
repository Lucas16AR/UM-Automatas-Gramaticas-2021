# Programa para analizar fechas en un string

import re

def extraer_año(match):
    dia, mes, año = match
    return año

fechas_regex = re.compile('(0[1-9]|[12][0-9]|3[01])[-/]([0-9]|1[0-2])[-/]([12][0-9]{3})')

matches = fechas_regex.findall(
    'Los formatos 31-5-1981 y 01/12/2021 son considerados como fechas validas. La fecha 33/15/2021 no existe.'
)

print(matches)

for index, result in enumerate(matches):
    print(f'La fecha {index + 1} es en el año {extraer_año(result)}')