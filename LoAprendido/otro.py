while True:

    try:
        cedula = int(input("Ingrese su documento de identidad: \nsi desea salir del digite (-1): \n"))
        cedula = cedula.isdigit() == False
        continue
        if cedula == -1:
         break
        
    except Exception as e:
        print("Error al ingresar la cedula. Ingrese su cedula de nuevo:")