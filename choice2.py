def bigger_number():
    print("Ingresa los números que deseas evaluar")
    number1 = input("digita el primer número que deseas evaluar...:")
    number2 = input("digita el segundo número que deseas evaluar...:")
    try:
        if(int(number1) > int(number2)):
            print(f"el número {number1} es el mayor")
        elif(int(number2) > int(number1)):
            print(f"el número {number2} es el mayor")
        else:
            print("ambos números son iguales")

        input("Presiona enter para continuar")
        return ""
    except:
        print("el valor que ingresaste no es un número, hasta la proxima")
        input("Presiona enter para continuar")
        return ""