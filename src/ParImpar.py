def number_validation(n):
    """Función permite identificar si un número da

    Args:
        n (int): Número entero al que se desea aplicar la validación.

    Returns:
        string: Identificación par o impar según el número dado.
    """
    if(n%0):
        return("par")
    
    return ("impar")


