#Así podemos leer datos dentro de una matriz Python cuando usamos una lista 
 

#Usaremos la matriz anterior. El ejemplo leerá los datos, imprimirá la matriz, mostrará el último elemento de cada fila.

 

#Ejemplo: para imprimir la matriz

 

M1 = [[8, 14, -6], 
    [12,7,4], 
    [-11,3,21]]

##To print the matrix
print(M1)


#Producción:


#The_Matrix M1 =  [[8, 14, -6], [12, 7, 4], [-11, 3, 21]]

 

#Ejemplo 2: Leer el último elemento de cada fila.

 

M1 = [[8, 14, -6],
        [12,7,4], 
        [-11,3,21]]

matrix_length = len(M1)

#To read the last element from each row.
for i in range(matrix_length):
    print(M1[i][-1])



#Producción:


-6
4
21

 

#Ejemplo 3: para imprimir las filas en la matriz

 

M1 = [[8, 14, -6],
        [12,7,4], 
        [-11,3,21]]

matrix_length = len(M1)

#To print the rows in the Matrix
for i in range(matrix_length):
    print(M1[i])

 

#Producción:

 

[8, 14, -6]
[12, 7, 4]
[-11, 3, 21]

 

#De esta manera es que funcionan las matrices en Python, puedes comenzar a ponerlas en práctica y descubrir los diferentes beneficios que aportan para cuando comiences a desarrollar una aplicación o sito web en este versátil lenguaje. 

