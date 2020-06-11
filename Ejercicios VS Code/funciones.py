def suma(a,b):
    y = a+b
    return y

def resta(a,b):
    y = a-b
    return y

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

resultado = suma(a,b)

print(f"La suma de {a} + {b} es igual a {resultado}")
print(f"La resta de {a} + {b} es igual a {resta(a,b)}")
#def mensaje():
#    print("Hola")

#entrada = input("Llame su funcion: ")

#if entrada == 'saludosaludo':
#    mensaje()