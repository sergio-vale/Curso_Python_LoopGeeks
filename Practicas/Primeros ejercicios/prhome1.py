total = 0 #Almacena la cantidad de dinero gastado
niños = 0
estudiante = 0
adulto = 0
adulto_mayor = 0 # Servirá para determinar el número de personas que han comprado en las diferentes categorías
numero_cliente = 1 #Fuinción estética para saber el numero del que se anota la edad

while True:#Pide el número de boletos a comprar
    try:
        cantidad_clientes = int(input("Bienvenido a Cinemex \n#Sin ti la magia del cine no es igual\n¿Cuántos boletos desea? "))
        if cantidad_clientes <= 0: #Para evitar que se de la situación de comprar 0 boletos se usa la función if
            print("Número de boletos inválido\n")
        else:
            break
    except ValueError as e: #Mandará un mensaje de error cuando el valor que se introduzca no sea un npumero
        print("Valor inválido\n")
print()

while cantidad_clientes > 0: #En este bloque se recopilan los datos de los clientes para determinar el precio al que se le venderá el boleto
    while True:#Pide la edad, su utiliza ehile para que en caso de no escribir un número 
        try:
            edad = int(input(f"Escriba la edad del cliente numero {numero_cliente}: "))
            break
        except ValueError as e:
            print("Solo valores numericos enteros\n")
    if edad < 0:#Rregula que no se escriban números negativos, que no se aplican a edades
        print("Edad invalidad\n")
    elif 3 <= edad <= 14:#Determina si el cliente es niño
        total = total + 25
        niños = niños + 1
        cantidad_clientes = cantidad_clientes - 1
        numero_cliente = numero_cliente + 1
    elif 15 <= edad <= 17:#Determina si el cliente entra en la categoría estudiante
        total = total + 32
        estudiante = estudiante + 1
        cantidad_clientes = cantidad_clientes - 1
        numero_cliente = numero_cliente + 1
    elif 18 <= edad <= 21:#En este rango existen dos posibles categorías, estudiante o adulto
        while True:#Determina si el cliente es estudiante
            estudia = input("¿Usted se encuentra estudiando actualmente?\n(S/N) ")
            estudia = estudia.upper()
            if estudia == 'S':
                total = total + 32
                estudiante = estudiante + 1
                cantidad_clientes = cantidad_clientes - 1
                numero_cliente = numero_cliente + 1
                break
            elif estudia == 'N':
                total = total + 43
                adulto = adulto + 1
                cantidad_clientes = cantidad_clientes - 1
                numero_cliente = numero_cliente + 1
                break
            else:
                print("Solo responde con 'S' o 'No'")
    elif 22 <= edad <= 64:#Determina si es adulto
        total = total + 30
        adulto = adulto + 1
        cantidad_clientes = cantidad_clientes - 1
        numero_cliente = numero_cliente + 1
    elif edad >= 65:#A partie de esta edad se le considera adulto mayor
        total = total + 30
        adulto_mayor = adulto_mayor + 1
        cantidad_clientes = cantidad_clientes - 1
        numero_cliente = numero_cliente + 1
    else:
        print("Aún no tiene la edad adecuada para entrar al cine\n")

print("\nUsted ha comprado\n")#Parte final del programa que da el total de compra
if niños != 0:#Estos if son para que solo se imprima en panttalla el total de categorías donde se haya comprado
    if niños == 1:
        print(f"{niños} Boleto para niño X $25")
    else:
        print(f"{niños} Boletos para niños X $25")
if adulto != 0:
    if adulto == 1:
        print(f"{adulto} Boleto para adulto X $43")
    else:
        print(f"{adulto} Boletos para adultos X $43")
if estudiante != 0:
    if estudiante == 1:
        print(f"{estudiante} Boleto para estudiante X $32")
    else:
        print(f"{estudiante} Boletos para estudiantes X $32")
if adulto_mayor != 0:
    if adulto_mayor == 1:
        print(f"{adulto_mayor} Boleto para adulto mayor X 30")
    else:
        print(f"{adulto_mayor} Boletos para adultos mayores X 30")
print(f"\nSu total es de ${total}")#Total de compra
print("\nGracias por su compra\n#Sin ti la magia del cine no es igual")#Despedida