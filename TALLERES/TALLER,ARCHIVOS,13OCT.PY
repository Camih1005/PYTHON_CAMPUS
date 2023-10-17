#Escribir un programa que permita la creación 
# e introducción de los datos del personal de 
# la empresa (Id, Nombre, Edad, Sexo y 
# Teléfono) y almacene la información de 
# forma persistente. No se pueden almacenar 
# la información de una persona varias veces, 
# deben haber registros únicos por persona.
#
# Estructura de datos elegida:
# Lista de diccionarios
# [ {id1: {nombre:"", edad: , sexo: , Telefono},
#   {id2: {nombre:"", edad: , sexo: , Telefono},
#   {idn: {nombre:"", edad: , sexo: , Telefono}
# }]


import json

def buscarEmpleado(lstPersonal, idEmpl):
    # return dicEmpleados.get(idEmpl) != None
    return idEmpl in lstPersonal

def mnubuscarEmpleado(lst):
    print("\n\n3. Buscar Empleado\n")
    
    idEmpl = leerIDEmpl()
    existEmpl = buscarEmpleado(lstPersonal, idEmpl)
    if existEmpl == False:
        print("El Empleado con ese código no ha sido ingresado.")
        input()
        return
    
    print("\n", "=" * 30)
    print("Nombre:", lstPersonal[idEmpl]["Nombre"])
    print("Edad :", lstPersonal[idEmpl]["Edad"])
    print("Sexo:", lstPersonal[idEmpl]["Sexo (M/F)"])
    print(f"telefono:", lstPersonal[idEmpl]["Telefono"])
    input("\n Presione cualquier tecla para volver al menu...")
    
    
def leerNombreEmpl(lstPersonal,idEmpl):
    while True:
        try:
            nom = input("Ingrese el nombre del empleado:")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)    
            

def modificarEmpleado(lst, ruta):
    fd = open(ruta, "r")
    print("\n\n2. Modificar Empleado\n")
    idEmpl = leerIDEmpl()
    existEmpl = buscarEmpleado(lst, idEmpl)
    if existEmpl == False:
        print("El código del empleado no existe.")
        input()
        return
    
    print("\n")
    while True:
        op = int(input("\n1. Nombre\n2. Cantidad de Horas\n3. Valor de la hora\nOpcion? "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue
        break
    
    if op == 1:
        nombre = leerNombreEmpl()
        lstPersonal[idEmpl]["nombre"] = nombre
    elif op == 2:
        edad = leerHoraTrabEmpl()
        lstPersonal[idEmpl]["HorasTrabajadas"] = cantHoras
        
    elif op == 3:
        valHora = leerValHoraEmpl()
        lstPersonal[idEmpl]["ValorHora"] = valHora
    elif op == 4:
            
def guardarEmpleado(lstPersonal, ruta):
    # Función que guarda los datos de la lista de personal
    # en un arcivo JSON
    # Devuelve True: si los datos fueron guardados correctamente
    # Devuelve False: si los datos no se pudieron guardar
    
    try:
        fd = open(ruta, "w")
    except Exception as e:
        print("Error al abrir el archivo para guardar al empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        json.dump(lstPersonal, fd)
    except Exception as e:
        print("Error al guardar la información del empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.")
        input("Presione cualquier tecla para continuar\n")
        return False
    
    return True

def existeId(id, lstPersonal):
    #funcion que encuentra la posición de un id en la lista
    # Devuelve un número enterior >= 0 si el id existe
    # Devuelve un -1 si el id NO existe
    for i, datos in enumerate(lstPersonal):
        # El método enumerate () agrega un contador a un iterable y 
        # lo devuelve en forma de objeto de enumeración. 
        # Este objeto enumerado puede usarse directamente para bucles 
        # o convertirse en una lista de tuplas usando la función list().
        k = int(list(datos.keys())[0])
        if k == id:
            return i
    return -1

def borrarPersonal(lstPersonal, rutaFile):
    print("\n\n3. Borrar Personal")
    
    id = int(input("Ingrese el ID: "))
    if existeId(id, lstPersonal) == -1:
        # si existeId es -1 entonces no existe ese id en lstPersonal
        print("No existe un empleado con ese ID")
        input("Presione cualquier tecla para continuar\n")
        return None
    
    for i in range(len(lstPersonal)):
        datos = lstPersonal[i]
        k = int(list(datos.keys())[0])
        if k == id:
            del lstPersonal[i]
            break
    
    if guardarEmpleado(lstPersonal, rutaFile) == True:
        print("El empleado ha sido borrado con exito")
        input("Presione cualquier tecla para continuar\n")
    else:
        print("Ocurrio un error al borrar el empleado")
        input("Presione cualquier tecla para continuar\n")
    
        return None
    
    
def leerIDEmpl(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")
    
    
def agregarPersonal(lstPersonal, ruta):
    print("\n\n1. Agregar Personal")
    
    id = int(input("Ingrese el ID: "))
    while existeId(id, lstPersonal) != -1:
        # si existeId es -1 entonces no existe ese id en lstPersonal
        # si es diferente a -1, entonces el id y existe.
        print("--> Ya existe un empleado con ese ID")
        input("Presione cualquier tecla para continuar\n")
        id = int(input("\nIngrese el ID: "))
        
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo (M/F): ")
    telefono = input("Teléfono: ")
    
    dicEmpleado = {}
    dicEmpleado[id] = {"nombre":nombre, "edad":edad, "sexo":sexo, "telefono":telefono}
    lstPersonal.append(dicEmpleado)
    
    if guardarEmpleado(lstPersonal, ruta) == True:
        input("El empleado ha sido registrado con éxito.\nPresione cualquier tecla para continuar...")
    else:
        input("Ocurrio algún error al guardar el empleado.")

def menu():
    while True:
        try:
            print("\n" * 30)
            print("*** REGISTRO DEL PERSONAL ***".center(40))
            print("MENU".center(40))
            print("1. Agregar")
            print("2. Modificar")
            print("3. Eliminar")
            print("4. Ver")
            print("5. Salir")
            op = int(input(">>> Opción (1-5)? "))
            if op < 1 or op > 5:
                print("Opción no válida. Escoja de 1 a 5.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 5.")
            input("Presione cualquier tecla para continuar...")
            
def cargarInfo(lstPersonal, ruta):
    try:
        fd = open(ruta, "r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            input("Presione cualquier tecla para continuar\n")
            return None
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        input("Presione cualquier tecla para continuar\n")
        return None
    
    # print(lstPersonal)
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.\n", e, "\n")
        input("Presione cualquier tecla para continuar\n")
        return None
    return lstPersonal
    
# *** PROGRAMA PRINCIPAL ***
rutaFile = "/home/skylab-116/Documents/CCamilo/LoAprendido/ArchivosY_JSON/datpersonal.json"
lstPersonal = []
lstPersonal =cargarInfo(lstPersonal, rutaFile)
while True:
    op = menu()
    if op == 1:
        agregarPersonal(lstPersonal, rutaFile)
    elif op == 2:
        # Modificar
        pass
    elif op == 3:
        borrarPersonal(lstPersonal, rutaFile)
    elif op == 4:
        # Ver
        pass
    else:
        # Salir
        print("\nGracias por usar el programa")
        break