def calcProdMaxIngresosSem(matVtas, matPrecios):
    fil = len(matVtas)
    lstTotVtas = [0] * fil
    for f in range(fil):
        lstTotVtas[f] = sum(matVtas[f]) * matPrecios[f]
     
    maxVtas = max(lstTotVtas) 
    prodmaxVtas = lstTotVtas.index(maxVtas) + 1   
    return prodmaxVtas
    
    
matPrecios = [1500, 5000, 6500, 2500, 22500]
matVtas =[[100, 88, 92, 85, 110, 118],
          [30, 42, 31, 32, 38, 40, 37],
          [23, 35, 39, 45, 55, 60, 61],
          [45, 50, 56, 65, 47, 57, 68],
          [18, 25, 33, 21, 22, 28, 32]]

prodMaxIngSem = calcProdMaxIngresosSem(matVtas, matPrecios)
print ("El producto que mas genera ingresos en la semana es :", prodMaxIngSem)


