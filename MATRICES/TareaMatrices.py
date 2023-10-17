def crear_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(i * n + j + 1)
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()


n = int(input("Ingrese el tamaño de la matriz cuadrada: "))

matriz = crear_matriz(n)

print("Matriz generada:")
imprimir_matriz(matriz)

# def crearMatrices(fil, col):
#     m = []
#     for i in range(fil):
#         fila = [0] * col
#         m.append(fila)
#     return m

# def printMatrices(mat):
#     for f in range(len(mat)):
#         for c in range(len(mat[f])):
#             print(mat[f][c], end='\t')
#         print('')

# def llenarMatrices(mat):
#     for f in range(len(mat)):
#         print("\nFila #",f+1)
#         for c in range(len(mat[f])):
#             mat[f][c] = int(input(f"\nmat[{f+1}][{c+1}]"))
#             print(mat[f][c], end=' ')
#         print('')


# matriz = crearMatrices(4, 5)
# llenarMatrices(matriz)
# printMatrices(matriz)