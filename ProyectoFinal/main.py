def userRequest(x):
    if x==1:
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
    elif x==2:
        print("Bienvenido administrador")
        print("1. Agregar productos")
        print("2. Ver inventario")
        print("3. Salir")
        user = int(input("Ingrese opción: "))
        if user == 1:
            print("Agregando productos...")
        elif user == 2:
            print("Mostrando inventario...")
        elif user == 3:
            print("Saliendo...")
def main():
    print("Bienveniado al sistema de gestión de inventario")
    print("1. Cliente")
    print("2. Administrador")
    usuario = int(input("Ingrese tipo de usuario: "))
    userRequest(usuario)
if __name__ == "__main__":
    main()