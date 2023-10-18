# Este programa está destinado para ACME, (empresa mencionado en el ejercicio) donde se podrá
# realizar multiples acciones, como agregar, modificar o eliminar usuarios del sistema. Todo 
# esto lleva al enfoque principal, que es el de gestionar la nómina de sus empleados.


# DECLARANDO LAS VARIABLES PRINCIPALES
isVerdadero = True
dictEmpleados = {}
smmlv = 1160000
subsidioTransporte = 140606


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS
def filtrarTexto(texto):
    textoArray = texto.split(" ")
    textoFiltradoArray = []
    
    for i in range(len(textoArray)):
        if textoArray[i] != "":
            textoFiltradoArray.append(textoArray[i])
    
    return textoFiltradoArray


def existeId(id):
    validarExisteId = dictEmpleados.get(id)
    
    if validarExisteId == None:
        return False
    else:
        return True


def recuperarInfoId(msj, min):
    # En caso de ingresarse un ID no registrado, se volverá a repetir este bucle a no ser que encuentre un ID o el usuario decida salir de la función.
    
    while True:    
        # Validación similar a la función "validarId()" adaptada a solo recolectar información según el ID dado.
        while True:
            try:
                buscarInfoEmpleado = int(input(msj))
                
                if buscarInfoEmpleado < min:
                    print("Error: El ID ingresado tiene un formato inválido. Inténtelo de nuevo.\n")
                    continue
                break
            
            except ValueError:
                print("Ha ocurrido un error al ingresar el ID del empleado. Inténtelo de nuevo.\n")
            except:
                print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")

        
        # Si "buscarInfoEmpleado" es igual a 0, entonces el usuario ha optado por regresar al menú principal aún estando dentro del sub-programa de "buscarEmpleado()"
        if buscarInfoEmpleado == 0:
            input("Regresando al menú principal. Presione cualquier tecla para continuar...")
            return False
        
        # En caso de que "buscarInfoEmpleado" sea mayor a 0, entonces queda verificar si existe el ID
        else:
            # Recuperar información del empleado
            validarExisteId = existeId(buscarInfoEmpleado)
            
            if validarExisteId:
                obtenerValoresInfo = dictEmpleados.get(buscarInfoEmpleado)
                return [buscarInfoEmpleado, list(obtenerValoresInfo.values())]
            else:
                print("Error: El ID ingresado no existe en el sistema. Ingrese un ID que esté registrado.\n")
                continue


#Función sin funcionamiento alguno en la primera versión. Futuro funcionamiento.
def sumarValorNominas(nomina):
    sumarNominas = 0
    for i in range(len(nomina)):
        sumarNominas += nomina[i]
    
    return sumarNominas
        

# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < min or opcionUsuario > max:
                print(f"Error: Debes elegir una opción dentro del rango válido ({min}-{max}).\n")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la opción elegida. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarId(msj, min, checked=False):
    while True:
        try:
            id = int(input(msj))
            existeIdEmpleado = existeId(id)
            
            if checked:
                pass
                # El pass es con el fin de evitar la validación de si existe un ID específico, pues se quiere que valide que el ID ingresado sea válido pero que no valide si ya existe o no.
            else:
                if existeIdEmpleado:
                    print(f"Error: El id '{id}' ya existe.\n")
                    continue
                
                else:
                    if id < min:
                        print(f"Error: El ID no puede ser menor que {min}.\n")
                        continue
            return id
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el ID del empleado. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarNombre(msj, min):
    while True:
        try:
            nombre = input(msj).strip()
            nombreFiltradoArray = filtrarTexto(nombre)
            
            nombreValidar = "".join(nombreFiltradoArray).lower()
            nombreFinal = " ".join(nombreFiltradoArray).title()
            
            if len(nombreFiltradoArray) < min:
                print("Error: Debes ingresar al menos un nombre y un apellido.\n")
                continue
            
            elif nombreValidar.isdigit() or not nombreValidar.isalnum() or len(nombreValidar) == 0:
                print("Error: El nombre no debe tener números ni caracteres especiales, solo letras.\n")
                continue
            
            return nombreFinal
        
        except Exception as e:
            print("Ha ocurrido un problema al ingresar el nombre del empleado.\n")
            print(f"Error: {e}\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarHorasTrabajadas(msj, min, max):
    while True:
        try:
            horasTrabajadas = int(input(msj))
            
            if horasTrabajadas < min or horasTrabajadas > max:
                print(f"Error: Debes ingresar un valor numérico entre el rango válido ({min}-{max}).\n")
                continue
            return horasTrabajadas
        
        except ValueError:
            print("Ha ocurrido un error al ingresar las horas laboradas. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarValorHora(msj, min, max):
    while True:
        try:
            valorHora = int(input(msj))
            
            if valorHora < min or valorHora > max:
                print(f"Error: Debes ingresar un valor dentro del rango permitido (${min} COP - ${max} COP).\n")
                continue
            return valorHora
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el valor de la hora laboral. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj):
    print("\n", "*** NOMINA ACME ***".center(27))
    print("MENU".center(30))
    
    print("\n1. Agregar empleado")
    print("2. Modificar empleado")
    print("3. Buscar empleado")
    print("4. Eliminar empleado")
    print("5. Listar empleados")
    print("6. Listar nómina de un empleado")
    print("7. Listar nómina de todos los empleados")
    print("8. Salir")
    return validarOpcionUsuario(msj, 1, 8)


def agregarEmpleado():
    print("\n\n", "=== AGREGAR EMPLEADO ===".center(10), "\n")
    print("Para crear el nuevo empleado, se necesita de la siguiente información:")
    
    id = validarId(">> ID: ", 1)
    nombre = validarNombre(">> Nombre: ", 2)
    horasTrabajadas = validarHorasTrabajadas(">> Horas trabajas: ", 1, 160)
    valorHora = validarValorHora(">> Valor de la hora: ", 8000, 150000)
    
    # Agregar la información recolectada al diccionario.
    dictEmpleados[id] = {
        "nombre": nombre, 
        "horasTrabajadas": horasTrabajadas, 
        "valorHora": valorHora
    }


def modificarEmpleado():
    entrarSubMenu = True
    print("\n\n", "=== MODIFICAR EMPLEADO ===".center(10))
    
    if len(dictEmpleados) == 0:
        print("Error: Este módulo no puede iniciarse si no tiene empleados registrados.")
        input("Agregue empleados y vuelva a intentarlo. Presione cualquier tecla para salir al menú principal...")
        entrarSubMenu = False
        return
    
    # El objetivo de este while es que permita ejecutar tantas veces como quiera el usuario el submenú sin tener que salirse y volver a digitar la opción de modificar empleado.
    while entrarSubMenu:
        print("\n¿Qué desea modificar?")
        print("1. Nombre del empleado")
        print("2. Horas trabajadas del empleado")
        print("3. Valor de la hora laboral del empleado")
        opcionUsuario = validarOpcionUsuario("   >> Escoja una opción (Ingrese 0 para regresar al menú): ", 0, 3)
        continuar = True
        
        
        #Iniciar el sub-programa que se encarga de editar un empleado según las opciones permitidas.
        while continuar:
            if opcionUsuario == 0:
                input("\nPresione cualquier tecla para regresar al menú principal...")
                return False
            
            else:
                keysEmpleados = list(dictEmpleados.keys())
                
                #Listar los empleados en pantalla
                print("\n")
                print("{:<7} {:<14} {:<35}".format("N°", "ID", "NOMBRE"))
                
                for i in range(len(keysEmpleados)):
                    print("{:<7} {:<14} {:<35}".format(i+1, keysEmpleados[i], dictEmpleados[keysEmpleados[i]]["nombre"]))
                
                empleadoEditar = validarOpcionUsuario(">> Ingrese el n° del empleado en la lista a modificar (Digite 0 para regresar al sub-menu): ", 0, len(keysEmpleados))
                
                
                #Validar si el usuario ya no desea editar ningún empleado
                if empleadoEditar == 0:
                    input("\nPresione cualquier tecla para regresar al sub-menú...")
                    break
                
                else:
                    if opcionUsuario == 1:
                        print(f"\nAnterior nombre: {dictEmpleados.get(keysEmpleados[empleadoEditar-1])['nombre']}")
                        nuevoNombre = validarNombre("Nuevo nombre: ", 2)
                        # Modificar el valor existente por el nuevo dato ingresado
                        dictEmpleados.get(keysEmpleados[empleadoEditar-1])["nombre"] = nuevoNombre
                        
                    elif opcionUsuario == 2:
                        print(f"\nAnterior cantidad de horas trabajadas: {dictEmpleados.get(keysEmpleados[empleadoEditar-1])['horasTrabajadas']} hrs")
                        nuevoHorasTrabajadas = validarHorasTrabajadas("Nueva cantidad de horas trabajadas: ", 1, 160)
                        # Modificar el valor existente por el nuevo dato ingresado
                        dictEmpleados.get(keysEmpleados[empleadoEditar-1])['horasTrabajadas'] = nuevoHorasTrabajadas
                    
                    elif opcionUsuario == 3:
                        print(f"\nAnterior valor de hora laboral: ${dictEmpleados.get(keysEmpleados[empleadoEditar-1])['valorHora']:,.0f} COP")
                        nuevoValorHora = validarValorHora("Nuevo valor de la hora laboral: ", 8000, 150000)
                        # Modificar el valor existente por el nuevo dato ingresado
                        dictEmpleados.get(keysEmpleados[empleadoEditar-1])['valorHora'] = nuevoValorHora
            
            # Verificar si el usuario desea seguir modificando información en el sistema, validando si antes el usuario  ha decidido regresar al submenú.
            continuarModificar = validarOpcionUsuario("¿Desea seguir modificando información? (1 SI / 0 NO): ", 0, 1)

            if continuarModificar == 1:
                continuar = False
                entrarSubMenu = True
            elif continuarModificar == 0:
                entrarSubMenu = False
                input("\nRegresando al menú principal...")
                break


def buscarEmpleado():
    print("\n\n", "=== BUSCAR EMPLEADO ===".center(10), "\n")
    
    if len(dictEmpleados) == 0:
        print("Error: Este módulo no puede iniciarse si no tiene empleados registrados.")
        input("Agregue empleados y vuelva a intentarlo. Presione cualquier tecla para salir al menú principal...")
        return
    
    while True:
        idBuscarInfo = recuperarInfoId(">> Ingrese el ID del empleado a buscar (Digite 0 para volver al menú): ", 0)
        
        # Verificando si "idBuscarInfo" es 0 (False) o no (True):
        if not idBuscarInfo:
            return  # No hay necesidad de que retorne valor alguno.
        
        else:
            idEmpleado, infoEmpleado = idBuscarInfo
            nombre, cantidadHrs, valorHrs = infoEmpleado
            
            
            print("\n", f"=== ID: {idEmpleado} ===")
            print(f"Nombre: {nombre}")
            print(f"Cantidad horas: {cantidadHrs} hrs")
            print(f"Valor hora: ${valorHrs:,.0f} COP")
            input()
        
        continuar = validarOpcionUsuario("¿Desea buscar a otro empleado? (1 SI / 0 NO): ", 0, 1)
        if continuar == 1:
            continue
        elif continuar == 0:
            input("Presione cualquier tecla para regresar al menú principal...")
            break


def eliminarEmpleado():
    print("\n\n", "=== ELIMINAR EMPLEADO ===".center(10), "\n")
    
    if len(dictEmpleados) == 0:
        print("Error: Este módulo no puede iniciarse si no tiene empleados registrados.")
        input("Agregue empleados y vuelva a intentarlo. Presione cualquier tecla para salir al menú principal...")
        return
    
    while True:
        idEmpleadoEliminar = validarId(">> Ingrese el ID del empleado a eliminar (Digite 0 para regresar al menú principal): ", 0, True)
        existeIdEmpleadoEliminar = existeId(idEmpleadoEliminar)
        
        
        if idEmpleadoEliminar == 0:
                input("Presione cualquier tecla para volver al menú principal...")
                break
        
        if not existeIdEmpleadoEliminar:
            print("Error: El empleado ingresado no ha sido registrado.\n")
            continue
        else:
            usuarioEliminado = dictEmpleados.pop(idEmpleadoEliminar)
            print(f"¡El empleado '{usuarioEliminado['nombre']}' bajo el ID '{idEmpleadoEliminar}' ha sido eliminado con éxito!")
            
            input()
            break
    
    print(dictEmpleados)


def listarEmpleados(paginacion):
    numberPaginacion = paginacion
    checked = False
    print("\n\n", "=== LISTAR EMPLEADOS ===".center(10))
    
    if len(dictEmpleados) == 0:
        print("Error: Este módulo no puede iniciarse si no tiene empleados registrados.")
        input("Agregue empleados y vuelva a intentarlo. Presione cualquier tecla para salir al menú principal...")
        return
    
    
    #El siguiente código corresponde el funcionamiento para mostrar mediante paginación el listado de los empleados con su información.
    keysDictEmpleados = list(dictEmpleados.keys())
    longitudEmpleados = len(keysDictEmpleados)
    inicioBucle = 0
    
    
    if longitudEmpleados <= paginacion:
        print("\n{:<7} {:<14} {:<40} {:<14} {:<13}".format("N°", "ID", "NOMBRE", "CANTIDAD HRS", "VALOR HRS"))
        for i in range(paginacion):
            try:
                nombre, cantidadHrs, valorHrs = list(dictEmpleados[keysDictEmpleados[i]].values())
                print("{:<7} {:<14} {:<40} {:<14} {:<13}".format(i+1, keysDictEmpleados[i], nombre, f"{cantidadHrs} hrs", f"${valorHrs:,.0f} COP"))
            
            except IndexError:
                break
    
    else:
        while True:
            print("\n{:<7} {:<14} {:<40} {:<14} {:<13}".format("N°", "ID", "NOMBRE", "CANTIDAD HRS", "VALOR HRS"))
            for i in range(inicioBucle, numberPaginacion):
                try:
                    nombre, cantidadHrs, valorHrs = list(dictEmpleados[keysDictEmpleados[i]].values())
                    print("{:<7} {:<14} {:<40} {:<14} {:<13}".format(i+1, keysDictEmpleados[i], nombre, f"{cantidadHrs} hrs", f"${valorHrs:,.0f} COP"))
                    
                    #En caso de que hayan varios empleados, validar que llegue hasta 5 y pregunte al usuario si continua o no
                    if i+1 == paginacion:
                        break
                
                except IndexError:
                    checked = True
                    break
                
                
            if checked:
                break
            else:
                continuarListarEmpleados = validarOpcionUsuario("\n¿Deseas listar más empleados? (1 SI / 0 NO): ", 0, 1)
                
                if continuarListarEmpleados == 0:
                    break
                elif continuarListarEmpleados == 1:
                    #Estas variables establecen el inicio y fin del rango en el bucle
                    inicioBucle = paginacion
                    numberPaginacion += paginacion
                    continue
    
    input("\nPresione cualquier tecla para continuar...")


def listarNominaEmpleado(id, min = 1, checked = False):    
    if checked:
        pass
    else:
        print("\n\n", "=== LISTAR NÓMINA DE UN EMPLEADO ===".center(10), "\n")
    
    if len(dictEmpleados) == 0:
        print("Error: Este módulo no puede iniciarse si no tiene empleados registrados.")
        input("Agregue empleados y vuelva a intentarlo. Presione cualquier tecla para salir al menú principal...")
        return
    
    
    #Preguntando al usuario por el ID del empleado
    descuentoEPS = 4
    descuentoPension = 4
    
    
    # Verificar si el llamado de la función proviene del menú principal o de otra función que no requiere la validación del ID.
    if checked:
        idEmpleadoNomina = id
    else:
        idEmpleadoNomina = validarId(id, min, True)
    
    
    #Verificar si el usuario ha decidido regresar al menú principal o quedarse en el sub-programa
    if idEmpleadoNomina == 0:
        input("Presione cualquier tecla para regresar al menú principal...")
        return
    
    else:
        #Calculando el salario neto (Primero calcular el salario bruto y luego el salario neto).
        salarioBruto = dictEmpleados[idEmpleadoNomina]['valorHora'] * dictEmpleados[idEmpleadoNomina]['horasTrabajadas']
        
        valorDescuentoEPS = (salarioBruto * descuentoEPS) / 100
        valorDescuentoPension = (salarioBruto * descuentoPension) / 100
        valorDescuentos = valorDescuentoEPS + valorDescuentoPension
        salarioNeto = salarioBruto - valorDescuentos
        
        if salarioBruto < smmlv:
            salarioNeto += subsidioTransporte
        
        
        if checked:
            #Imprimiendo los resultados si la función ha sido llamada desde otra función
            nombre, horasTrabajadas, valorHora = list(dictEmpleados[idEmpleadoNomina].values())
            return [idEmpleadoNomina, nombre, horasTrabajadas, valorHora, salarioNeto]
        
        else:
            #Imprimiendo los resultados si la función NO fue llamada por otra función
            nombre, horasTrabajadas, valorHora = list(dictEmpleados[idEmpleadoNomina].values())
            
            print("\n", f"=== ID: {idEmpleadoNomina} ===")
            print(f"Nombre: {nombre}")
            print(f"Horas Trabajadas: {horasTrabajadas} hrs")
            print(f"Valor de la hora laboral: ${valorHora:,.0f} COP")
            print(f"Valor de la nómina del empleado: ${salarioNeto:,.0f} COP")
            input()


def listarNominasTotalEmpleados(paginacion):
    print("\n\n", "=== LISTAR LAS NÓMINAS DE LOS EMPLEADOS ===".center(10), "\n")
    
    if len(dictEmpleados) == 0:
        print("Error: Este módulo no puede iniciarse si no tiene empleados registrados.")
        input("Agregue empleados y vuelva a intentarlo. Presione cualquier tecla para salir al menú principal...")
        return
    
    
    # Imprimir los resultados en pantalla mediante una paginación de 5 empleados
    inicioBucle = 0
    keysDictEmpleados = list(dictEmpleados.keys())
    longitudEmpleados = len(keysDictEmpleados)
    paginacionContador = paginacion
    checked = False
    sumaNomina = 0
    valorTotalNominas = []
    
    if longitudEmpleados <= paginacion:
        print("\n{:<7} {:<14} {:<40} {:<14} {:<13} {:<16}".format("N°", "ID", "NOMBRE", "CANTIDAD HRS", "VALOR HRS", "VALOR NÓMINA"))
        
        for i in range(longitudEmpleados):
            # valorTotalNominas.append(nomina)
            id, nombre, horasTrabajadas, valorHora, nomina = listarNominaEmpleado(keysDictEmpleados[i], 1, True)
            print("{:<7} {:<14} {:<40} {:<14} {:<13} {:<16}".format(i+1, id, nombre, f"{horasTrabajadas} hrs", f"${valorHora:,.0f} COP", f"${nomina:,.0f} COP"))
            sumaNomina += nomina
            
    else:
        while True:
            print("\n{:<7} {:<14} {:<40} {:<14} {:<13} {:<16}".format("N°", "ID", "NOMBRE", "CANTIDAD HRS", "VALOR HRS", "VALOR NÓMINA"))
            
            for i in range(inicioBucle, paginacionContador):
                try:
                    id, nombre, horasTrabajadas, valorHora, nomina = listarNominaEmpleado(keysDictEmpleados[i], 1, True)
                    print("{:<7} {:<14} {:<40} {:<14} {:<13} {:<16}".format(i+1, id, nombre, f"{horasTrabajadas} hrs", f"${valorHora:,.0f} COP", f"${nomina:,.0f} COP"))
                    # valorTotalNominas.append(nomina)
                    sumaNomina += nomina
                    
                    #En caso de que hayan varios empleados, validar que llegue hasta 5 y pregunte al usuario si continua o no
                    if i+1 == paginacionContador:
                        break
                
                except IndexError:
                    checked = True
                    break
            
            if checked:
                break
            else:
                continuarListarNomina = validarOpcionUsuario("\n¿Deseas listar más empleados? (1 SI / 0 NO): ", 0, 1)
                
                if continuarListarNomina == 0:
                    break
                elif continuarListarNomina == 1:
                    #Estas variables establecen el inicio y fin del rango en el bucle
                    inicioBucle = paginacionContador
                    paginacionContador += paginacion
                    continue
    
    
    # Calcular el recuento del valor total de nóminas
    print(f"VALOR TOTAL NÓMINAS: ${sumaNomina:,.0f} COP")
    input("\nFinalizando cálculo de nómina. Presione cualquier tecla para continuar...")


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    opcionUsuario = menu("   >> Escoja una opción (1-8)?: ")
    paginacion = 5
    
    if opcionUsuario == 1:
        agregarEmpleado()
    
    elif opcionUsuario == 2:
        modificarEmpleado()
    
    elif opcionUsuario == 3:
        buscarEmpleado()
    
    elif opcionUsuario == 4:
        eliminarEmpleado()
    
    elif opcionUsuario == 5:
        listarEmpleados(paginacion)
    
    elif opcionUsuario == 6:
        listarNominaEmpleado(">> Ingrese el ID del empleado para calcular su nómina (Digite 0 para regresar al menú principal): ", 0, False)
    
    elif opcionUsuario == 7:
        listarNominasTotalEmpleados(paginacion)
    
    elif opcionUsuario == 8:
        confirmarSalida = validarOpcionUsuario("\n¿Está seguro que quiere cerrar el programa? (1 SI / 0 NO): ", 0, 1)
        
        #Confirmar si el usuario desea salir del programa o no
        if confirmarSalida == 0:
            input("Regresando al menú principal. Presione cualquier tecla para continuar...")
            isVerdadero = True
            
        elif confirmarSalida == 1:
            isVerdadero = False
            input("¡Gracias por usar nuestro software!")