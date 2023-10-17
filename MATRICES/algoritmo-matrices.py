def crearMatrices(fil, col):
    m = []
    for i in range(fil):
        fila = [0] * col
        m.append(fila)
    return m

def printMatrices(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print(mat[f][c], end='\t')
        print('')

def llenarMatrices(mat):
    for f in range(len(mat)):
        print("\nFila #",f+1)
        for c in range(len(mat[f])):
            mat[f][c] = int(input(f"\nmat[{f+1}][{c+1}]"))
            # print(mat[f][c], end=' ')
        print('')


matriz = crearMatrices(4, 5)
llenarMatrices(matriz)
printMatrices(matriz)

