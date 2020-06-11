class Triangulo:
    """Se crea la clase triangulo"""
    def __init__(self):
        """Esta dunción pedira tres datos que son las medidas y las almacenará"""
        self.lado_1 = int(input("Escriba la medida del primer lado: "))
        self.lado_2 = int(input("Escriba la medida del segundo lado: "))
        self.lado_3 = int(input("Escrina la medida del tercer lado: "))

    def imprimir(self):
        """Imprime en pantalla la medida de los lados del triangulo"""
        print("\nLos lados del triangulo tienen las siguientes medidas")
        print(f" >El lado uno mide {self.lado_1}u")
        print(f" >El lado uno mide {self.lado_2}u")
        print(f" >El lado uno mide {self.lado_3}u")

    def tipo(self):
        """Evalua la medida de los lados para determinar el tipo de triangulo. 
        Sabemos que los equilateros tienen la misma medida en todos sus lados, 
        los isósceles tienen dos lados iguales y uno diferente, y los escalenos 
        tienen medidas diferentes en todos sus lados"""
        if self.lado_1 == self.lado_2 and self.lado_2 == self.lado_3:
            print("\nEste triangulo es equilátero")
        elif self.lado_1 != self.lado_2 and self.lado_2 != self.lado_3 and self.lado_1 != self.lado_3:
            print("\nEste triangulo es escaleno")
        else:
            print("\nEste triangulo es isósceles")

pizza = Triangulo()
pizza.imprimir()
pizza. tipo()