# Bucle w
import math

numero = int(input("Ingrese un numero: "))

while numero<0:
    print("Error no puede ser un numero negativo")
    numero = int(input("Escriba un numero: "))

print(f"La raiz cuadrada es {(math.sqrt(numero))}")