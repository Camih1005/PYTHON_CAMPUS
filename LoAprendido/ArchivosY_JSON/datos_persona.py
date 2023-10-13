import json  

def guardarEmpleado(lstPersonal, ruta):
    try:
        fd = open(ruta,"w")
    except Exception as e:
        print("Error al guardar el empleado\n", e)
        return None
    
    try:
        json.dump(lstPersonal, fd)
    except Exception as e:
        print("Error al guardar la informacion del empleado.\n", e)
        return None
    
def existeID(id,lstPersonal):
    for datos in lstPersonal:
        if datos["id"] == id:
            return True
    return False          

def agregarpersonal(lstPersonal):
    print("\n\n1. Agregar personal")
    
    id = int(input("Ingrese el ID:"))
    while existeID(id,lstPersonal):
        print("---> YA existe un empleado con ese ID: ")
        input()
        id = int(input("\Ingrese el ID: "))
        
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo M/F: ")
    telefono = input("Telefono")
    
    dicEmpleado={}
    dicEmpleado[id] = {"nombre":nombre, "edad":edad, "sexo": sexo, "telefono":telefono}
    
        
    
    
    
def menu():     
    while True:         
        try:             
            print(" NOMINA ACME ".center(40))             
            print("MENU".center(40))             
            print("1. Agregar\n2. Modificar\n3. Borrar\n4. Ver\n5. Salir")             
            op = int(input(">>> Opción (1-5)? "))             
            if op < 1 or op > 5:                 
                print("Opción no válida. Escoja de 1 a 5.")                 
                input("Presione cualquier tecla para continuar...")                 
                continue             
            return op         
        except ValueError:             
            print("Opción no válida. Escoja de 1 a 5.")             
            input("Presione cualquier tecla para continuar...")   

def cararInfo(lstpersonal,ruta):           
    try:
        fd = open(ruta,"r")
    except Exception as e:
        try:
            fd = open(ruta,"w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n" + d)
            return None   
    
    try:
        lstpersonal = json.load(fd)    
    except Exception as e:
        print("Error al cargar informacion\n". e)
        return None
    
    fd.close()
    return lstpersonal


ruta =  ""
while True:     
    op = menu()     
    if op == 1:         
                
        pass     
    elif op == 2:                  
        pass     
    elif op == 3:         
        pass     
    elif op == 4:                 
        pass     
    else:            
         print("\n Gracias por usar el programa.")         
         break