class Persona:
    #Se crea la clase persona
    def __init__(self):
        """Función que se iniciara al crear un objeto de la clase persona 
        que almacenará dos valores, edad y nombre"""
        self.nombre = input("Escriba el nombre de la persona: ")
        self.edad = int(input("Escriba la edad de la persona: "))

    def imprimir(self):
        """Función que imprime en pantalla la edad de la persona"""
        print(f"\n{self.nombre} tiene {self.edad} años")

    def etapa(self):
        """Funcion que lee la edad evalua el numeor introducido en edad
        y si es igual o menor a 17 conluye que el objeto de la clase persona es menor de edad, 
        si no es así, será mayor de edad"""
        if self.edad <= 17:
            print(f"\n{self.nombre} es menor de edad")
        else:
            print(f"\n{self.nombre} es mayor de edad")

inge = Persona()
inge.imprimir()
inge.etapa()