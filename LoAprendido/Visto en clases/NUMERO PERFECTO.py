numero = int(input("Introduce un número perfecto:"))
i=1
total=0
while(i < numero):
   if numero%i==0:
     total = total+i
   i=i+1

if total==numero: 
   print("perfecto")
else:
    print("no perfecto")

#2

matricula = 10000
cont_años = 0
while matricula <= 20000:
   cont_años += 1
   matricula += matricula * 0.07



print(f"El valor la matricula sera el doble en {cont_años} años")





 