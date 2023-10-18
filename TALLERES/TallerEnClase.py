import json

def guardarEmpleado(lstlibros, ruta):
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
        json.dump(lstlibros, fd)
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

def buscarEmpleado(lstlibros, id):
    for i in range(len(lstlibros)):
        if (lstlibros[i][0] == id):
            return i

    return -1

def existeId(id, lstlibros):
    #funcion que encuentra la posición de un id en la lista
    # Devuelve un número enterior >= 0 si el id existe
    # Devuelve un -1 si el id NO existe
    for i, datos in enumerate(lstlibros):
        # El método enumerate () agrega un contador a un iterable y 
        # lo devuelve en forma de objeto de enumeración. 
        # Este objeto enumerado puede usarse directamente para bucles 
        # o convertirse en una lista de tuplas usando la función list().
        k = int(list(datos.keys())[0])
        if k == id:
            return i
    return -1

def borrarLibro(lstlibros, rutaFile):
    print("\n\n3. Borrar Libro")
    
    id = int(input("Ingrese el ID: "))
    if existeId(id, lstlibros) == -1:
        # si existeId es -1 entonces no existe ese id en lstPersonal
        print("No existe un empleado con ese ID")
        input("Presione cualquier tecla para continuar\n")
        return None
    
    for i in range(len(lstlibros)):
        datos = lstlibros[i]
        k = int(list(datos.keys())[0])
        if k == id:
            del lstlibros[i]
            break
    
    if guardarEmpleado(lstlibros, rutaFile) == True:
        print("El empleado ha sido borrado con exito")
        input("Presione cualquier tecla para continuar\n")
    else:
        print("Ocurrio un error al borrar el empleado")
        input("Presione cualquier tecla para continuar\n")
        return None

def Listar_libros(rutaFile):
    try:
        with open(rutaFile,encoding="UTF-8" 'r') as json_file:
            data = json.load(json_file)
            libros = data.get("libros", [])

            if libros:
                i = 0
                while i < len(libros):
                    for j in range(i, min(i + 3, len(libros))):
                        libro = libros[j]
                        titulo = libro.get("titulo", "Título no disponible")
                        autor = libro.get("autor", "Autor no disponible")
                    i += 3

                    if i < len(libros):
                        input("Presiona Enter para ver más libros...")

                print("No hay más libros para mostrar.")

            else:
                print("No se encontraron libros en el archivo JSON.")

    except FileNotFoundError:
        print("El archivo JSON no existe.")
    except json.JSONDecodeError:
        print(f"El archivo JSON no es válido.")
    except Exception as e:
        print("Ocurrió un error")

# Llama a la función y pasa el nombre del archivo JSON como argumento
archivo_json = "tu_archivo.json"
Listar_libros(archivo_json)    
    
    
def agregarPersonal(lstlibros, ruta):
    print("\n\n1. Agregar libro")
    
    id = int(input("Ingrese el ID: "))
    while existeId(id, lstlibros) != -1:
        # si existeId es -1 entonces no existe ese id en lstPersonal
        # si es diferente a -1, entonces el id y existe.
        print("--> Ya existe un libro con ese ID")
        input("Presione cualquier tecla para continuar\n")
        id = int(input("\nIngrese el ID: "))
        
    nombre = input("Titulo_libro: ")
    autor =(input("Autor: "))
    precio= int(input("Precio: "))

    
    dicLibreria = {}
    dicLibreria[id] = {"nombre":nombre, "autor":autor, "precio":precio}
    lstlibros.append(dicLibreria)
    
    if guardarEmpleado(lstlibros, ruta) == True:
        input("El libro ha sido registrado con exito.\nPresione cualquier tecla para continuar...")
    else:
        input("Ocurrio algún error al guardar el empleado.")

def menu():
    while True:
        try:
            print("\n" * 30)
            print("*** LIBRERIA CAMILO ***".center(40))
            print("MENU".center(40))
            print("1. INSERTAR LIBRO")
            print("2. MODIFICAR LIBRO")
            print("3. ELIMINAR LIBRO")
            print("4. LISTAR LIBROS ")
            print("5. Salir")
            op = int(input(">>> Opción (1-5)? "))
            if op < 1 or op > 5:
                print("Opción no válida. Escoja de 1 a 5.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a .")
            input("Presione cualquier tecla para continuar...")
            
def cargarInfo(lstLibros, ruta):
    try:
        fd = open(ruta, encoding="UTF-8" "r" )
    except Exception as e:
        try:
            fd = open(ruta, encoding="UTF-8" "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            input("Presione cualquier tecla para continuar\n")
            return None
    try:
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
    
    # print(lstPersonal)
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.\n", e, "\n")
        input("Presione cualquier tecla para continuar\n")
        return None
    return lstLibros
    
# *** PROGRAMA PRINCIPAL ***
rutaFile = "/home/spukN01-/Documents/CCamilo/CAMPUS_REPOSITORIO/TALLERES/LIBRERIA.json"
lstlibros = []
lstlibros =cargarInfo(lstlibros, rutaFile)
while True:
    op = menu()
    if op == 1:
        agregarPersonal(lstlibros, rutaFile)
    elif op == 2:
        # Modificar
        pass
    elif op == 3:
        borrarLibro(lstlibros, rutaFile)
    elif op == 4:
        Listar_libros(rutaFile)
    else:
        # Salir
        print("\nGracias por usar el programa")
        break
