def sumar(numero_1,numero_2):
    """
    Suma de dos numeros
    Parametros:
    numero_1, numero_2
    Return:
    La suma de numero_1+numero_2
    """
    return numero_1 + numero_2

def restar(numero_1,numero_2):
    """
    resta de dos numeros
    Parametros:
    numero_1, numero_2
    Return:
    La resta de numero_1-numero_2
    """
    return numero_1 - numero_2

def multiplicar(numero_1,numero_2):
    """
    Multiplicacion de dos numeros
    Parametros:
    numero_1, numero_2
    Return:
    La multiplicacion de numero_1*numero_2
    """
    return numero_1 * numero_2

def division(numero_1,numero_2):
    """
    Division de dos numeros
    Parametros:
    numero_1, numero_2
    Return:
    La division de numero_1/numero_2
    """
    if numero_2 != 0:
        return numero_1 / numero_2
    raise ZeroDivisionError("ERROR: División entre 0 no permitida")