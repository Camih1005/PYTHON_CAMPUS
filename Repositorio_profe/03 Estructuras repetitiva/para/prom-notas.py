# capturar las notas de un curso y calcular el promedio de estas.
# Mostrar en pantalla el resultado del promedio

cant = int(input("Cantidad de notas: "))

sumaNotas = 0
for i in range(1, cant+1):
    nota = float(input(f"Ingrese la nota #{i}: "))
    sumaNotas = sumaNotas + nota # sumaNotas += nota
    
prom = sumaNotas / cant

print(f"El promedio de las notas es: {prom:.1f}")

