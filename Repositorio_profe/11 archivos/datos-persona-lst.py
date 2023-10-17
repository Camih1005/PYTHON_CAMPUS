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
rutaFile = "Campus Lands\\Ciclo 1\\Grupo-C4-Sep\\Código\\11 archivos\\datpersonal.json"
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
