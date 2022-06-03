#[1] Listar sesiones ordenados por ID

import pandas as pd

def sessionID():
    
    archivo_excel = pd.read_excel(r'/home/lucas1608ar/Universidad/Automatas-Gramaticas/Trabajo Final/Usuarios WiFi.xlsx')
    print(archivo_excel.columns)
    values = archivo_excel['ID Conexion unico'].values

    print(values)

    columnas = ['ID Conexion unico']
    df_seleccionados = archivo_excel[columnas]

    print(df_seleccionados)