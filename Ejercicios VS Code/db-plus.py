# Importacion del módulo sqlite 3 como db
import sqlite3 as db

#conexión a la base de datos
conn = db.connect("firstdb.db")

# Creación de un objeto llamado cursor a partir de la instancia conn.cursos
cursor = conn.cursor()

#Crear una tabla

#create_table = """ CREATE TABLE inventary (_id int, name text, price real)"""
#cursor.execute(create_table)

#Insertar datos
add_values = """ INSERT INTO inventary VALUES ('5', 'Are', '200')"""
cursor.execute(add_values)

conn.commit()

conn.close()