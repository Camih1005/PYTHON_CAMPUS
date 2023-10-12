#SERVICIO DE AGUA
n = int(input("cuantos ususarios? "))

for i in range(1, n+1):
    print(f"\nDatos del usuario #{i}" )
    cod = input("codigo? ")
    nom = input("nombre? ")
    est = input("estado [V: Vigente o S: Suspendido]")
    estr = int(input("estrato[1 a 6]? "))
    con = float(input("consumo de agua al mes [cm3]? "))


    if est == "V" or est == "v":
        if estr == 1:
            tbas = 10000
        elif estr == 2:
            tbas = 20000
        elif estr == 3:
            tbas = 30000
        elif estr == 4:
            tbas = 45000
        elif estr == 5:
            tbas = 600000
        elif estr == 6:
            tbas = 70000
#calcular el valor del consumo
        valcons = con * 200
#calcular el valor a pagar
        valpagar = tbas + valcons
        #imprimir el informe del usuario

        print("\n", "=" * 40 )           
        print("\t Nombre: ", nom)
        print(f"\tValor consumo: ${valcons:,.0f}")
        print(f"valor de la factura de agua: ${valpagar:,.0f}")   

""""""
#saber numero de digitos
import math

num = int(input("digite un numero entero: "))

if num < 0 :
    num = -1 * num

cantDig = math.floor(math.log10(num)) + 1

print("la cantidad de digitos es:", cantDig)

""""""

#Funcion range (valor inicial, valor final: incremento)
print(list(range(5)))  # 1 - 2 - 3 - 4 
print(list(range(19)))

print(list(range(2, 20)))
print(list(range(15, -3)))
print(list(range(2, 10, 3)))
print(list(range(15, -3, -1)))

print(list(range()))

""""""""

#ciclo 
for i in range(10):
    print(i, end=", ") # para poner todo hacial un lado con comas y espacio o se quita el end=", "
    


for i in range(6):
    print("*", end="")

print("")
for i in range(3):
    print("*    *")

for i in range(6):
    print("*", end="")

 """""""

#NOTAS DEL ESTUDIANTE PROMEDIO
nombre = input("nombre del estudiante: ")
nota = int(input("ingrese una nota: [0-100]: "))

if nota >= 0 and nota <= 59:
    notaCual = "D"
elif nota >= 60 and nota <= 79:
    notaCual = "C"
elif nota >= 80 and nota <= 89:
    notaCual = "B"
elif nota >= 90 and nota <= 100 :
    notaCual = "A"         
else:
    notaCual = ""
    print( "error. nota invalida.")

print("estudiante:", nombre)
print("nota cuantitativa:", nota)
print("nota cualitativa:", notaCual) 


a= float(input("nota 1: "))
b= float(input("nota 2: "))
c= float(input("nota 3: "))
nota=(a+b+c)/3
print("promedio notas: ",nota)   

"""""""

#sacar el promedio de notas que uno quiera sacar.

cant = int(input("Cantidad de notas: "))

sumaNotas = 0
for i in range(1, cant+1):
    nota = float(input(f"ingrese la nota #{i}: "))
    sumaNotas = sumaNotas + nota

prom = sumaNotas / cant

print(f"El promedio de las notas es: {prom:.1f}")

"""""""

#calcular el factorial de un numero
#factorial de 5 = 1 * 2 * 3 * 4 * 5

n = int(input("numero: "))

fact = 1
for i in range(1, n+1):
    fact *= i # fact = fact * i

print(f"el factorial de {n} es {fact:,}")    

"""""""

#ejercicio 1
#hacer un programa de python que genere el siguienre numero de la secuencia 1,1,2,-1,1,-2,?

n = int(input("numero: "))

fact = 1
for i in range(1, n+1):
    fact *= i # fact = fact * i

print(f"el factorial de {n} es {fact:,}")    

n1 = 1
n2 = 1
sig = -1
print(n1, n2, end=", ")
for i in range(5):
    s = n1 + (sig ** i) * n2 
    n1 = n2
    n2 = s
    print(s, end=", ")





                  