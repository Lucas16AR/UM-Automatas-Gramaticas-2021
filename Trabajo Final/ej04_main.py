import clear
import ej01_constant as cs
import ej02_functions as ft
import ej03_user as us

def main():
    ej03_user = us.User()
    while True:
        clear.clear()
        print(cs.MENU)
        inp = input("")
        inp = inp.lower()
        if inp == '1':
            ej03_user.list_session_id()
            ft.return_menu()
        elif inp == '2':
            ej03_user.datetime_search()
            ft.return_menu()
        elif inp == '3':
            ej03_user.total_session_time()
            ft.return_menu()
        elif inp == '4':
            ej03_user.mac_user_devices()
            ft.return_menu()
        elif inp == '5':
            ej03_user.mac_ap()
            ft.return_menu()
        elif inp == '6':
            ft.exit_program()
            break
        elif inp == 'e':
            ft.exit_program()
            break
        else:
            ft.error_menu()

if __name__ == '__main__':
    main()