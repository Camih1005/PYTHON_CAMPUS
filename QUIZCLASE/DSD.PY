import json

# Variables globales
rutaFile = "tabla_posiciones.json"
lstjugadores = []

def cargar_tabla_posiciones():
    try:
        with open(rutaFile, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_tabla_posiciones(tabla):
    try:
        with open(rutaFile, "w") as file:
            json.dump(tabla, file, indent=4)
    except Exception as e:
        print("Error al guardar la tabla de posiciones:", e)

def existeJugador(nombre, jugadores):
    for jugador in jugadores:
        if jugador['nombre'] == nombre:
            return True
    return False


def verificar_victoria(tablero, marca):
    for i in range(3):
        # Verificar filas y columnas
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == marca or \
           tablero[0][i] == tablero[1][i] == tablero[2][i] == marca:
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == marca or \
       tablero[0][2] == tablero[1][1] == tablero[2][0] == marca:
        return True

    return False

def imprimir_tabla_posiciones():
    tabla = cargar_tabla_posiciones()
    if tabla:
        print("\nTabla de Posiciones:")
        for i, jugador in enumerate(tabla, start=1):
            print(f"{i}. {jugador['nombre']} - Victorias: {jugador['victorias']}, Derrotas: {jugador['derrotas']}")
    else:
        print("La tabla de posiciones está vacía.")

def Jugar():
    while True:
        try:
            jugador = input("Ingrese el nombre del jugador: ")
            if not jugador.isalnum():
                print("Nombre inválido. Debe contener solo caracteres alfanuméricos.")
            else:
                return jugador
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def Crearjuego():
    return [[" " for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tablero):
    for i in tablero:
        print(" | ".join(i))
        print("-" * 9)

def verificar_victoria(tablero, marca):
    # Implementa la lógica para verificar si hay una victoria
    # Retorna True si el jugador con 'marca' ganó, de lo contrario False
    pass

def juego_tic_tac_toe():
    print("¡Bienvenido al juego Tic Tac Toe!")
    
    while True:
        opcion = input("\n1. Jugar\n2. Ver Tabla de Posiciones\n3. Salir\nElija una opción (1/2/3): ")

        if opcion == "1":
            jugador1 = Jugar()
            jugador2 = Jugar()
            tablero = Crearjuego()
            turno = 1

            while True:
                if turno % 2 == 1:
                    jugador_actual = jugador1
                    marca = 'X'
                else:
                    jugador_actual = jugador2
                    marca = 'O'

                imprimir_tablero(tablero)
                print(f"Turno de {jugador_actual} ({marca})")

                fila = int(input("Ingrese la fila (1, 2, 3): "))
                columna = int(input("Ingrese la columna (1, 2, 3): "))

                if tablero[fila - 1][columna - 1] == " ":
                    tablero[fila - 1][columna - 1] = marca
                else:
                    print("¡Esa casilla ya está ocupada!")
                    continue

                if verificar_victoria(tablero, marca):
                    imprimir_tablero(tablero)
                    print(f"¡{jugador_actual} ({marca}) ha ganado!")
                    break

                if turno == 9:
                    imprimir_tablero(tablero)
                    print("¡Es un empate!")
                    break

                turno += 1
            # Actualizar la tabla de posiciones
            tabla_posiciones = cargar_tabla_posiciones()
            for jugador in tabla_posiciones:
                if jugador['nombre'] == jugador_actual:
                    if marca == 'X':
                        jugador['victorias'] += 1
                    else:
                        jugador['derrotas'] += 1
                    break
            else:
                if marca == 'X':
                    tabla_posiciones.append({'nombre': jugador_actual, 'victorias': 1, 'derrotas': 0})
                else:
                    tabla_posiciones.append({'nombre': jugador_actual, 'victorias': 0, 'derrotas': 1})
            guardar_tabla_posiciones(tabla_posiciones)
            
        elif opcion == "2":
            imprimir_tabla_posiciones()

        elif opcion == "3":
            print("¡Gracias por jugar!")
            break

        else:
            print("Opción no válida. Elija una opción válida (1/2/3).")

if __name__ == "__main__":
    juego_tic_tac_toe()