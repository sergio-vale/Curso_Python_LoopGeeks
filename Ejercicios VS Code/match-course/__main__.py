import functions_math as math

def menu():
    """Menú de una calcuadora con operaciones básicas"""
    print("Bienvenido a la calculadora en consola, a continuación le muesto el menú de opciones")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")

def main():
    """Operaciones a realizar por la calculadora"""
    while True:
        while True:
            menu()
            try:
                opcion = int(input("Escoja una opcion del menu: "))
                break
            except ValueError as e:
                print("ERROR: Valor invalido")
        print()
        
        if opcion == 0:
            break
        if 1 <= opcion <= 4:
            while True:
                try:
                    numero_1 = float(input("Digite el número 1: "))
                    break
                except ValueError as e:
                    print("Error: Valor inválido")
            while True:
                try:
                    numero_2 = float(input("Digite el número 2: "))
                    break
                except ValueError as e:
                    print("Error: Valor inválido")
                    
        if opcion == 1:
            resultado = math.sumar(numero_1, numero_2)
            print(f"{numero_1} + {numero_2} = {resultado}.")
        elif opcion == 2:
            resultado = math.restar(numero_1, numero_2)
            print(f"{numero_1} - {numero_2} = {resultado}.")
        elif opcion == 3:
            resultado = math.multiplicar(numero_1, numero_2)
            print(f"{numero_1} * {numero_2} = {resultado}.")
        elif opcion == 4:
            try:
                resultado = math.division(numero_1, numero_2)
                print(f"{numero_1} / {numero_2} = {resultado}.")
            except ZeroDivisionError as e:
                print(e)
        print("\n")
    
    print("\n")
    print("Gracias por usarme")

if __name__ == '__main__':
    main()