# main.py
from include import clear_terminal, interface, menu_gf, read_int, read_float, read_string

clear_terminal()
interface()
choice = read_int()

if choice == 0:
    exit()
elif choice == 1:
    clear_terminal()
    menu_gf()
    input = read_int()
    if input == 0:
        clear_terminal()
        interface()