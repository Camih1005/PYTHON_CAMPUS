total_ventas = 0
comisiones_totales = 0
while True:

    try:
        cedula = int(input("Ingrese su documento de identidad: \nsi desea salir del digite (-1): \n"))
        cedula = cedula.isdigit() == True
        if cedula == -1:
         print("Hasta luego")
         continue
        break
    except Exception as e:
        print("Error al ingresar la cedula. Ingrese su  cedula de nuevo:") 
    
    
    Nombre = input("Ingrese su nombre: \n")
    tipo_vendedor = int(input("1. Puerta a puerta. \n2. Telemercadeo.  \n3. Ejecutivo en ventas. \nEscoja el tipo de vendedor: "))
    valor_ventas = int(input("Ingrese el valor las ventas del mes: "))

    if tipo_vendedor == 1:
        total_ventas += valor_ventas
        comision = valor_ventas * 0.2
        comisiones_totales += comision
        print(f"El valor a pagar de comision es: {comision:,.2f}\n")
    elif tipo_vendedor == 2:
        total_ventas += valor_ventas
        comision = valor_ventas * 0.15
        comisiones_totales += comision
        print(f"El valor a pagar de comision es: {comision:,.2f}\n")
    elif tipo_vendedor == 3:
        total_ventas += valor_ventas
        comision = valor_ventas * 0.25
        comisiones_totales += comision
        print(f"El valor a pagar de comision es: {comision:,.2f}\n")

print(f"El valor total de ventas es: ${total_ventas:,.2f} \ny el valor a pagar de comisiones es: ${comisiones_totales:,.2f}")
