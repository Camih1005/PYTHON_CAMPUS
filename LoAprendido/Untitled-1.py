while True:
    try:
        nombre=(input("Ingrese un nombre"))
        if len(nombre) == 0 or nombre.isalnum()== False:   
            print("Nombre invalido. vuelva a digitarlo")
            continue
        break
    except Exception as e:
        print("Error al ingresar .\n", e)

#Validar codigo  
while True:
    try:
        cod= int(input("Ingrese el codigo :"))
       
        break
    except ValueError:
        print("Codigo invalido. Solo numeros")

            
#Validar programa academico
while True:
    try:
        prog_acad= int(input("""Programa academico al que pertenece:
                      1 -- Tecnico en Sistemas
                      2 -- Tecnico en Desarrollo de videojuegos
                      3 -- Tecnico en Animacion digital
                      """
                      ))
        if prog_acad < 1 or prog_acad > 3:
            print("EL programa no esta en el rango(1-3). INtente de nuevo")
            continue
        break
    except ValueError:
        print("Error. programa invalido.")

#Validar programa academico
while True:
    try:
        ind_beca= int(input("""Indicador de beca:
                      1 -- Beca por rendimiento academico. Descuento del 50[%] sobre el valor de la matricula
                      2 -- Beca cultural - Deportes. Descuentos del 40[%] sobre el valor de la matricula
                      3 -- Sin Beca
                     """
                    ))
                    
        if ind_beca< 1 or ind_beca > 3:
            print("la beca no esta en el rango(1-3). INtente de nuevo")
            continue
        break
    except ValueError:
        print("Error. beca invalido.")