import json
import time

            
        
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

def imprimir_tablero(tablero):
    for i in tablero:
        print(" l ".join(i))
        print("-" *9)

def Crearjuego():
    return [[" " for _ in range(3)] for _ in range(3)]     

def Jugar1():
    while True:
        try:
            jugador = input("\tIngrese el nombre del jugador 1 : ")
            if not jugador.isalnum():
                print("Nombre inválido. Debe contener solo caracteres alfanuméricos.")
            else:
                return jugador
        except Exception as e:
            print("Error al ingresar el nombre.", e) 

def ImprTablaPocisiones(lstjugadores,rutaFile):
    tabla = cargarJug(lstjugadores,rutaFile)
    if tabla:
        print("\nTabla de Posiciones:")
        for i, jugador in enumerate(tabla, start=1):
            print(f"{i}. {jugador['nombre']} - Victorias: {jugador['victorias']}, Derrotas: {jugador['derrotas']}")
    else:
        print("La tabla de posiciones está vacía.")  
            
    

def guardarJugadores(lstjugadores,rutaFile):    
    try:
        fd = open(rutaFile, "w")
    except Exception as e:
        print("Error al guardar la información\n", e)
        return None
    try:
        lstjugadores = json.dump(lstjugadores,fd)
    except Exception as e:
        print("Error al guardar la información\n", e)
    fd.close()
    return True
        
def cargarJug(lstjugadores, rutaFile):
    try:
        fd = open(rutaFile, "r")
    except Exception as e:
        try:
            fd = open(rutaFile, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            fd.close()
            input("Presione cualquier tecla para continuar\n")
            return None
    try:
        fd = open(rutaFile, "r")
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstjugadores = json.load(fd)
        else:
            lstjugadores = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        input("Presione cualquier tecla para continuar\n")
        return None
    fd.close()
    return lstjugadores


def juego_tic_tac_toe():
    
    rutaFile = "QUIZCLASE/Pocisionesjugadores.json"
    lstjugadores = []
    lstjugador = []
    lstjugadores =cargarJug(lstjugadores, rutaFile)



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
                print(f"Turno de {ActualJugador} (con la {marca})")
    
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
                    lstjugador.append(ActualJugador)
                    lstjugador.append(marca)
                    lstjugadores.append(lstjugador)
                    guardarJugadores(lstjugadores,rutaFile)
                    print(f"{jugador1} se tardo {tiempo1:,.3f} ")                 
                    break


                if turno == 9:
                    imprimir_tablero(tablero)
                    print("EMPATE!")
                    break

                turno += 1
            # Actualizar la tabla de posiciones
            TablaPoci = cargarJug(lstjugadores,rutaFile)
            for jugador in TablaPoci:
                if jugador[0] == ActualJugador:
                    if marca == 'X':
                        jugador['victorias'] += 1
                    else:
                        jugador['derrotas'] += 1
                    break
            else:
                if marca == 'X':
                    TablaPoci.append({'nombre': ActualJugador, 'victorias': 1, 'derrotas': 0})
                else:
                    TablaPoci.append({'nombre': ActualJugador, 'victorias': 0, 'derrotas': 1})
            guardarJugadores(TablaPoci)

            
        elif opcion == "2":
            ImprTablaPocisiones(lstjugadores,rutaFile)

        elif opcion == "3":
            print("¡Gracias por jugar!")
            break

        else:
            print("Opción no válida. Elija una opción válida del 1 al 3.")


juego_tic_tac_toe()