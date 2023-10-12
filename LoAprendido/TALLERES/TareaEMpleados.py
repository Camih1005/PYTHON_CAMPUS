# total_ventas = 0
# comisiones_totales = 0
# while True:
#     cedula = int(input("Ingrese su documento de identidad: \nsi desea salir del digite (-1): \n"))
#     if cedula == -1:
#         break
#     Nombre = input("Ingrese su nombre: \n")
#     tipo_vendedor = int(input("1. Puerta a puerta. \n2. Telemercadeo.  \n3. Ejecutivo en ventas. \nEscoja el tipo de vendedor: "))
#     valor_ventas = int(input("Ingrese el valor las ventas del mes: "))

#     if tipo_vendedor == 1:
#         total_ventas += valor_ventas
#         comision = valor_ventas * 0.2
#         comisiones_totales += comision
#         print(f"El valor a pagar de comision es: {comision:,.2f}\n")
#     elif tipo_vendedor == 2:
#         total_ventas += valor_ventas
#         comision = valor_ventas * 0.15
#         comisiones_totales += comision
#         print(f"El valor a pagar de comision es: {comision:,.2f}\n")
#     elif tipo_vendedor == 3:
#         total_ventas += valor_ventas
#         comision = valor_ventas * 0.25
#         comisiones_totales += comision
#         print(f"El valor a pagar de comision es: {comision:,.2f}\n")

# print(f"El valor total de ventas es: ${total_ventas:,.2f} \ny el valor a pagar de comisiones es: ${comisiones_totales:,.2f}")

#2222222

# while True:
#   cedula = int(input("ingrese documento de identidad:\nSi quiere salir ingrese (1): "))
#   if cedula == "n":
#      break


#   nombre = input("Ingrese su nombre: ")
#   clase_de_conductor = int(input("Ingrese su clase de conductor:\n1.Experto\n2.Basico\n1 o 2: "))
#   valor_pasajes = int(input("Valor total de las pasajes del mes: "))
#   Valor_enc = int(input("Valor de encomiendas del mes: ")) 

#   valor_encomienda = 0
#   total_pasajes = 0

#   if clase_de_conductor == 1:
#     total_pasajes = valor_pasajes * 0.30
#     valor_encomienda = Valor_enc * 0.20
#     print(f"El valor total de pasajes mas comision es de : ${total_pasajes:,.2f}")
#     print(f"El valor total de encomiendas es de : ${valor_encomienda:,.2f}")
#   elif clase_de_conductor == 2:
#     total_pasajes = valor_pasajes * 0.20
#     valor_encomienda = Valor_enc * 0.15
#     print(f"El valor total de pasajes mas comision es de : ${total_pasajes:,.2f}")  
#     print(f"El valor total de encomiendas es de : ${valor_encomienda:,.2f}")


while True:
  cedula = int(input("ingrese documento de identidad:\nSi quiere salir ingrese (1): "))
  if cedula == "n":
    break
  nombre = input("Ingrese su nombre: ")
  categoria =  input("Ingrese la categoria:\nDOCENTE A\nDOCENTE B\nDOCENTE C\nElija:")
  print("A/H = 25000\nB/H = 35000\nC/H = 50000")
  horas_laboradas = int(input("Ingrese las horas laboradas: "))

  Horlab = 1
  total_h = 0
  horalab = 1
  totall = 0
  if categoria == "A":
    total_h = horas_laboradas * 25000
    print(f"Precio total de hora laborada es {total_h}")
  elif categoria == "B" :
    total_h = horas_laboradas * 35000
    print(f"precio total de horas laboradas es {total_h}")
  elif categoria ==  "C":
    total_h = horas_laboradas  * 50000
    print(f"precio total de horas laboradas es {total_h}")
  else:
    print("opcion no valida")
      





 