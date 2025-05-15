#importo la libreria sqlite3 para la base de datos
import sqlite3 as sql

#creo la base de datos que contiene la tabla de usuarios y productos
def createdb(DatabaseName):
    conn =sql.connect(DatabaseName)
    conn.commit()
    conn.close()

#creo la tabla de inventario que contiene los productos
def createTable():
    conn = sql.connect('ProyectoFinal/Users&Stock.db')
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE inventario (
            name TEXT,
            price FLOAT,
            stock FLOAT
        )'''
    )
    conn.commit()
    conn.close()

#creo la tabla de usuarios que contiene los datos de los usuarios
def createTableUsers():
    conn = sql.connect('ProyectoFinal/Users&Stock.db')
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE users (
            name TEXT,
            password TEXT,
            type TEXT
        )'''
    )
    conn.commit()
    conn.close()

#creo la funcion para insertar los datos del nuevo usuario
def insertUser(name, password, type):
    conn = sql.connect('ProyectoFinal/Users&Stock.db')
    cursor = conn.cursor()
    cursor.execute(
        '''INSERT INTO users (name, password, type) VALUES (?, ?, ?)''',
        (name, password, type)
    )
    conn.commit()
    conn.close()

#creo la funcion para insertar los datos del nuevo producto
def insertProduct(name, price, stock):
    conn = sql.connect('ProyectoFinal/Users&Stock.db')
    cursor = conn.cursor()
    cursor.execute(
        '''INSERT INTO inventario (name, price, stock) VALUES (?, ?, ?)''',
        (name, price, stock)
    )
    conn.commit()
    conn.close()

#creo la funcion para mostrar los productos
def PrintProducts():
    conn = sql.connect('ProyectoFinal/Users&Stock.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM inventario''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
def userRequest(x):
    while True:
        if x == 1:
            print("Bienvenido cliente")
            print("1. Ver productos")
            print("2. Comprar productos")
            print("3. Salir")
            user = int(input("Ingrese opción: "))
            if user == 1:
                print("Mostrando productos...")
            elif user == 2:
                print("Comprando productos...")
            elif user == 3:
                print("Saliendo...")
                break
        elif x == 2:
            print("Bienvenido administrador")
            print("1. Agregar productos")
            print("2. Agregar usuarios")
            print("3. Ver inventario")
            print("4. Salir")
            user = int(input("Ingrese opción: "))
            if user == 1:
                print("Agregando productos...")
                name = input("Ingrese nombre del producto: ")
                price = float(input("Ingrese precio del producto: "))
                stock = float(input("Ingrese stock del producto: "))
                insertProduct(name, price, stock)
            elif user == 2:
                print("Agregando usuarios...")
                name = input("Ingrese nombre del usuario: ")
                password = input("Ingrese contraseña del usuario: ")
                typeUser = input("Ingrese tipo de usuario: ")
                insertUser(name, password, typeUser)
            elif user == 3:
                print("Mostrando inventario...")
                PrintProducts()
            elif user == 4:
                print("Saliendo...")
                break
def main():
    print("Bienveniado al sistema de gestión de inventario")
    print("1. Cliente")
    print("2. Administrador")
    print("3. Nuevo usuario")
    print("4. Salir")
    usuario = int(input("Ingrese tipo de usuario: "))
    userRequest(usuario)
if __name__ == "__main__":
    #createdb('ProyectoFinal/Users&Stock.db')
    #createTable()
    #createTableUsers()
    main()