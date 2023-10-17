def calcDiaMaxIngresos(matVtas, matPrecios):
    fils = len(matVtas)
    cols = len(matVtas[0])
    lstVtasDia = [0] * cols
    for f in range(fils):
        for c in range(cols):
            lstVtasDia[c] += matVtas[f][c] * matPrecios[f]
      
    print(lstVtasDia)
    diaMaxVtas = max(lstVtasDia)
    posDia = lstVtasDia.index(diaMaxVtas)
    return posDia
                
def calcProdMaxIngresosSem(matVtas, matPrecios):
    fil = len(matVtas)
    lstTotVtas = [0] * fil
    for f in range(fil):
        lstTotVtas[f] = sum(matVtas[f]) * matPrecios[f]
        
    # print(lstTotVtas)
    maxVtas = max(lstTotVtas)
    prodMaxVtas = lstTotVtas.index(maxVtas) + 1
    return prodMaxVtas
    


matPrecios = [1500, 5000, 6500, 2500, 22500]
matVtas = [ [100, 88, 92, 94, 85, 110, 118],
            [30, 42, 31, 32, 38, 40, 37],
            [23, 35, 39, 45, 55, 60, 61],
            [45, 50, 56, 65, 47, 57, 68],
            [18, 25, 33, 21, 22, 28, 32] ]

prodMaxIngSem = calcProdMaxIngresosSem(matVtas, matPrecios)
print("El producto que más genera ingresos en la semana es:", prodMaxIngSem)

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]
diaMaxIngreso = calcDiaMaxIngresos(matVtas, matPrecios)
print("El día que genera ingresos en es:", dias[diaMaxIngreso])