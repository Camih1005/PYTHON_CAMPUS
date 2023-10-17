type1 = "Puerta a puerta"
type2 = "Telemercadeo"
type3 = "Ejecutivo de ventas"
sumatoriaVentas = 0
sumatoriaComisiones = 0

while bandera == True:
    while True:
        try:
            cedula = input("Ingrese el numero de la cedula: ")
            cedula = cedula.strip()
            cedula2 = cedula.replace(",","")
            cedula2 = cedula2.replace(".","")
            if len(cedula2) == 0 or cedula2.isdigit() == False or (len(cedula2) >= 8 and len(cedula2) <= 10) == False :
                if cedula == "-1":
                    bandera = False
                else:
                    print("Formato de cedula invalido")
                    continue
            break
        except Exception as e:
                print(f"Error.Cedula invalida.{e}")

    if bandera == True:    
        while True:
            try:
                name = input("Ingrese el nombre del vendedor: ")
                name = name.strip()
                name2 = name.replace(" ","",3)
                if len(name2) == 0 or name2.isalnum() == False:
                    print("Formato de nombre invalido.")
                    continue
                break
            except Exception as e:
                print(f"Error.Nombre invalido.{e}")

        while True:
            try:
                contVentas = input("Cuanto vendio en el mes: ")
                contVentas = contVentas.strip()
                contVentas = float(contVentas.replace(",","."))
                if contVentas < 0 :
                    print("Formato invalido, digite un numero positivo")
                    continue
                break
            except BaseException as e:
                print(f"Error.formato invalido.{e}")

        while True:
            try:
                vendedor = int(input(f"Ingrese el tipo de vendedor, donde:\n          [1]->{type1}\n          [2]->{type2}\n          [3]->{type3}\n ¿Que tipo de vendedor es?: "))
                if vendedor < 1 or vendedor > 3:
                    print("Numero fuera de rango")
                    continue
                break
            except Exception as e:
                print(f"Error.formato invalido.{e}")
    
        if vendedor == 1:
            comision = contVentas*(0.2)
            print(f"{name} identificado con CC.{cedula} comisiono en el mes: ${comision:,.0f} COP")
        elif vendedor == 2:
            comision = contVentas*(0.15)
            print(f"{name} identificado con CC.{cedula} comisiono en el mes: ${comision:,.0f} COP")
        elif vendedor == 3:
            comision = contVentas*(0.25)
            print(f"{name} identificado con CC.{cedula} comisiono en el mes: ${comision:,.0f} COP")
        sumatoriaVentas += contVentas
        sumatoriaComisiones += comision
print("\n")                   
print("="*10,"INFORMES DEL MES","="*10)     
print(f"En el mes se vendio: ${sumatoriaVentas:,.0f} COP")
print(f"En el mes los empleados comisionaron : ${sumatoriaComisiones:,.0f} COP")