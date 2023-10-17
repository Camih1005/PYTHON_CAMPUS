def ordenamiento_burbuja(lst):
    N = len(lst)
    for i in range(0, N-1):
        for j in range(i+1, N):
            if lst[i][1]["precio"] < lst[j][1]["precio"]:
                t = lst[i]
                lst[i] = lst[j]
                lst[j] = t
    return lst


productos = {
    1 : {
        "nombre":"pantalon",
        "precio": 125,
        "cantidad": 5
    },
    2 : {
        "nombre":"camisa",
        "precio": 200,
        "cantidad": 25
    },
    3 : {
        "nombre":"camiseta",
        "precio": 100,
        "cantidad": 3
    }
}

print(productos)

#pasar dic a lista
print("")
lstproductos = list(productos.items())
print(lstproductos)

lstord = ordenamiento_burbuja(lstproductos)
print("")
print(lstord)

print("")
productos = dict(lstord)
print(productos)