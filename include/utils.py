import os
import platform

def clear_terminal():
    system = platform.system()
    if(system == "Windows"):
        os.system("cls")
    else:
        os.system("clear")
