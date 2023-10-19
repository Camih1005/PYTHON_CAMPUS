import json

def modificarLibro(lstLibros, rutaFile):
    print("\n\n2. Editar Libro")
    
    codigo = input("Ingrese el ID del libro a modificar: ")
    empleado_codigox = existeId(codigo, lstLibros)
    
    if empleado_codigox == -1:
        print("No existe un empleado con ese ID")
        input("Presione cualquier tecla para continuar\n")
        return
    
    libro_actual = lstLibros[empleado_codigox][codigo]
    print("Datos actuales del libro:")
    print("Codigo:", codigo)
    print("Titulo:", libro_actual["titulo"])
    print("Autor:", libro_actual["autor"])
    print("Precio:", libro_actual["precio"])
    
    
    nuevo_titulo = input("Nuevo titulo: ")
    nuevo_autor = input("Nueva autor: ")
    nuevo_precio = float(input("Nuevo precio: "))
    
    lstLibros[empleado_codigox][codigo] = {
        "titulo": nuevo_titulo,
        "autor": nuevo_autor,
        "precio": nuevo_precio,
    }
    
    if guardarLibro(lstLibros, rutaFile):
        print("Los datos del libro han sido modificados con éxito")
    else:
        print("Ocurrió un error al modificar los datos del libro")
    
    input("Presione cualquier tecla para continuar\n")

def guardarLibro(lstLibros, ruta):
    # Función que guarda los datos de la lista de personal
    # en un arcivo JSON
    # Devuelve True: si los datos fueron guardados correctamente
    # Devuelve False: si los datos no se pudieron guardar
    
    try:
        fd = open(ruta, "w")
    except Exception as e:
        print("Error al abrir el archivo para guardar el libro.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        json.dump(lstLibros, fd)
    except Exception as e:
        print("Error al guardar la información del libro.\n", e)
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

def existeId(codigo, lstLibros):
    #funcion que encuentra la posición de un codigo en la lista
    # Devuelve un número enterior >= 0 si el codigo existe
    # Devuelve un -1 si el codigo NO existe
    for i, datos in enumerate(lstLibros):
        # El método enumerate () agrega un contador a un iterable y 
        # lo devuelve en forma de objeto de enumeración. 
        # Este objeto enumerado puede usarse directamente para bucles 
        # o convertirse en una lista de tuplas usando la función list().
        k = list(datos.keys())[0]
        if k == codigo:
            return i
    return -1

def borrarLibro(lstLibros, rutaFile):
    print("\n\n3. Borrar Libro")
    codigo = input("Ingrese el codigo: ")
    poscod = existeId(codigo, lstLibros)
    if poscod == -1:
        # si existeId es -1 entonces no existe ese codigo en lstLibros
        print("No existe un libro con ese codigo")
        input("Presione cualquier tecla para continuar\n")
        return None
    
    del lstLibros[poscod]
    
    if guardarLibro(lstLibros, rutaFile) == True:
        print("El libro ha sido borrado con exito")
        input("Presione cualquier tecla para continuar\n")
    else:
        print("Ocurrio un error al borrar el libro")
        input("Presione cualquier tecla para continuar\n")
        return None
    
# def verLibros(lstLibros):
    
def agregarPersonal(lstLibros, ruta):
    print("\n\n1. Agregar Libro")
    
    codigo = int(input("Ingrese el codigo: "))
    while existeId(codigo, lstLibros) != -1:
        # si existeId es -1 entonces no existe ese codigo en lstLibros
        # si es diferente a -1, entonces el codigo y existe.
        print("--> Ya existe un libro con ese ID")
        input("Presione cualquier tecla para continuar\n")
        codigo = input("\nIngrese el ID: ")

    titulo = input("Titulo: ")
    autor = input("Autor: ")
    precio = float(input("Precio: "))
    
    dicLibros = {}
    dicLibros[codigo] = {"codigo":codigo, "titulo":titulo, "autor":autor, "precio":precio}
    lstLibros.append(dicLibros)
    
    if guardarLibro(lstLibros, ruta) == True:
        input("El libro ha sido registrado con éxito.\nPresione cualquier tecla para continuar...")
    else:
        input("Ocurrio algún error al guardar el libro.")

def menu():
    while True:
        try:
            print("\n" * 30)
            print("*** REGISTRO DE LIBROS ***".center(40))
            print("MENU".center(40))
            print("1. Insertar")
            print("2. Consultar")
            print("3. Editar")
            print("4. Borrar")
            print("5. Listar")
            print("6. Salir")
            op = int(input(">>> Opción (1-5)? "))
            if op < 1 or op > 5:
                print("Opción no válida. Escoja de 1 a 5.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 5.")
            input("Presione cualquier tecla para continuar...")
            
def cargarInfo(lstLibros, ruta):
    try:
        fd = open(ruta, "r")
    except Exception as e:
        try:
            fd = open(ruta, "w+")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            input("Presione cualquier tecla para continuar\n")
            return None
    try:
        if fd.closed:
            fd = open(ruta, "r")
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstLibros = json.load(fd)
        else:
            lstLibros = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        input("Presione cualquier tecla para continuar\n")
        return None
    
    # print(lstLibros)
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.\n", e, "\n")
        input("Presione cualquier tecla para continuar\n")
        return None
    return lstLibros
    
# *** PROGRAMA PRINCIPAL ***
rutaFile = "datlibro.json"
lstLibros = []
lstLibros =cargarInfo(lstLibros, rutaFile)
while True:
    op = menu()
    if op == 1:
        agregarPersonal(lstLibros, rutaFile)
    elif op == 2:
        pass
    elif op == 3:
        modificarLibro(lstLibros, rutaFile)
    elif op == 4:
        borrarLibro(lstLibros, rutaFile)
        # borrar
        pass
    else:
        # Salir
        print("\nGracias por usar el programa")
        break