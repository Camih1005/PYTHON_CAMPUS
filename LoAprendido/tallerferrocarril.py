def main():
    
    red_ferrocarriles = {}


    N = int(input("Número de ciudades: "))

    
    for i in range(N):
        nombre_ciudad = input(f"Nombre de la ciudad {i + 1}: ")
        conexiones = input(f"Ciudades enlazadas para {nombre_ciudad}: ").split(',')
        red_ferrocarriles[nombre_ciudad] = conexiones


    ciudad_origen = input("Ciudad de origen: ")
    ciudad_destino = input("Ciudad de destino: ")


    if hay_via_directa(red_ferrocarriles, ciudad_origen, ciudad_destino):
        print("Hay una vía directa entre las ciudades.")
    else:
        print("No hay una vía directa entre las ciudades.")

def hay_via_directa(red_ferrocarriles, ciudad_origen, ciudad_destino):
    visitados = set()
    cola = [ciudad_origen]

    while cola:
        ciudad_actual = cola.pop(0)
        if ciudad_actual == ciudad_destino:
            return True

        visitados.add(ciudad_actual)

        for ciudad_vecina in red_ferrocarriles.get(ciudad_actual, []):
            if ciudad_vecina not in visitados:
                cola.append(ciudad_vecina)

    return False

if __name__ == "__main__":
    main()