import sqlite3 as db
import sys

#Conexcion a la base de datos (de no estar creada la db la creará)
conn = db.connect('dbshop.db')

#Creación de un objeto llamado cursos a partir de la instancia conn.cursor
cursor = conn.cursor

def create_table():
    create_table = """ CREATE TABLE inventary (_id, name, price) """
    cursor.excute(create_table)

def data():
    print(">>>Datos actuales")
    for row in conn.execute("SELECT_id, name, price from inventary"):
        data_act = print(row)
    return data_act

def add_article():
    # Crear una lisra vacia
    products = []
    #Solicitamos los datos al usuario
    ident = input("Igrese el id del articulo, tome en cuenta el anterior id: ")
    product = input("Ingrese el nombre del producto: ")
    price= input("Ingrese el precio: ")
    #Agregamos los datos a nuestra lista
    products.append((ident,product,price))
    #Insertar la lista en la db
    cursor.executemany("INSERT INTO inventary (_id, name, price) VALUES (?, ?, ?)", products)

def changes():
    see_changes = int(input("¿Desea ver los cambios actualizados?\n1 >> Ver el registro modificado \n 2 >> Salir del programa\n>>>>"))
    if see_changes == 1:
        data()
    else:
        sys.exit()

print("----Registro de datos tienda departamental----")
print("----------Menu de opciones----------")
print("1 >> Ingresar un dato nuevo")
print("2 >> Revisar el registro")
opcion = int(input(">>>"))

if opcion == 1:
    #data()
    add_article()
    conn.commit()
    changes()
elif opcion == 2:
    data()
    new = int(input("¿Desea añadir un nuevo artículo?\n1 >> Añadir \n2 >> Salir del programa\n  >> "))
    if new == 1:
        add_article()
        conn.commit()
        changes()
    else:
        sys.exit()
print("Hasta la proxima")
conn.close()