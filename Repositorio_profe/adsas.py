import json

def inicializar_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

def verificar_ganador(tablero, jugador):
    for fila in tablero:
        if all(cell == jugador for cell in fila):
            return True
    for columna in range(3):
        if all(tablero[fila][columna] == jugador for fila in range(3)):
            return True
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False

def jugar():
    print("¡Bienvenido al juego de Tic Tac Toe!")
    jugador1 = input("Jugador 1, ingrese su nombre: ")
    jugador2 = input("Jugador 2, ingrese su nombre: ")

    tablero = inicializar_tablero()
    turno = 1
    jugadores = [jugador1, jugador2]

    while True:
        imprimir_tablero(tablero)
        print(f"Turno de {jugadores[turno % 2]} (X)")

        fila = int(input("Ingrese el número de fila (1, 2 o 3): ") - 1)
        columna = int(input("Ingrese el número de columna (1, 2 o 3): ") - 1)

        if tablero[fila][columna] == " ":
            tablero[fila][columna] = "X" if turno % 2 == 0 else "O"
            if verificar_ganador(tablero, tablero[fila][columna]):
                imprimir_tablero(tablero)
                print(f"¡{jugadores[turno % 2]} (X) ha ganado!")
                break
            turno += 1
        else:
            print("La celda ya está ocupada. Inténtalo de nuevo.")

    with open("tic_tac_toe.json", "w") as archivo:
        json.dump({"tablero": tablero, "turno": turno, "jugadores": jugadores}, archivo)

if __name__ == "__main__":
    jugar()
