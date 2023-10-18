# Este programa está destinado para ACME, (empresa mencionado en el ejercicio) donde se podrá
# realizar multiples acciones, como agregar, modificar o eliminar usuarios del sistema. Todo 
# esto lleva al enfoque principal, que es el de gestionar la nómina de sus empleados.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
listaEmpleados = []
smmlv = 1160000
subsidioTransporte = 140606


# DECLARANDO LAS FUNCIONES COMPLEMENTARIAS
def filtrarTexto(text):
    nombre = input(text).strip()
    nombreArray = nombre.split(" ")
    nombreArrayFiltrado = []
    
    for n in nombreArray:
        if n != "":
            nombreArrayFiltrado.append(n)
    
    nombreFiltradoValidar = "".join(nombreArrayFiltrado).lower()
    nombreFinal = " ".join(nombreArrayFiltrado).title()
    
    return [nombreArray, nombreArrayFiltrado, nombreFiltradoValidar, nombreFinal]


def encontrarEmpleado(msj, min):
    try:
        idBuscar = validarId(msj, min)
        
        if idBuscar == 0:
            return [idBuscar]
        
        for i in range(len(listaEmpleados)):
            for j in range(len(listaEmpleados[i])):
                if listaEmpleados[i][j] == idBuscar:
                    posicion1 = i
                    posicion2 = j
                    checked = True
        
        return [idBuscar, posicion1, posicion2, checked]
    
    except Exception as e:
        print("\nHa ocurrido un error durante la ejecución del programa. Inténtelo de nuevo.")
        print(f"Error: {e}")
        
        input("\nPresione cualquier tecla para salir al menú...")
        return False


def existenEmpleados():
    cantidadEmpleados = len(listaEmpleados)
    
    if cantidadEmpleados == 0:
        return False
    elif cantidadEmpleados >= 1:
        return True


def listarEmpleadosPaginacion(list, cant, count, iterado):
    continuar = True
    cantidadEmpleadosLista = len(list)
    
    while continuar:
        while count < cant:
            for i in range(count, len(list)):
                id, nombre, hrsLab, valHrs = list[i]
                print("{:<14} {:<30} {:<18} {:<15}".format(id, nombre, f"{hrsLab} hrs", f"${valHrs:,.0f} COP"))
                count += 1
                
                if count == 5 * iterado:
                    return count
                
                if count == cantidadEmpleadosLista:
                    return True


def calcularNomina(posicion1):
    descuentoEPS = 4
    descuentoPension = 4
    
    #Salario Bruto
    hrsLaboradas = listaEmpleados[posicion1][2]
    valorhrs = listaEmpleados[posicion1][3]
    salarioBruto = valorhrs * hrsLaboradas
    
    
    #Salario Neto
    salarioBruto -= (salarioBruto * descuentoEPS) / 100
    salarioBruto -= (salarioBruto * descuentoPension) / 100
    
    #Verificar si el empleado aplica para el subsidio de transporte
    if salarioBruto < smmlv:
        salarioNeto = salarioBruto + subsidioTransporte
        return salarioNeto
    
    elif salarioBruto > smmlv:
        salarioNeto = salarioBruto
        return salarioNeto


# DECLARANDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcion = int(input(msj))
            
            if opcion < int(min) or opcion > int(max):
                print(f"Error: Ingresa un valor numérico válido ({min}-{max}).\n")
                continue
            return opcion
        
        except ValueError:
            print("Ha ocurrio un error al ingresar su opción. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrio un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarId(idEmpl, min):
    while True:
        try:
            id = int(input(idEmpl))
            
            if id < int(min):
                print(f"Error: Debes ingresar un número igual o superior a {min}\n")
                continue
            return id
        
        except ValueError:
            print("Ha ocurrido un error al registrar el ID. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrio un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")
    
    # QUEDÉ AQUÍ


def validarNombre(msj):
    while True:
        try:
            nombreArray, nombreArrayFiltrado, nombreFiltradoValidar, nombreFinal = filtrarTexto(msj)
            
            if len(nombreArray) < 2:
                print(f"Error: Debes ingresar al menos 1 nombre y 1 apellido.\n")
                continue

            elif len(nombreFiltradoValidar) == 0:
                print("Error: Has ingresado un nombre vacío.")
                continue
                
            elif not nombreFiltradoValidar.isalnum():
                print("Error: El nombre no puede tener caracteres especiales.\n")
                continue
            
            elif nombreFiltradoValidar.isdigit():
                print("Error: El nombre no puede contener solo números.\n")
                continue
            return nombreFinal
        
        except Exception as e:
            print("Ha ocurrido un error al ingresar el nombre. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrio un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarHorasTrabajadas(hrs, min, max):
    while True:
        try:
            horas = int(input(hrs))
            
            if horas < int(min) or horas > int(max):
                print(f"Error: Ingrese un valor numérico positivo dentro del rango permitido ({min}-{max})\n")
                continue
            return horas
        
        except ValueError:
            print("Ha ocurrido un error al ingresar las horas laboradas. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrio un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarValorHora(valHr, min, max):
    while True:
        try:
            valorHora = float(input(valHr))
            
            if valorHora < int(min) or valorHora > int(max):
                print(f"Error: Ingrese un valor válido dentro del rango permitido (${min} - ${max}).\n")
                continue
            return valorHora
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el valor de la hora laboral. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrio un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


# DECLARANDO LAS FUNCIONES NECESARIAS
def menu(msj):
    print("\n\n", "*** NOMINA ACME ***")
    print(" " * 8, "MENÚ")
    
    print("\n1. Agregar empleado")
    print("2. Modificar empleado")
    print("3. Buscar empleado")
    print("4. Eliminar empleado")
    print("5. Listar empleados")
    print("6. Listar nómina de un empleado")
    print("7. Listar nómina de todos los empleados")
    print("8. Salir")
    
    return validarOpcionUsuario(msj, 1, 8)


def agregarEmpleado(idEmpl, nombreEmpl, hrsTrabajoEmpl, valorHoraEmpl):
    print("\n", "*** AGREGAR EMPLEADO ***")
    print("Ingrese la siguiente información sobre el nuevo empleado:")
    
    id = validarId(idEmpl, 1)
    nombre = validarNombre(nombreEmpl)
    horasTrabajadas = validarHorasTrabajadas(hrsTrabajoEmpl, 1, 160)
    valorHora = validarValorHora(valorHoraEmpl, 8000, 150000)
    
    listaEmpleados.append([id, nombre, horasTrabajadas, valorHora])
    print("\n", id, nombre, horasTrabajadas, valorHora)
    print(listaEmpleados)


def modificarEmpleado(msj):
    continuar = True
    cantidadEmpleados = existenEmpleados()
    print("\n\n", "*** MODIFICAR EMPLEADO ***")
    
    # Validar si existe algún empleado añadido a la lista de empleados.
    if not cantidadEmpleados:
        print("Error: Imposible acceder a este sub-programa.")
        print("Motivo: No hay usuarios añadidos al sistema.")
        input()
        return
        
        
    while continuar:
        print("\n¿Qué información del empleado desea modificar?")
        print("1. Modificar el nombre")
        print("2. Modificar las horas trabajadas")
        print("3. Modificar el valor de la hora")
        opcionUsuario = validarOpcionUsuario(msj, 0, 3)
        
        if opcionUsuario == 0:
            break
        
        # Listar los empleados a modificar
        print("\n{:<7} {:<14} {:<30}".format("N°", "ID", "Nombre"))
        
        for i in range(len(listaEmpleados)):
            print("{:<7} {:<14} {:<30}".format(f"{i+1}", listaEmpleados[i][0], listaEmpleados[i][1]))
            
        elegirEmpleado = validarOpcionUsuario("\n  >> ¿Cuál es el número (N°) del empleado a modificar? Escriba 0 para salir al submenú: ", 0, i+1)
        
        
        # Verificar que el usuario no haya desistido
        if elegirEmpleado == 0:
            continue
        
        
        # Modificar el nombre de un empleado        
        if opcionUsuario == 1:
            print(f"\nNombre anterior: {listaEmpleados[elegirEmpleado-1][1]}")
            nuevoNombre = validarNombre("Nuevo nombre: ")
            
            listaEmpleados[elegirEmpleado-1][1] = nuevoNombre
        
        # Modificar las horas trabajadas de un empleado
        elif opcionUsuario == 2:
            print(f"\nHoras trabajadas anterior: {listaEmpleados[elegirEmpleado-1][2]}")
            nuevasHorasTrabajadas = validarHorasTrabajadas("Nueva cantidad de horas trabajadas: ", 1, 160)
            
            listaEmpleados[elegirEmpleado-1][2] = nuevasHorasTrabajadas
            
        # Modificar el valor de la hora de un empleado
        elif opcionUsuario == 3:
            print(f"\nValor de la Hora anterior: ${listaEmpleados[elegirEmpleado-1][3]:,.0f} COP")
            nuevoValorHora = validarHorasTrabajadas("Nuevo valor de la hora para el empleado: $", 8000, 150000)
            
            listaEmpleados[elegirEmpleado-1][3] = nuevoValorHora
        
        # Validar si el usuario desea modificar otro usuario
        continuarModificar = validarOpcionUsuario("¿Deseas modificar algún otro usuario? (1 SI / 0 NO): ", 0, 1)
        
        if continuarModificar == 1:
            continuar = True
        elif continuarModificar == 0:
            continuar = False


def buscarEmpleado(msj, validar):
    continuar = True
    cantidadEmpleados = existenEmpleados()
    
    # Condicional if-else para que muestre o no el mensaje del sub-programa al iniciarse
    if validar:
        pass
    else:
        print("\n\n", "*** BUSCAR EMPLEADO ***")
        
    # Validar si existe algún empleado añadido a la lista de empleados.
    if not cantidadEmpleados:
        print("Error: Imposible acceder a esta parte del programa.")
        print("Motivo: No hay usuarios añadidos al sistema.")
        input()
        return None
    
    while continuar:
        retornarIdEmpleado = validar
        valorRetornado = encontrarEmpleado(msj, 0)
        
        if not valorRetornado:
            return
        
        else:
        
            if len(valorRetornado) == 1:
                idBuscar, = valorRetornado
            
            else:
                idBuscar, posicion1, posicion2, checked = valorRetornado
            
            
            # Verifica si el usuario desea salir o no del sub-programa
            if idBuscar == 0:
                continuar = False
                return None
                    
            
            # Comprueba si el ID ingresado existe en el sistema      
            if not checked:
                print(f"\nEl empleado con el ID '{idBuscar}' no ha sido ingresado.")
                continue
            
            else:
                if retornarIdEmpleado:
                    return [idBuscar, posicion1, posicion2]
                
                # En caso de que no se quiera eliminar un usuario entonces buscará el usuario.
                else:
                    idInfo, nombreInfo, horasTrabajadasInfo, valorHoraInfo = listaEmpleados[posicion1]
                    
                    print(f"\n=== ID {idInfo} ===")
                    print("Nombre:", nombreInfo)
                    print(f"Horas trabajadas: {horasTrabajadasInfo} hrs")
                    print(f"Valor de la hora: ${valorHoraInfo:,.0f} COP")
                    input()
        
        
        continuarBuscar = validarOpcionUsuario("¿Desea buscar otro empleado? (1 SI / 0 NO): ", 0, 1)
        
        if continuarBuscar == 1:
            continuar = True
        elif continuarBuscar == 0:
            continuar = False


def eliminarEmpleado(msj, validar):
    continuar = True
    print("\n", "*** ELIMINAR EMPLEADO ***")
    
    while continuar:
        empleadoEliminado = buscarEmpleado(msj, validar)
        
        if empleadoEliminado == None:
            return
        
        else:
            # Pequeña validación para asegurarse que no hayan errores (Poco probable, pues ya se valida
            # información antes de entrar por esta nueva validación).
            while True:
                try:
                    idBuscar, posicion1, posicion2 = empleadoEliminado
                    elementoEliminado = listaEmpleados.pop(posicion1)
                    
                    if len(elementoEliminado) == 0 or not elementoEliminado:
                        print("El usuario no se ha eliminado como debía. Inténtelo de nuevo.")
                        continue
                    break
                
                except Exception as e:
                    print("Mensaje de Error:", {e})
        
        print(f"\n¡El empleado '{elementoEliminado[1]}' con ID de '{elementoEliminado[0]}' ha sido eliminado correctamente!")
        
        
        # Determinar si el usuario desea continuar eliminando empleados del sistema.
        continuarEliminar = validarOpcionUsuario("¿Desea eliminar otro empleado? (1 SI / 0 NO): ", 0, 1)
        
        if continuarEliminar == 1:
            continuar = True
        elif continuarEliminar == 0:
            continuar = False
    
    return elementoEliminado


def listarEmpleados():
    continuar = True
    checked = False
    cantidadEmpleados = existenEmpleados()
    print("\n\n", "*** LISTAR EMPLEADOS ***")
    
    # Validar si existe algún empleado añadido a la lista de empleados.
    if not cantidadEmpleados:
        print("\nError: Imposible acceder a este sub-programa.")
        print("Motivo: No hay usuarios añadidos al sistema.")
        input()
        return

    
    while continuar:
        print("\n{:<14} {:<30} {:<18} {:<15}".format("ID", "Nombre", "Horas laboradas", "Valor hora"))
        count = 0
        iterado = 1
        
        if len(listaEmpleados) > 5:
            while True:
                # La variable contador almacenará el retorno de la función (Número o booleano)
                # Si es número, significa que aún queda elementos por mostrar y se prepara una nueva paginación
                # Pero si recibe un booleano (True), entonces significa que se han mostrado todos los empleados, regresando al menú.
                contador = listarEmpleadosPaginacion(listaEmpleados, len(listaEmpleados), count, iterado)
                
                # Este if permite que se salga del sub-programa cuando ya no hayan más elementos por mostrar
                if contador == True:
                    input()
                    return
                
                else:
                    # Verificar si el usuario desea continuar con la paginación de más información.
                    continuarMostrarInfo = validarOpcionUsuario("\n¿Desea ver más información? (1 SI / 0 NO): ", 0, 1)
                    if continuarMostrarInfo == 1:
                        iterado += 1
                        count += contador
                        continue
                
                    # Sale de la función si el usuario desiste en ver más empleados
                    elif continuarMostrarInfo == 0:
                        return False
        
        elif len(listaEmpleados) <= 5:
            for i in range(len(listaEmpleados)):
                id, nombre, hrsLab, valHrs = listaEmpleados[i]
                print("{:<14} {:<30} {:<18} {:<15}".format(id, nombre, f"{hrsLab} hrs", f"${valHrs:,.0f} COP"))
                checked = True

        # Se ejecuta este if solo si el for anterior se ha completado exitosamente
        if checked:
            input()
            continuar = False
            return
            

def listarNominaEmpleado(msj, validar):
    continuar = True
    print("\n", "*** LISTAR LA NÓMINA DE UN EMPLEADO ***")
    
    while continuar:
        valorRetorno = buscarEmpleado(msj, validar)
        
        if not valorRetorno:
            return False
        
        else:
            idEmpleado, posicion1, posicion2 = valorRetorno
            nominaResultado = calcularNomina(posicion1)
            
            
            for i in range(0, 5):
                try:
                    listaEmpleados[posicion1]
                    listaEmpleados[posicion1][4] = nominaResultado
                
                except IndexError:
                    listaEmpleados[posicion1].append(nominaResultado)
            
            id, nombre, horasTrabajadas, valorHora, valorNomina = listaEmpleados[posicion1]
            
            print("\n", f"==== {idEmpleado} ====")
            # print(nominaResultado)
            
            print(f"\nID: {id}")
            print(f"Nombre: {nombre}")
            print(f"Horas Trabajadas: {horasTrabajadas} hrs")
            print(f"Valor Hora: ${valorHora:,.0f} COP")
            print(f"Valor nómina: ${valorNomina:,.0f} COP\n")


def listarNominas():
    valorNominaTotal = 0
    empleadosCantidad = 0
    descuentoEPS = 4
    descuentoPension = 4
    cantidadEmpleados = existenEmpleados()
    
    if not cantidadEmpleados:
        print("Error: Imposible acceder a esta parte del programa.")
        print("Motivo: No hay usuarios añadidos al sistema.")
        input()
        return None
    
    
    print("\n", "*** LISTAR NÓMINA DE TODOS LOS EMPLEADOS ***")
    
    for i in range(len(listaEmpleados)):
        #Salario Bruto
        hrsLaboradas = listaEmpleados[i][2]
        valorhrs = listaEmpleados[i][3]
        salarioBruto = valorhrs * hrsLaboradas
        
        #Salario Neto
        salarioBruto -= (salarioBruto * descuentoEPS) / 100
        salarioBruto -= (salarioBruto * descuentoPension) / 100
        
        #Verificar si el empleado aplica para el subsidio de transporte
        if salarioBruto < smmlv:
            salarioNeto = salarioBruto + subsidioTransporte
        
        elif salarioBruto > smmlv:
            salarioNeto = salarioBruto
        
        for j in range(0, 5):
            try:
                listaEmpleados[i]
                listaEmpleados[i][4] = salarioNeto
            
            except IndexError:
                listaEmpleados[i].append(salarioNeto)
                
    
        id, nombre, horasTrabajadas, valorHora, valorNomina = listaEmpleados[i]
        print("\n", f"==== {id} ====")
        
        print(f"\nID: {id}")
        print(f"Nombre: {nombre}")
        print(f"Horas Trabajadas: {horasTrabajadas} hrs")
        print(f"Valor Hora: ${valorHora:,.0f} COP")
        print(f"Valor nómina: ${valorNomina:,.0f} COP\n")
        print("-" * 35)
        
        valorNominaTotal += valorNomina
        empleadosCantidad += 1
    
    print(f"Valor total de las nóminas de los empleados: ${valorNominaTotal:,.0f} COP")
    print(f"La cantidad de empleados contados fue de: {empleadosCantidad:.0f} empleados")


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Ingrese una opción (1-8): ")
    
    if opcionUsuario == 1:
        agregarEmpleado("ID: ", "Nombre: ", "Horas Trabajadas: ", "Valor de la Hora: ")
    
    elif opcionUsuario == 2:
        modificarEmpleado("  >> Elija una opción (1-3) o elija 0 para salir al menú: ")
    
    elif opcionUsuario == 3:
        buscarEmpleado("Ingrese el ID del empleado a buscar (Escriba 0 para volver al menú): ", False)
    
    elif opcionUsuario == 4:
        eliminarEmpleado("Ingrese el ID del empleado que desea eliminar (Escriba 0 para volver al menú): ", True)
    
    elif opcionUsuario == 5:
        listarEmpleados()
    
    elif opcionUsuario == 6:
        listarNominaEmpleado("Ingrese el ID del empleado al que desea conocer la nómina: (Escriba 0 para volver al menú): ", True)
    
    elif opcionUsuario == 7:
        listarNominas()
    
    elif opcionUsuario == 8:
        salirOpcion = validarOpcionUsuario("\n  >> ¿Está seguro que desea salir del programa? (1 SI / 0 NO): ", 0, 1)
        
        if salirOpcion == 1:
            print("\n¡Gracias por usar nuestro software! Saliendo...")
            isVerdadero = False
        
        elif salirOpcion == 0:
            isVerdadero = True