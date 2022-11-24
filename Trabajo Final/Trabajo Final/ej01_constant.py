#Menu
MENU = '''
    |---------------------------------------------------------------|
    |                Bienvenidos, elija una opcion                  |
    |                                                               |
    | 1. Listar todas las sesiones por ID                           |
    | 2. Listar los inicios de session en un periodo de tiempo      |
    | 3. Tiempo total de la sesion de un usuario                    |
    | 4. Mac de un usuario                                          |
    | 5. Listar usuarios conectados a una AP                        |
    | 6. Salir                                                      |
    |---------------------------------------------------------------|

    '''

#ReGex
DATETIME_REGEX = ('''(0[1-9]|[12]\d|3[01])\/([1-9]|1[0-2])\/[12]\d{3} ([01][0-9]|2[0-3]):[0-5]\d:[0-5]\d''')

#Paths
PATH_TXT = "usuarios.txt"
FULLPATH_TXT = r"/home/lucas1608ar/Universidad/Automatas-Gramaticas/Automatas-Gramaticas-2021/Trabajo Final/usuarios.txt"
PATH_XLSX = "usuarios.xlsx"
FULLPATH_XLSX = r"/home/lucas1608ar/Universidad/Automatas-Gramaticas/Automatas-Gramaticas-2021/Trabajo Final/usuarios.xlsx"
PATH_XLSX_USER = r"/home/lucas1608ar/Universidad/Automatas-Gramaticas/Automatas-Gramaticas-2021/Trabajo Final/files/UserSession.xlsx"
PATH_MAC_USER = r"/home/lucas1608ar/Universidad/Automatas-Gramaticas/Automatas-Gramaticas-2021/Trabajo Final/files/MacUser.xlsx"

#Inputs
QUESTION_RET = "Volver a menu principal? (Y/N) "
INP_SHOW_DATA = "Ver informacion completa de las conexiones? (Y/N) "
UN_INP = "Nombre de Usuario: "
DATETIME_INPUT = "Ingrese la fecha, con el formato >> DD/MM/YYYY HH:MM:SS: "
DATETIME_INPUT_1 = "Ingrese la primer fecha con este formato >>> DD/MM/YYYY HH:MM:SS: "
DATETIME_INPUT_2 = "Ingrese la segunda fecha con este formato DD/MM/YYYY HH:MM:SS: "
DATETIME_RANGE_INPUT = "Quiere usar un rango de tiempo para buscar? (Y/N) "
MAC_USER_INP = "Ingrese la MAC del Usuario para analizar: "
AP_INPUT = "Ingrese la MAC AP para buscar: "

#Mensajes
RETURN_MENU = "Menu principal"
SEARCHING_DATA = "Buscando"
LOADING_DATA = "Cargando"
LOAD_DATA = "Carga correcta"
USER_NOT_FOUND = "No existe el usuario"
MAC_NOT_FOUND = "No existe la MAC"
WRONG_DT_1 = "Valores ingresados en formato incorrecto"
WRONG_DT_2 = "Valores ingresados en formato incorrecto"
INP_FB = "Opcion elegida: "
INFO_HELP = "Testeo"
VALIDATE_CHECKING = "Validando"
VALIDATE_CORRECT = "Datos validados"
DATETIME_RANGE_MSG = "Ingrese un rango de fechas"
DT_RANGE_MSG = "Setee un rango de fechas"
TO_EXCEL = "Para mas detalles, vea el excel"
CHECK_XLSX = "Para mas detalles, vea el excel 'Usuarios WiFi'"

#Operaciones de string
JUMP_LINE = "\n"

#Salida
EXIT = "Saliendo. Hasta Luego"