import os
import platform

def clear_terminal():
    system = platform.system()
    if(system == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

def interface():
    print('''
    __________________________________________
          
              /$$$$$$   /$$$$$$  /$$$$$$$$
             /$$__  $$ /$$__  $$| $$_____/
            | $$  \\__/| $$  \\__/| $$      
            |  $$$$$$ | $$ /$$$$| $$$$$   
             \\____  $$| $$|_  $$| $$__/   
             /$$  \\ $$| $$  \\ $$| $$      
            |  $$$$$$/|  $$$$$$/| $$      
            \\______/  \\______/ |__/            
    __________________________________________
                1 - Gastos Fixos
                2 - Calcular PID
                3 - MOSTRE-ME STATISCAS!!!
                0 - Sair
    ''')

def menu_gf():
    print('''
    __________________________________________
          
    Bem-vindo ao gerenciamento de gastos fixos
    __________________________________________
        1 - Adicionar gasto fixo
        2 - Consultar tabela de gastos
        3 - Remover gasto fixo
        0 - Sair
    ''')

def read_int():
    x = int(input(''))
    return x

def read_float():
    x = float(input(''))
    return x

def read_string():
    x = input('')
    return x
