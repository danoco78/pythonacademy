# -*- coding: utf-8 -*-
import os
from choice1 import par_impar
from choice2 import bigger_number
from choice3 import pair_numbers

def print_menu():
    os.system("cls")
    print("Que programa deseas ejecutar?")
    print("------------------------------")
    print("1. Verificar que un número es par o impar")
    print("2. Que número es mayor")
    print("3. Los números pares desde 0 hasta un valor dado")
    print("4. Suma acumulada de números de una lista")
    print("5. Tabla de multiplicar de un número dado")
    print("6. Busqueda de palabras palindromas en una lista dada")
    print("7. identificar una lista con valores duplicados")
    print("Q - Salir del programa")
    print("------------------------------")
#    print("\n")


choice = ""
while choice.upper() != "Q":
    print_menu()
    choice = input("Por favor elije tu opción ")
    if(choice == "1"):
        choice = par_impar()
    elif(choice == "2"):
        choice = bigger_number()
    elif(choice == "3"):
        choice = pair_numbers()
