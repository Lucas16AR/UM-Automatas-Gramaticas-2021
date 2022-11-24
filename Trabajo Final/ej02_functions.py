import time
import ej01_constant as cs
from ej04_main import *

def help_function():
    print(cs.JUMP_LINE)
    time.sleep(0.1)
    print(cs.HELP)
    time.sleep(0.1)
    print(cs.INFO_HELP)
    inp = input(cs.INP_SHOW_DATA)
    if inp.isupper():
        inp = inp.lower()
    if inp == 'y':
        print(cs.JUMP_LINE)
        time.sleep(0.1)
        print(cs.LOADING_DATA)
        print(cs.JUMP_LINE)
        user = cs.User()
        user.print_xlsx()
        time.sleep(0.1)
        print(cs.JUMP_LINE)
        print(cs.LOAD_DATA)
        time.sleep(0.1)
        print(cs.JUMP_LINE, cs.CHECK_XLSX)
        time.sleep(0.1)
    elif inp == 'n':
        time.sleep(0.1)
    else:
        error_menu()

def return_menu():
    inp = input(cs.QUESTION_RET)
    if inp.isupper():
        inp = inp.lower()
    if inp == 'y':
        print(cs.JUMP_LINE)
        time.sleep(0.1)
        print(cs.RETURN_MENU)
        time.sleep(0.1)
    elif inp == 'n':
        exit_program()
        exit()
    else:
        error_menu()

def exit_program():
    print(cs.JUMP_LINE)
    time.sleep(0.1)
    print(cs.EXIT)
    time.sleep(0.1)

def error_menu():
    print(cs.JUMP_LINE)
    print(cs.ERR)
    time.sleep(0.1)
    print(cs.JUMP_LINE)
    print(cs.RETURN_MENU)
    time.sleep(0.1)