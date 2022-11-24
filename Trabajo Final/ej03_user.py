import re
import ej01_constant as cs
import time
import pandas as pd
import datetime

class User:

    def operate_xlsx_file(self):
        df = pd.read_excel(cs.PATH_XLSX) # lee el archivo
        df = df.dropna()
        return df

    def list_session_id(self):
        print(cs.JUMP_LINE)
        inp = input(cs.UN_INP) # ingresa el usuario
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        df = self.operate_xlsx_file() # llama a la funcion
        if inp in df.values:
            # separa estas dos columnas con loc
            df_loc = df.loc[:,["ID Conexion unico", "Usuario"]]
            # busca un usuario en esa columna y lo separa con loc
            user_df = df_loc[df_loc["Usuario"].str.contains(inp)]
            print(cs.JUMP_LINE)
            print(user_df)
            user_df.to_excel(cs.PATH_XLSX_USER) # guarda los datos en un excel
            print(cs.JUMP_LINE, cs.TO_EXCEL)
        else:
            print(cs.JUMP_LINE, cs.USER_NOT_FOUND)
        time.sleep(0.1)

    def print_xlsx(self):
        df = self.operate_xlsx_file()
        print(df)

    def mac_user_devices(self):
        print(cs.JUMP_LINE)
        inp = input(cs.MAC_USER_INP)
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        df = self.operate_xlsx_file()
        if inp in df.values:
            df_loc = df.loc[:,["MAC Cliente", "Usuario"]]
            macs = df_loc[df_loc["MAC Cliente"].isin([inp])]
            mac_user = macs.groupby(['MAC Cliente', 'Usuario']).size().reset_index(name='Cantidad de Veces Utilizada')
            print(cs.JUMP_LINE)
            print(mac_user)
            mac_user.to_excel(cs.PATH_MAC_USER)
            print(cs.JUMP_LINE, cs.TO_EXCEL)
        else:
            print(cs.JUMP_LINE)
            print(cs.MAC_NOT_FOUND)
        time.sleep(0.1)

    def datetime_search(self):
        print(cs.JUMP_LINE)
        # regex datetime
        regex = re.compile(cs.DATETIME_REGEX)
        print(cs.DT_RANGE_MSG)
        time.sleep(2)
        print(cs.JUMP_LINE)
        date_1 = str(input(cs.DATETIME_INPUT_1)) # ingreso primera fecha
        validation_date = regex.fullmatch(date_1) # valido con fullmatch
        print(cs.JUMP_LINE)
        print(cs.VALIDATE_CHECKING)
        time.sleep(2)
        if validation_date: # validacion correcta
            print(cs.JUMP_LINE, cs.VALIDATE_CORRECT, cs.JUMP_LINE)
            date_2 = str(input(cs.DATETIME_INPUT_2)) # ingreso segunda fecha
            validation_date_2 = regex.fullmatch(date_2) # valido con fullmatch
            print(cs.JUMP_LINE)
            print(cs.VALIDATE_CHECKING)
            time.sleep(2)
            if validation_date_2: # segunda validacion correcta
                print(cs.JUMP_LINE, cs.VALIDATE_CORRECT, cs.JUMP_LINE)
                usr_input = input(cs.UN_INP) # ingreso usuario
                print(cs.JUMP_LINE, cs.SEARCHING_DATA)
                df = self.operate_xlsx_file() # llamo a la funcion para leer el archivo
                if usr_input in df.values and date_1 < date_2: # verifico si existe el usuario y si el rango de fechas es correcto
                    df_loc = df.reindex(["Usuario","Inicio de Conexi¢n"]) # separo estas dos columnas con loc
                    usr_df = df_loc[df_loc["Usuario"].isin([usr_input])] # busco mi usuario ingresado
                    date_df = usr_df.loc[df["Inicio de Conexi¢n"].between(date_1, date_2)] # busco entre mi rango de fechas
                    print(cs.JUMP_LINE)
                    print(date_df)
                    date_df.to_excel(cs.PATH_DATE_USR)
                    print(cs.JUMP_LINE, cs.TO_EXCEL)
                else: # no match
                    print(cs.JUMP_LINE, cs.NO_MATCH)
            else:
                print(cs.JUMP_LINE, cs.WRONG_DT_2)
        else:
            print(cs.JUMP_LINE, cs.WRONG_DT_1)
        time.sleep(0.1)
        
    def total_session_time(self):
        print(cs.JUMP_LINE)
        inp = input(cs.UN_INP) # ingresa el usuario
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        df = self.operate_xlsx_file() # llama a la funcion
        if inp in df.values:
            # separa estas dos columnas con loc
            df_loc = df.loc[:,["Usuario", "Session Time"]]
            # busca un usuario en esa columna y lo separa con loc
            user_df = df_loc[df_loc["Usuario"].str.contains(inp)]
            total_time_df = user_df['Session Time'].sum()
            print(cs.JUMP_LINE)
            total_time = str(datetime.timedelta(seconds=total_time_df))
            print("El tiempo total de este usuario es:", total_time)
        else:
            print(cs.JUMP_LINE, cs.USER_NOT_FOUND)
        time.sleep(0.1)
    
    def mac_ap(self):
        print(cs.JUMP_LINE)
        # regex datetime
        regex = re.compile(cs.DATETIME_REGEX)
        opt_inp = input(cs.DATETIME_RANGE_INPUT)
        if opt_inp.isupper():
            opt_inp = opt_inp.lower()
        if opt_inp == 'n':
            print(cs.JUMP_LINE)
            time.sleep(0.1)
            print(cs.EXIT)
            time.sleep(0.1)
            exit()
        if opt_inp == "y":
            print(cs.JUMP_LINE, cs.DT_RANGE_MSG)
            time.sleep(2)
            print(cs.JUMP_LINE)
            date_1 = str(input(cs.DATETIME_INPUT_1)) # ingreso primera fecha
            validation_date = regex.fullmatch(date_1) # valido con fullmatch
            print(cs.JUMP_LINE)
            print(cs.VALIDATE_CHECKING)
            time.sleep(2)
        if opt_inp != 'y':
            time.sleep(0.1)
            exit
        if opt_inp != 'n':
            time.sleep(0.1)
            exit
            if validation_date: # validacion correcta
                print(cs.JUMP_LINE, cs.VALIDATE_CORRECT, cs.JUMP_LINE)
                date_2 = str(input(cs.DATETIME_INPUT_2)) # ingreso segunda fecha
                validation_date_2 = regex.fullmatch(date_2) # valido con fullmatch
                print(cs.JUMP_LINE)
                print(cs.VALIDATE_CHECKING)
                time.sleep(2)
                if validation_date_2: # segunda validacion correcta
                    print(cs.JUMP_LINE, cs.VALIDATE_CORRECT, cs.JUMP_LINE)
                    mac_ap_input = str(input(cs.AP_INPUT))
                    print(cs.JUMP_LINE,cs.SEARCHING_DATA, cs.JUMP_LINE)
                    df = self.operate_xlsx_file()
                    if mac_ap_input in df.values and date_1 < date_2:
                        df_loc = df.loc[:,["MAC AP", "Usuario", "Inicio de Conexi¢n", "Fin de Conexio"]]
                        df_mac_date = df_loc[(df_loc["MAC AP"].isin([mac_ap_input])) & (df_loc["Inicio de Conexi¢n"].between(date_1, date_2))]
                        print(df_mac_date)
                        df_mac_date.to_excel(cs.PATH_MAC_DT)
                        print(cs.JUMP_LINE, cs.TO_EXCEL)
                    else:
                        print(cs.JUMP_LINE, cs.NO_MATCH)
                else:
                    print(cs.JUMP_LINE, cs.WRONG_DT_2)
            else:
                print(cs.JUMP_LINE, cs.WRONG_DT_1)
        else:
            print(cs.JUMP_LINE)
            inp = input(cs.DATETIME_INPUT)
            validation_date = regex.fullmatch(inp) # valido con fullmatch
            print(cs.JUMP_LINE)
            print(cs.VALIDATE_CHECKING)
            time.sleep(2)
            if validation_date:
                print(cs.JUMP_LINE, cs.VALIDATE_CORRECT, cs.JUMP_LINE)
                inp = inp.split("  ")
                inp.append("  ")
                inp.append("23:59:00")
                date_1 = inp[0] + inp[2] + inp[1]
                date_2 = inp[0] + inp[2] + inp[3]
                mac_ap_input = str(input(cs.AP_INPUT))
                print(cs.JUMP_LINE,cs.SEARCHING_DATA, cs.JUMP_LINE)
                df = self.operate_xlsx_file()
                if mac_ap_input in df.values and date_1 < date_2:
                    df_loc = df.loc[:,["MAC AP", "Usuario", "Inicio de Conexi¢n", "Fin de Conexio"]]
                    df_mac_date = df_loc[(df_loc["MAC AP"].isin([mac_ap_input])) & (df_loc["Inicio de Conexi¢n"].between(date_1, date_2))]
                    print(df_mac_date)
                    df_mac_date.to_excel(cs.PATH_MAC_DT)
                    print(cs.JUMP_LINE, cs.TO_EXCEL)
                else:
                    print(cs.JUMP_LINE, cs.NO_MATCH)
            else:
                print(cs.JUMP_LINE, cs.WRONG_DT_1)
        time.sleep(0.1)