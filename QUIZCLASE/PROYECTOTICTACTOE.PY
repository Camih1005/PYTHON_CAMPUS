import json

def leernombre():

def menu():
    while True:
        try:
            print("***************JUEGO TIC TAC TOE****************")
            print("*******************ACME GAME******************")
            print("Bienvenidos al mejor juego jamas creado por python!")
            print( "=" * 30, "\n")
            print("1. Iniciar juego ")
            print("2. Ver tabla de pocisiones")
            print("3. Salir del juego")
            print()

            op = int(input(">>> Opción (1-3)? "))
            if op < 1 or op > 3:
                print("Opción no válida. Escoja de 1 a 3.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 3.")
            input("Presione cualquier tecla para continuar...")

opcion = menu()

while True:
    option = menu()
    if option == 1:
        agregarProducto()
        print()
        input()
    elif option == 2:
        modifyProduct(dicProduct, readId())
        print()
        input()
    elif option == 3:
        eraseProduct(dicProduct, readId())
        print(dicProduct)
        input()
   
    elif option == 6:
        print("Thanks for using the software")
        input()
        break

