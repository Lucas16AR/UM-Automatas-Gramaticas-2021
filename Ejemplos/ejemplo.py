import pandas as pd

def session_id():
    
    archivo_excel = pd.read_excel(r'/home/lucas1608ar/Universidad/Automatas-Gramaticas/Ejemplos/ejemplo.ods')
    print(archivo_excel.columns)
    values = archivo_excel['Identificador'].values

    print(values)

    columnas = ['Identificador', 'Nombre', 'Apellidos']
    df_seleccionados = archivo_excel[columnas]

    print(df_seleccionados)

session_id()