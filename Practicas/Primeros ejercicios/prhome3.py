usuario = 'Serg_2029' #Usuario por defecto
usuario_i = ' '#Usuario que se introducirá y debe ser idéntico a constante 'usuario'
clave = '019283'#Contraseña por defecto
clave_i = ' '#Variable que se introducirá y debe ser idéntico a 'clave'

while True:
    while True:
        #Bucle de login
        usuario_i = input("Introduzca su nombre de usuario: ")
        clave_i = input("Introduzca la clave: ")
        if usuario != usuario_i and clave != clave_i:#Mensajes de error en caso de que alguna variable sea diferente a las constantes
            print("El usuario y la contraseña introducidos son incorrectos\n")
        elif usuario_i != usuario:
            print("El ususario introducido es incorrecto\n")
        elif clave != clave_i:
            print("La contraseña intrducida es incorrecta\n")
        else:
            print('\nContraseña correcta, sesión iniciada\n')#Cuando todos están correctos se rompe el bucle de login
            break
    print("¿Desa cambiar la contraseña?")
    while True: 
        #Bloque para cambiar la contraseña
        n_contra = input("(Presione 'Y' para crear una nueva contraseña o 'N' para continuar)\n").upper()
        if n_contra == 'Y':
            clave = input("Escriba la nueva contraseña:  ")
            print(f"La nueva contraseña es {clave}\n")
            print('\nEs necesario iniciar sesión nuevamente\n')
            break
        elif n_contra == 'N':
            print()
            break
        else:
            print()
    if n_contra == 'Y':
        #Si el usuario Cambió la contraseña n_contra 
        print()
    else:
        break

#PLUS JUEGO
while True:
    print("><><><><TIME TO PLAY><><><><")
    print("   <<   A) Chiste      >>\n   <<   B)Adivinanza   >>\n   <<   C)Acertijo     >>")
    juego = input("Escoja su juego o pulse cualquier otra tecla para salir para salir: ").upper()
    if juego == 'A':
        print("\nHabía un perro llamado pegamento se cayó y se pegó\n")
    elif juego == 'B':
        print("\nAdivina adivinador que tiene el rey en la pansa\n")
        respuesta = input("A) El ombligo\nB) Tripas\n").upper()
        if respuesta == 'A':
            print("Excelente\n")
        elif respuesta == 'B':
            print("Incorrecto\n")
        else:
            print("Sólo A o B")
    elif juego == 'C':
        print("\n¿Que se puede ver con los ojos cerrados?\n")
        respuesta_2= input("A) Nada\nB) La oscuridad\n").upper()
        if respuesta_2 == 'A':
            print("Incorrecto\n")
        elif respuesta_2 == 'B':
            print("Excelente\n")
        else:
            print("Solo A y B\n")
    else:
        print("\nGracias por su visita\n")
        break