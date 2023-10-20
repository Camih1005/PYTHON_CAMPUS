import json
import time

rutaFile = "TABLAPosiciones.json"

def verificar_victoria(triki, linea):
    for i in range(3):
        if triki[i][0] == triki[i][1] == triki[i][2] == linea or \
           triki[0][i] == triki[1][i] == triki[2][i] == linea:
            return True

    if triki[0][0] == triki[1][1] == triki[2][2] == linea or \
       triki[0][2] == triki[1][1] == triki[2][0] == linea:
        return True

    return False

def guardarJugadores(tabla):
    try:
        with open(rutaFile, "w") as file:
            json.dump(tabla, file, indent=4)
    except Exception as e:
        print("Error al guardar la tabla de posiciones:", e)

def cargarJug():
    try:
        with open(rutaFile, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except Exception as e:
        print("Error al cargar la tabla de posiciones:", e)
        return []

def imprimir_tablero(tablero):
    for i in tablero:
        print(" | ".join(i))
        print("-" * 9)

def Crearjuego():
    return [[" " for _ in range(3)] for _ in range(3)]

def Jugar1():
    while True:
        try:
            jugador = input("\tNombre: ")
            if not jugador.isalnum():
                print("Nombre inválido. Debe contener solo caracteres alfanuméricos.")
            else:
                return jugador
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def ImprTablaPocisiones():
    tabla = cargarJug()
    if tabla:
        # Ordenar la tabla por tiempo ascendente
        tabla_ordenada = sorted(tabla, key=lambda x: x["tiempo"])
        
        print("\nTabla de Posiciones:")
        print("-" * 55)  # Línea superior
        print("{:<5} {:<15} {:<9} {:<12}".format("Pos.", "Nombre", "Victorias", "Tiempo (S)"))
        print("-" * 55)  # Línea divisoria
        
        for i, jugador in enumerate(tabla_ordenada, start=1):
            print("{:<5} {:<15} {:<9} {:<12}".format(i, jugador['nombre'], jugador['victorias'], jugador['tiempo']))
        
        print("-" * 55)  # Línea inferior
    else:
        print("La tabla de posiciones está vacía.")

def juego_tic_tac_toe():
    print("°°°°°°°°°°°°°°°°JUEGO DE TIC TAC TOE°°°°°°°°°°°°°°°°")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\tESPERO QUE DISFRUTEN EL MEJOR JUEGO\n")
    print("XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO")

    lstjugadores = cargarJug()

    while True:
        opcion = input("\n\t1. Jugar TIC TAC TOE\n\t2. Ver Tabla de Posiciones de jugadores\n\t3. Salir\n\tElija una opción del 1 al 3: ")

        if opcion == "1":
            empiezo = time.time()
            print("\n\tPLAYER 1 |X|")
            jugador1 = Jugar1()
            print("\n\tPLAYER 2 |O|")
            jugador2 = Jugar1()
            empiezo2 = time.time()
            tablero = Crearjuego()
            turno = 1

            movimientos1 = []
            movimientos2 = []

            while True:
                if turno % 2 == 1:
                    ActualJugador = jugador1
                    marca = 'X'
                    movimientos = movimientos1
                else:
                    ActualJugador = jugador2
                    marca = 'O'
                    movimientos = movimientos2

                imprimir_tablero(tablero)
                print(f"Turno de {ActualJugador} (con la {marca})")
                fila = int(input("Ingrese la fila (1, 2, 3): "))
                columna = int(input("Ingrese la columna (1, 2, 3): "))

                if tablero[fila - 1][columna - 1] == " ":
                    tablero[fila - 1][columna - 1] = marca
                    movimientos.append(f"({fila}, {columna})")
                else:
                    print("Esa casilla está en uso, repita de nuevo.")
                    continue

                if verificar_victoria(tablero, marca):
                    final = time.time()
                    imprimir_tablero(tablero)
                    print(f"¡{ActualJugador} ({marca}) es el ganador!")
                    print(f"Movimientos de {ActualJugador}:")
                    for movimiento in movimientos:
                        print(movimiento)
                    tiempo = final - empiezo if ActualJugador == jugador1 else final - empiezo2
                    lstjugadores.append({"nombre": ActualJugador, "victorias": 1, "tiempo": tiempo, "movimientos": movimientos1 if ActualJugador == jugador1 else movimientos2})
                    guardarJugadores(lstjugadores)
                    print(f"{ActualJugador} se tardó {tiempo:.3f} segundos")
                    break

                if turno == 9:
                    imprimir_tablero(tablero)
                    print("EMPATE!")
                    tiempo1 = final - empiezo
                    tiempo2 = final - empiezo2
                    lstjugadores.append({"nombre": jugador1, "victorias": 0, "tiempo": tiempo1, "movimientos": movimientos1})
                    lstjugadores.append({"nombre": jugador2, "victorias": 0, "tiempo": tiempo2, "movimientos": movimientos2})
                    guardarJugadores(lstjugadores)
                    break

                turno += 1

        elif opcion == "2":
            ImprTablaPocisiones()

        elif opcion == "3":
            print("¡Gracias por jugar!")
            break

        else:
            print("Opción no válida. Elija una opción válida del 1 al 3.")

if __name__ == "__main__":
    juego_tic_tac_toe()

