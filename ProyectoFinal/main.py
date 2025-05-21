# Importo la librería sqlite3 para la base de datos
import sqlite3 as sql
import os

#crea la base de datos que contiene la tabla de usuarios y productos
def createdb(DatabaseName):
    if os.path.exists(DatabaseName):
        print(f"Database '{DatabaseName}' already exists. Skipping creation.")
        return
    conn = sql.connect(DatabaseName)
    conn.commit()
    conn.close()

#elimina un producto de la base de datos
def delateProduct(name):
    conn = sql.connect('ProyectoFinal/Users&Stock.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM inventario WHERE name = ?''', (name,))
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

#funcion para insertar los datos del nuevo usuario
def insertUser(name, password, type):
    conn = sql.connect('ProyectoFinal/Users&Stock.db')
    cursor = conn.cursor()
    cursor.execute(
        '''INSERT INTO users (name, password, type) VALUES (?, ?, ?)''',
        (name, password, type)
    )
    conn.commit()
    conn.close()

#funcion para insertar los datos del nuevo producto
#se le pasan los datos del producto como parametros
def insertProduct(name, price, stock):
    conn = sql.connect('ProyectoFinal/Users&Stock.db')
    cursor = conn.cursor()
    cursor.execute(
        '''INSERT INTO inventario (name, price, stock) VALUES (?, ?, ?)''',
        (name, price, stock)
    )
    conn.commit()
    conn.close()

#funcion para mostrar los productos
#se conecta a la base de datos y se seleccionan todos los productos
#se guardan en una variable y se imprimen
def PrintProducts():
    conn = sql.connect('ProyectoFinal/Users&Stock.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM inventario''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

#funcion para realizaar la compra de productos
#se le pide al usuario el nombre del producto y la cantidad
#se busca el producto en la base de datos y se verifica si hay stock
#si hay stock se actualiza la base de datos y se muestra el precio total
#si no hay stock se muestra un mensaje de error
#si el usuario ingresa "salir" se sale del bucle
#se muestra la boleta de compra con los productos comprados y el precio total
def BuyProducts():
    conn = sql.connect('ProyectoFinal/Users&Stock.db')
    cursor = conn.cursor()
    total = 0
    boleta = []
    while True:
        name = input("Ingrese nombre del producto: ")
        if name == "salir":
            print("Saliendo...")
            break
        try:
            amount = int(input("Ingrese cantidad del producto: "))
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para la cantidad.")
            continue
        cursor.execute('''SELECT * FROM inventario WHERE name = ?''', (name,))
        rows = cursor.fetchall()
        if len(rows) == 0:
            print("Producto no encontrado")
        else:
            for row in rows:
                if row[2] < amount:
                    print("No hay suficiente stock")
                else:
                    price = row[1] * amount
                    total += price
                    cursor.execute('''UPDATE inventario SET stock = stock - ? WHERE name = ?''', (amount, name))
                    conn.commit()
                    print("Compra realizada")
                    print("El precio total es: " + str(price))
                    boleta.append((name, amount, row[1], price))
    if boleta:
        print("\n----- Boleta de compra -----")
        print("Producto\tCantidad\tPrecio\tTotal")
        for item in boleta:
            print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")
        print(f"Total a pagar: {total}")

#funcion para manejar las solicitudes de los clientes
def handleClientRequests():
    while True:
        print("Bienvenido cliente")
        print("1. Comprar productos")
        print("2. Salir")
        user = int(input("Ingrese opción: "))
        if user == 1:
            PrintProducts()
            print("Comprando productos...")
            BuyProducts()
        elif user == 2:
            print("Saliendo...")
            break

#funcion para manejar las solicitudes de los administradores
def handleAdminRequests():
    while True:
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

#funcion para mostrar el menu de opciones
#dependiendo del tipo de usuario que ingrese
def userRequest(x):
    if x == 1:
        handleClientRequests()
    elif x == 2:
        handleAdminRequests()

#funcion para validar el usuario y la contraseña
#se conecta a la base de datos y se selecciona el usuario y la contraseña
#si el usuario y la contraseña son correctos se devuelve el tipo de usuario
#si el usuario y la contraseña son incorrectos se devuelve False
def validateUser(usuario, password):
    conn = sql.connect('ProyectoFinal/Users&Stock.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM users WHERE name = ? AND password = ?''', (usuario, password))
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Usuario o contraseña incorrectos")
        conn.close()
        return False
    else:
        for row in rows:
            print("Bienvenido " + row[0])
            conn.close()
            return row[2]
    
#funcion principal donde se ingresara el usuario y validara la contraseña
#cerrando el programa si se ingresan 3 veces mal tanto el usuario como la contraseña
def main():
    print("Bienveniado al sistema de gestión de inventario")
    intentos = 0
    while True:
        usuario = input("Ingrese usuario: ")
        password = input("Ingrese contraseña: ")
        tipo = validateUser(usuario, password)
        if tipo == False:
            print("Usuario o contraseña incorrectos")
            intentos += 1
            if intentos == 3:
                print("Demasiados intentos")
                print("el programa se cerrara")
                break
        else:
            if tipo == "cliente":
                userRequest(1)
            elif tipo == "admin":
                userRequest(2)

if __name__ == "__main__":
    #createdb('ProyectoFinal/Users&Stock.db')
    #createTable()
    #createTableUsers()
    main()