#TRABAJO 1
distancia_en_kilometros = float(input ("Ingresa el valor de distancia en km: "))
numero_de_dias_min = float(input ("Ingresa el valor de numero de dias: "))
subtotal = distancia_en_kilometros * 0.63
subtotal_descuento = subtotal * 0.7
if numero_de_dias_min>7 and distancia_en_kilometros > 800: 
		print(f"Valor del ticket ${subtotal} y se le aplica un 30% de descuento y el valor final es ${subtotal_descuento}")
else:
    descuento=0
total=subtotal-descuento
print(f"Valor del ticket ${total}")

#TRABAJO 2


año = int(input("ingrese el año a buscar:"))

if  año%4 == 0 and 100 != 0:
	print("Es bisiesto")
	
elif año%100 == 0 and 400 != 0:  
		print("Es bisiesto")   # divisible entre 4 y 100
else : # divisible entre 4, 100 y 400
		print("no es bisiesto")
		
        
 #TRABAJO 3
peso= float(input("ingrese el peso:"))
altura= float(input("ingrese la altura:"))


imc= round(peso/(altura**2),2)
if imc<18.5:
  print("peso bajo") 
elif imc>=18.5 and imc<=24.9:
  print("peso normal")
elif imc>=25.0 and imc<=29.9:
  print("sobrepeso")
elif imc>=30.0 and imc<=34.9:
  print("obesidad")
elif imc>=35.0 and imc<=39.9:
  print("obesidad extrema")
else:
  print("Los dato que ingreso no son validos")       