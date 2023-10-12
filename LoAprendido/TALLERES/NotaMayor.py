def resultado (N1,N2,N3,N4,N5):
  promedio = (N1+N2+N3+N4+N5)/5
  if promedio > 3.5:
    # print("La nota es mayor a 3.5, pasaste")
    return True
  else:
    # print("Reprovaste")
    return False 

Nota1 = float(input("Dijete la nota N1:"))
Nota2 = float(input("Dijete la nota N2:"))
Nota3 = float(input("Dijete la nota N3:"))
Nota4 = float(input("Dijete la nota N4:"))
Nota5 = float(input("Dijete la nota N5:"))

if resultado (Nota1, Nota2, Nota3, Nota4, Nota5):
   print("gano el año")
else:
  print("Perdio el año")


