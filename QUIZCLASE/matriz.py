import json
import time

rutaFile = "tabla_posiciones.json"  # Mueve la declaración de rutaFile al principio del script

def verificar_victoria(triki, linea):
    for i in range(3):
        if triki[i][0] == triki[i][1] == triki[i][2] == linea or \
           triki[0][i] == triki[1][i] == triki[2][i] == linea:
            return True

    if triki[0][0] == triki[1][1] == triki[2][2] == linea or \
       triki[0][2] == triki[1][1] == triki[2][0] == linea:
        return True

    return False

# Función que guarda los datos de la lista de jugadores en un archivo JSON
def guardarJugadores(tabla):
    try:
        with open(rutaFile, "w") as file:
            json.dump(tabla, file, indent=4)
    except Exception as e:
        print("Error al guardar la tabla de posiciones:", e)

# Función que carga los datos de los jugadores desde el archivo JSON
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
            jugador = input("\tIngrese el nombre del jugador 1: ")
            if not jugador.isalnum():
                print("Nombre inválido. Debe contener solo caracteres alfanuméricos.")
            else:
                return jugador
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def ImprTablaPocisiones():
    tabla = cargarJug()
    if tabla:
        print("\nTabla de Posiciones:")
        for i, jugador in enumerate(tabla, start=1):
            print(f"{i}. {jugador['nombre']} - Victorias: {jugador['victorias']}, Derrotas: {jugador['derrotas']}")
    else:
        print("La tabla de posiciones está vacía.")


lstjugadores = []
lstjugador = []
def juego_tic_tac_toe():
    print("°°°°°°°°°°°°°°°°JUEGO DE TIC TAC TOE°°°°°°°°°°°°°°°°°°°")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\tESPERO QUE DISFRUTEN EL MEJOR JUEGO\n")
    print("XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO")
    tiempo1 = 0
    tiempo2 = 0

    while True:
        opcion = input("\n\t1. Jugar TIC TAC TOE\n\t2. Ver Tabla de Posiciones de jugadores\n\t3. Salir\n\tElija una opción del 1 al 3: ")

        if opcion == "1":
            empiezo = time.time()
            jugador1 = Jugar1()
            final = time.time()
            empiezo2 = time.time()
            jugador2 = Jugar1()
            final2 = time.time()
            tablero = Crearjuego()
            turno = 1
            tiempo1 = tiempo1 + (final - empiezo)
            tiempo2 = tiempo2 + (final2 - empiezo2)

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
                    print("Esa casilla está en uso, repita de nuevo.")
                    continue

                if verificar_victoria(tablero, marca):
                    imprimir_tablero(tablero)
                    print(f"¡{ActualJugador} ({marca}) es el ganador!")
                    lstjugador.append(ActualJugador)
                    lstjugadores.append({"nombre": ActualJugador, "victorias": 1, "derrotas": 0})
                    guardarJugadores(lstjugadores)
                    print(f"{jugador1} se tardó {tiempo1:,.3f} segundos")
                    break

                if turno == 9:
                    imprimir_tablero(tablero)
                    print("EMPATE!")
                    lstjugadores.append({"nombre": jugador1, "victorias": 0, "derrotas": 0})
                    lstjugadores.append({"nombre": jugador2, "victorias": 0, "derrotas": 0})
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
