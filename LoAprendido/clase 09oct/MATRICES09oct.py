def crearMatrices(fil, col):
    m=[]
    for i in fil:
        fila = [0] * col
        m.append(fila)
        
    return m 

def printMatriz(mat):
    for f in range (len(mat)):
        for c in range (len(mat[f])):
            print(mat[f] [c] , end = "")
        print("")
        
def llenarMatriz(mat):
    for f in range (len(mat)):
        print("\nFila #",f)
        for c in range (len(mat[f])):
            mat[f][c] = int(input(f"mat[{f}][{c}]? "))

            
    
matriz = crearMatrices(4,5)
llenarMatriz(matriz)
printMatriz(matriz)        