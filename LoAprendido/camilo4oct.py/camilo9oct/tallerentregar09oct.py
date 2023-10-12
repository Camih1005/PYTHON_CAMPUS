import random

def leerIntentos(msj):
    while True:
        try:
            n = int(input(msj))
            if n < 1 or n > 10 or n == "":
                print("Intentos alcanzados")
                continue
            return n
        except ValueError:
            print("Error, Total de intentos alcanzados")

def leerNombre(msj):
    while True:
        try:
            nom = input("Ingrese nombre:")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def menu():
    while True:
        try:
            print("\n" )
            print("\nMENU" )
            print("1. Nombre del usuario: ")
            print("2. Jugar: ")
            print("3. Salir ")
            op = int(input(">>> Opción (1-3)? "))
            if op < 1 or op > 3:
                print("Opción no válida. Escoja de 1 a 3.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 3.")
            input("Presione cualquier tecla para continuar...")
            
dicjug= []
while True:
    op = menu()
    if op == 1:
        leerNombre(dicjug)
        print(dicjug)
        input()
    elif op == 2:
        
    

    #elif op == 2:
#   modifProd(dicprod)
    #  3  print(dicprod)
#input()    
    #elif op == 3:
        #eliminarDicc(dicprod)
        #print(dicprod)
        #input()            