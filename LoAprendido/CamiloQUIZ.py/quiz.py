def eliminarDicc(dicprod):
    leerIDprod.pop(dicprod)
    print("Empleado eliminado.")

def buscarProd(dicprod, idprod):
    return idprod in dicprod

def mnubuscarProd(dicprod):
    print("\n\n3. Buscar producto\n")
    
    idprod = leerIDprod()
    existEmpl = buscarProd(dicprod, idprod)
    if existEmpl == False:
        print("El producto con ese código no ha sido ingresado.")
        input()
        return
    
def listarprod(dicprod):
    print("4. Listar productos")
    for i in dicprod.keys():
        i +=1
    print(f"Lista de producto\n{dicprod}")
    
    
def modifProd(dicprod):
    print("\n\n2. Modificar Producto\n")
    
    IdProd = leerIDprod()
    existProd = buscarProd(dicprod, IdProd)
    if existProd == False:
        print("El código del producto no existe.")
        input()
        return

def CantdeProduct():
    while True:
        try:
            cant = int(input("Ingrese cantidad de productos de entrada:"))
            if cant <0 or cant> 1000:
                print("Cantidad de productos ingresada")
                continue
            return cant
        except ValueError:
            print("Error en la digitacion")
            

def leerPrecioProduct():
    while True:
        try:
            n = int(input("Ingrese precio del producto a ingresar: "))
            if n < 0 or n > 250000:
                print("No hay ningun producto con ese valor")
                continue
            return n
        except ValueError:
            print("Error de valor.")

def leerNombreProduct():
    while True:
        try:
            nom = input("Ingrese el nombre del producto:")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre de producto inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el producto.", e)

def leerIDprod():
    while True:
        try:
            n = int(input("Ingrese el ID del producto: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")

def agregarProd(dicprod):
    print("\n\n*** 1. Agregar producto\n")
    dicprod = {}
    id= leerIDprod()
    if buscarProd(dicprod, id) == True:
        print("El id ya existe en la lista")
        input()
        return   
    
    dicprod["Nombre"] = leerNombreProduct()
    dicprod["Precio del producto"] = leerPrecioProduct()
    dicprod["Cantidad"] = CantdeProduct()
    

def menu():
    while True:
        try:
            print("="*18)
            print("PRODUCTOS ACME")
            print("="*18)
            print("1. Agregar producto")
            print("2. Modificar producto")
            print("3. Eliminar producto")
            print("4. Listar varios productos")
            print("5. Estrategia de mercadeo")
            print("6. SALIR")
            op = int(input(">>> Opción (1-6)? "))
            if op < 1 or op > 6:
                print("Opción no válida. Escoja de 1 a 6.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 6.")
            input("Presione cualquier tecla para continuar...")
            
dicprod= {}
while True:
    op = menu()
    if op == 1:
        agregarProd(dicprod)
        print(dicprod)
        input()
    elif op == 2:
        modifProd(dicprod)
        print(dicprod)
        input()    
    elif op == 3:
        eliminarDicc(dicprod)
        print(dicprod)
        input()
    elif op == 4:
        listarprod(dicprod)
        print(dicprod)
        input()
    
        
        
    
        

    
    #elif op == 8:
        print("\n\nGracias.")
        break            
    