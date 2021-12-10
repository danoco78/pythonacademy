import os

def display_title_bar(title):
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')

    print("\t***************************")
    print("\t***  Ejercicios Python  ***")
    print("\t***************************")
    print("\t %s" %title)