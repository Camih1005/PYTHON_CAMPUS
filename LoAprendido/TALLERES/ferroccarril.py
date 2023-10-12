#1
distancia_en_kilometros = float (input ("Ingresa el valor de distancia en km: "))
numero_de_dias_min = float (input ("Ingresa el valor de numero de dias: "))
subtotal=distancia_en_kilometros*0.63
if numero_de_dias_min>7:
    descuento=subtotal*0.30
else:
    descuento=0
total=subtotal-descuento
print ("valor de descuento: " + repr (descuento))
print ("Valor de subtotal: " + repr (subtotal))
print ("Valor de total: " + repr (total))

#2


año = input(int("ingrese el año a buscar:"))

if not año % 4:
	if not año % 100:     # divisible entre 4 y 100
		if not año % 400:  # divisible entre 4, 100 y 400
			print("Es bisiesto")
		else:              # divisible entre 4 y 100 y no entre 400
			print("No es bisiesto")
	else:                 # divisible  entre 4 y no entre 100
		print("Es bisiesto")
else:                    # no divisible entre 4
	print("No es bisiesto")
