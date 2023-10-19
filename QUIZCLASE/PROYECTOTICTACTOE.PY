import json

def existeNom(Nombre, lstLibros):
    #funcion que encuentra la posición de un codigo en la lista
    # Devuelve un número enterior >= 0 si el codigo existe
    # Devuelve un -1 si el codigo NO existe
    for i, datos in enumerate(lstLibros):
        # El método enumerate () agrega un contador a un iterable y 
        # lo devuelve en forma de objeto de enumeración. 
        # Este objeto enumerado puede usarse directamente para bucles 
        # o convertirse en una lista de tuplas usando la función list().
        k = list(datos.keys())[0]
        if k == Nombre:
            return i
    return -1


def Jugar():
    while True:
        try:
            jugador = input("Ingrese el nombre del jugador 1: ")
            
            if len(jugador) == 0 and  not jugador.isalnum():
                print("Nombre inválido")
                continue
            
            return jugador
        except Exception as e:
            print("Error al ingresar el nombre.", e)
            
        

def guardarnombre(lstjugadores, ruta):
    # Función que guarda los datos de la lista de personal
    # en un arcivo JSON
    # Devuelve True: si los datos fueron guardados correctamente
    # Devuelve False: si los datos no se pudieron guardar
    
    try:
        fd = open(rutaFile, "w")
    except Exception as e:
        print("Error al abrir el archivo para guardar al empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        json.dump(lstjugadores, fd)
    except Exception as e:
        print("Error al guardar la información del empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.")
        input("Presione cualquier tecla para continuar\n")
        return False
    
    return True

def Crearjuego():
    banderaa = 0
    for e in range(3):
        print("+-----+-----+-----+")
        print(f"|  {e+1+banderaa}  |  {e+2+banderaa}  |  {e+3+banderaa}  |")
        print(f"|     |     |     |")
        
        banderaa +=2 
    print("+-----+-----+-----+")
    
def CreandosotwareJuego():
    pass

def agregarNOM(lstjugadores, rutaFile):
    print("\n\n1. Agregar Libro")
    
    nombre = int(input("Ingrese el codigo: "))
    while existeNom(nombre, lstjugadores) != -1:
        # si existeId es -1 entonces no existe ese codigo en lstLibros
        # si es diferente a -1, entonces el codigo y existe.
        print("--> Ya existe un libro con ese ID")
        input("Presione cualquier tecla para continuar\n")
        nombre = input("\nIngrese el nombre: ")

    nombre = input("nombre: ")
    
    dicjugadores = {}
    dicjugadores[nombre] = {"nombre":nombre}
    lstjugadores.append(dicjugadores)
    
    if guardarnombre(lstjugadores, rutaFile) == True:
        input("El jugador ha sido registrado con éxito.\nPresione cualquier tecla para continuar...")
    else:
        input("Ocurrio algún error al guardar el jugador.")            
        
            
def menu():
    while True:
        try:
            print("***************JUEGO TIC TAC TOE****************")
            print("*******************ACME GAME******************")
            print("Bienvenidos al mejor juego jamas creado por python!")
            print( "=" * 50, "\n")
            print("1. Iniciar juego ")
            print("2. Ver tabla de pocisiones")
            print("3. Salir del juego")
            print()

            op = int(input(">>> Opción (1-3):  "))
            if op < 1 or op > 3:
                print("Opción no válida. Escoja de 1 a 3.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 3.")
            input("Presione cualquier tecla para continuar...")
            
rutaFile = "/home/spukN01-/Documents/CCamilo/CAMPUS_REPOSITORIO-1/QUIZCLASE/DatosJugadores.json"
lstjugadores = []
lstjugadores =(lstjugadores, rutaFile)
while True:
    op = menu()
    if op == 1:
        player1 = Jugar()
        player2 = Jugar()
        print("Que comienze el juego")
        Crearjuego()
    
    elif op == 2:
        pass
    
    elif op == 3:
        print("\nGracias por usar el programa")