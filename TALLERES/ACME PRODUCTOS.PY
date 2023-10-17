def readId():
    while True:
        try:
            num = int(input("Enter your ID: "))
            if num < 1:
                print("Error: Invalid input, must be a positive integer")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return num
        except ValueError:
            print("Error: Invalid input, must be an integer")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

def readVal():
    while True:
        try:
            num = int(input("Ingrese el precio: "))
            if num < 1:
                print("Error: Invalid input, must be a positive integer")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return num
        except ValueError:
            print("Error: Invalid input, must be an integer")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

def readAmount():
    while True:
        try:
            num = int(input("Ingrese cantidad de productos: "))
            if num < 1:
                print("Error: Invalid input, must be a positive integer")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return num
        except ValueError:
            print("Error: Invalid input, must be an integer")
            input("Press any key to continue")
def readStr():
    while True:
        try:
            phrase = input("Ingrese el nombre del producto: ")
            phrase = phrase.strip()
            if len(phrase) == 0 or phrase.isalnum() == False:
                print("Error: Invalid input, must be a string")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return phrase
        except Exception as e:
            print(f"Error: Invalid input, must be a string\n{e}")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

def findProduct(dicProduct, ID):
    for k, v in dicProduct.items():
        if k == ID:
            return k
    return None

def agregarProducto(dicProduct):
    print("*** Nuevo Prodcto***")
    datProduct = {}
    id = readId()
    if findProduct(dicProduct, id) != None:
        print("The ID already exists.")
        input()
        return
    datProduct["name"] = readStr()
    datProduct["price"] = readVal()
    datProduct["amount"] = readAmount()

    dicProduct[id] = datProduct

def modifyProduct(dicProduct, ID):
    if findProduct(dicProduct, ID) == None:
        print("The ID already exist")
        return
    while True:
        print("* Modify Product *")
        print("1- Change name")
        print("2- Change value")
        print("3- Change amount")
        n = int(input("Choose which option you would like to modify: "))
        if n < 1 or n > 3:
            print("Error: Input must be between 1 and 3")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")
            continue
        break
    if n == 1:
        dicProduct[ID]["name"] = readStr()
    elif n == 2:
        dicProduct[ID]["price"] = readVal()
    elif n == 3:
        dicProduct[ID]["price"] = readAmount()

def eraseProduct(dicProduct, ID):
        if findProduct(dicProduct, ID) == None:
            print("That ID does not exist, try again.")
            input()
            return
        op = input("\nAre you sure you wish to erase this product (Y/N)? ")
        if op.lower() == "y":
            dicProduct.pop(ID)

def listProducts(dicProduct):
    count = 0
    # The for loop will go through every key inside of dicProduct, and then the values within that key
    for k, v in dicProduct.items():
        print("\n", "=" * 30, "\n")
        print(f"ID: {k}")
        print(f"Name: {v['name']}")
        print(f"Value: {v['price']}")
        print(f"Amount: {dicProduct[k]['amount']}")
        print("\n", "=" * 30, "\n")
        
        count += 1

        if count % 5 == 0:
            op = input("Do you wish to continue? (Y/N) ")
            if op.lower() == "n":
                return

def ordenamiento_burbuja(lst):
    N = len(lst)
    for i in range(0, N-1):
        for j in range(i+1, N):
            if lst[i][1]["price"] > lst[j][1]["price"]:
                t = lst[i]
                lst[i] = lst[j]
                lst[j] = t
    return lst


def sortProducts(dicProducts):
    print("\n5. Estrategia de mercados\n")
    # *** codigo original
    # lst = dicProduct.values()
    # for i in range(len(lst)):
    #     for j in range(i+1):
    #         if lst[i]["price"]>lst[j]["price"]:
    #             t=lst[i]["price"]
    #             lst[i]["price"] = lst[j]["price"]
    #             lst[j]["price"] = t
    # return list
    
    # ** Solución con metodo burbuja
    prodOrd = ordenamiento_burbuja(list(dicProduct.items()))
    
    # *** Solución con función sorted
    # prodOrd = sorted(list(dicProduct.items()), key=lambda x : x[1]["price"])
    
    print("ID\t\tNombre\t\tPrecio\t\tCantidad")
    print("-" * 80)
    i = 0
    for tpl in prodOrd:
        print(f"{tpl[0]}\t\t{tpl[1]['name']}\t\t{tpl[1]['price']}\t\t{tpl[1]['amount']}")
        i += 1
        if i % 5 == 0:
            i = 0
            input("\nPresione cualquier tecla para continuar ...")
    
    
    
def menu():
    while True:
        try:
            print("\n", "=" * 30, "\n")
            print("\tPRODUCTOS ACME")
            print("\n", "=" * 30, "\n")
            print("1- Agregar producto")
            print("2- Modificar producto")
            print("3- Eliminar producto")
            print("4- Listar varios productos")
            print("5- Estrategia de mercadeo")
            print("6- Salir")
            opcion = int(input("Ingrese una opcion: "))
            if opcion < 1 or opcion > 6:
                print("Error: Input must be between 1 and 8")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return opcion
        except ValueError:
            print("Error: Invalid option")

dicProduct = {}

while True:
    option = menu()
    if option == 1:
        agregarProducto(dicProduct)
        print(dicProduct)
        input()
    elif option == 2:
        modifyProduct(dicProduct, readId())
        print(dicProduct)
        input()
    elif option == 3:
        eraseProduct(dicProduct, readId())
        print(dicProduct)
        input()
    elif option == 4:
        listProducts(dicProduct)
        input()
    elif option == 5:
        sortProducts(dicProduct)
        print(dicProduct)
        input()
        pass
    elif option == 6:
        print("Thanks for using the software")
        input()
        break