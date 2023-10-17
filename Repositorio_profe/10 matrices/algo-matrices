def crearMatrices(fil, col):
    m = []
    for i in range(fil):
        fila = [None] * col # col:5 => [5, 2.25, "carlos", {}]
        m.append(fila)
        
    return m

def printMatriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print(mat[f][c], end=" ")
        print("")
        
def llenarMatriz(mat):
    for f in range(len(mat)):
        print("\nFila #",f+1)
        for c in range(len(mat[f])):
            mat[f][c] = int(input(f"mat[{f+1}][{c+1}]? "))

matriz = crearMatrices(4, 5)
llenarMatriz(matriz)
printMatriz(matriz)