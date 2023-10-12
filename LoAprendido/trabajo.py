def listarEmpl():
    for i in range(len(dicEmpleado)):
        imprimirempleado(i)


def eliminarEmp(indx):
    print(indx)
    dicEmpleado.remove(dicEmpleado[indx][0])
    dicEmpleado.remove(dicEmpleado[indx][1])
    dicEmpleado.remove(dicEmpleado[indx][2])
    dicEmpleado.remove(dicEmpleado[indx][3])

    print("Usuario eliminado")

    return


def imprimirempleado(indx):
    print(dicEmpleado[indx][0])
    print(dicEmpleado[indx][1])
    print(dicEmpleado[indx][2])
    print(dicEmpleado[indx][3])

    return

def leerValHoraEmpl():
    while True:
        try:
            n = int(input("Ingrese el valor de la hora trabajada del empleado: "))
            if n < 8000 or n > 150000:
                print("Valor de la Hora inválida. Debe estar en el rango de [8000, 150000]")
                continue
            return n
        except ValueError:
            print("Error al ingresar el valor de la hora trabajada.")

def leerHoraTrabEmpl():
    while True:
        try:
            n = int(input("Ingrese la horas trabajadas del empleado: "))
            if n < 0 or n > 160:
                print("Horas inválidas. Debe estar en el rango de [0, 160]")
                continue
            return n
        except ValueError:
            print("Error al ingresar las horas.")

def leerNombreEmpl():
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

def leerIDEmpl():
    while True:
        try:
            n = int(input("Ingrese el ID del empleado: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")
            
def buscarEmpleado(dicEmpleado, idEmpl):
    for i in range(len(dicEmpleado)):
        if (dicEmpleado[i][0] == idEmpl):
            return i

    return -1


def modificarEmpleado(dicEmpleado):
    print("\n\n2. Modificar Empleado\n")
    
    idEmpl = leerIDEmpl()
    posEmpl = buscarEmpleado(dicEmpleado, idEmpl)
    if posEmpl == -1:
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
        dicEmpleado[posEmpl][1] = nombre
    elif op == 2:
        cantHoras = leerHoraTrabEmpl()
        dicEmpleado[posEmpl][2] = cantHoras
    elif op == 3:
        valHora = leerValHoraEmpl()
        dicEmpleado[posEmpl][3] = valHora

def agregarEmpleado(dicEmpleado):
    print("\n\n*** 1. Agregar empleado\n")
    lstDatos = []
    id = leerIDEmpl()
    if buscarEmpleado(dicEmpleado, id) != -1:
        print("El id ya existe en la lista")
        input()
        return
    
    lstDatos.append(id)
    lstDatos.append(leerNombreEmpl())
    lstDatos.append(leerHoraTrabEmpl())
    lstDatos.append(leerValHoraEmpl())
    
    dicEmpleado.append(lstDatos)

def menu():
    while True:
        try:
            print("*** NOMINA ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar empleado")
            print("2. Modificar empleado")
            print("3. Buscar emplado")
            print("4. Eliminar empleado")
            print("5. Listar empleados")
            print("6. Listar nómina de un empleado")
            print("7. Listar nómina de todos los empleados")
            print("8. Salir")
            op = int(input(">>> Opción (1-8)? "))
            if op < 1 or op > 8:
                print("Opción no válida. Escoja de 1 a 8.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 8.")
            input("Presione cualquier tecla para continuar...")

## PROGRAMA PRINCIPAL
dicEmpleado= []
while True:
    op = menu()
    if op == 1:
        agregarEmpleado(dicEmpleado)
        print(dicEmpleado)
        input()
    elif op == 2:
        modificarEmpleado(dicEmpleado)
    elif op == 3:
        ind = leerIDEmpl()
        indx = buscarEmpleado(dicEmpleado,ind)

        if(indx!=-1):
            imprimirempleado(indx)
        
    elif op == 4:
        ind = leerIDEmpl()
        indx = buscarEmpleado(dicEmpleado,ind)
        print(indx)       
        if(indx!=-1):
            eliminarEmp(indx)
    elif op== 5:
        listarEmpl()

    
    elif op == 8:
        print("\n\nGracias por usar el software. Adios")
        break