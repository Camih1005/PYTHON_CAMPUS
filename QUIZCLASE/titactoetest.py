import json
import time

def existeNom(Nombre, lstjugadores):
    #funcion que encuentra la posición de un codigo en la lista
    # Devuelve un número enterior >= 0 si el codigo existe
    # Devuelve un -1 si el codigo NO existe
    for i, datos in enumerate(lstjugadores):
        # El método enumerate () agrega un contador a un iterable y 
        # lo devuelve en forma de objeto de enumeración. 
        # Este objeto enumerado puede usarse directamente para bucles 
        # o convertirse en una lista de tuplas usando la función list().
        k = list(datos.keys())[0]
        if k == Nombre:
            return i
    return -1

            
        
def verificar_victoria(triki, linea):
    for i in range(3):

        if triki[i][0] == triki[i][1] == triki[i][2] == linea or \
           triki[0][i] == triki[1][i] == triki[2][i] == linea:
            return True

    if triki[0][0] == triki[1][1] == triki[2][2] == linea or \
       triki[0][2] == triki[1][1] == triki[2][0] == linea:
        return True

    return False


def guardarnombre(lstjugadores, rutaFile):
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

def imprimir_tablero(Juego):
    for i in Juego:
        print(" | ".join(i))
        print("-" *9)

def Crearjuego():
    return [[" " for _ in range(3)] for _ in range(3)]     

def Jugar1():
    while True:
        try:
            jugador = input("\tIngrese el nombre del jugador : ")
            if not jugador.isalnum():
                print("Nombre inválido. Debe contener solo caracteres alfanuméricos.")
            else:
                return jugador
        except Exception as e:
            print("Error al ingresar el nombre.", e) 

def ImprTablaPocisiones():
    tabla = TablaDePosiciones()
    if tabla:
        print("\nTabla de Posiciones:")
        for i, jugador in enumerate(tabla, start=1):
            print(f"{i}. {jugador['nombre']} - Victorias: {jugador['victorias']}, Derrotas: {jugador['derrotas']}")
    else:
        print("La tabla de posiciones está vacía.")  
            
def TablaDePosiciones(rutaFile):
    try:
        with open(rutaFile, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  
            
rutaFile = "QUIZCLASE/Pocisionesjugadores.json"
lstjugadores = []
lstjugadores =(lstjugadores, rutaFile)
def juego_tic_tac_toe():
    print("°°°°°°°°°°°°°°°°JUEGO DE TIK TAC TOE°°°°°°°°°°°°°°°°°°°")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\tESPERO QUE DISFRUTEN EL MEJOR JUEGO\n")
    print("XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO")
    tiempo1 = 0    
    tiempo2 = 0
    while True:
        opcion = input("\n\t1. Jugar TIC TAC TOE\n\t2. Ver Tabla de Posiciones de jugadores\n\t3. Salir\n\tElija una opcion del 1 al 3:  ")

        if opcion == "1":
            empiezo = time.time()
            jugador1 = Jugar1()
            final = time.time()
            empiezo2 = time.time()
            jugador2 = Jugar1()
            final2 = time.time()
            tablero = Crearjuego()
            turno = 1
            tiempo1 = tiempo1 + (final-empiezo)
            tiempo2 = tiempo2 + (final2-empiezo2)

            while True:
                if turno % 2 == 1:
                    ActualJugador = jugador1
                    marca = 'X'
                else:
                    ActualJugador = jugador2
                    marca = 'O'

                imprimir_tablero(tablero)
                print(f"Turno de {ActualJugador} ({marca})")
    
                fila = int(input("Ingrese la fila (1, 2, 3): "))
                columna = int(input("Ingrese la columna (1, 2, 3): "))

                if tablero[fila - 1][columna - 1] == " ":
                    tablero[fila - 1][columna - 1] = marca
                else:
                    print("Esa casilla esta en uso, repita de nuevo.")
                    continue

                if verificar_victoria(tablero, marca):
                    imprimir_tablero(tablero)
                    print(f"¡{ActualJugador} ({marca}) Es el ganador!")
                    print(f"{jugador1} se tardo {tiempo1} ")                 
                    break


                if turno == 9:
                    imprimir_tablero(tablero)
                    print("EMPATE!")
                    break

                turno += 1
            # Actualizar la tabla de posiciones
            ImprTablaPocisiones = TablaDePosiciones()
            for jugador in ImprTablaPocisiones:
                if jugador['nombre'] == ActualJugador:
                    if marca == 'X':
                        jugador['victorias'] += 1
                    else:
                        jugador['derrotas'] += 1
                    break
            else:
                if marca == 'X':
                    ImprTablaPocisiones.append({'nombre': ActualJugador, 'victorias': 1, 'derrotas': 0})
                else:
                    ImprTablaPocisiones.append({'nombre': ActualJugador, 'victorias': 0, 'derrotas': 1})
            ImprTablaPocisiones(ImprTablaPocisiones)

            
        elif opcion == "2":
            ImprTablaPocisiones()

        elif opcion == "3":
            print("¡Gracias por jugar!")
            break

        else:
            print("Opción no válida. Elija una opción válida del 1 al 3.")

if __name__ == "__main__":
    juego_tic_tac_toe()
    print()