def resultadoEstudiante(n1,n2,n3,n4,n5):
    prom = (n1+n2+n3+n4+n5) / 5
    if prom > 3.5:
        return True
    else:
        return False
    
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))
nota5 = float(input("Ingrese la nota 5: "))

if resultadoEstudiante(nota1, nota2, nota3, nota4, nota5):
    print("Gano el año")
else:
    print("Perdió el año")