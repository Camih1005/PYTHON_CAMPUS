def suma(num1, num2):
    resultado = num1 + num2
    return resultado

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        resultado = None
    return resultado

def menu():
    while True:
        try:
            print("*** MENU CALCULADORA ***")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
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
    
def leerNum(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            return num
        except ValueError:
            print("Error. Número inválido")
            input("Presione cualquier tecla para continuar...")
        
    
## PROGRAMA PRINCIPAL
while True:
    opcion = menu()
    if opcion == 1:
        print("\n\n1. SUMAR")
        num1 = leerNum("Ingrese el primer numero: ")
        num2 = leerNum("Ingrese el segundo numero: ")
        print(f"El resultado de la suma es: {suma(num1, num2):.3f}")
    elif opcion == 2:
        print("\n\n2. RESTAR")
        num1 = leerNum("Ingrese el primer numero: ")
        num2 = leerNum("Ingrese el segundo numero: ")
        print(f"El resultado de la resta es: {resta(num1, num2):.3f}")
    elif opcion == 3:
        print("\n\n3. MULTIPLICAR")
        num1 = leerNum("Ingrese el primer numero: ")
        num2 = leerNum("Ingrese el segundo numero: ")
        print(f"El resultado de la multiplicación es: {multiplicacion(num1, num2):.3f}")
    elif opcion == 4:
        print("\n\n4. DIVIDIR")
        num1 = leerNum("Ingrese el primer numero: ")
        num2 = leerNum("Ingrese el segundo numero: ")
        res = division(num1, num2)
        if res != None:
            print(f"El resultado de la división es: {res:.3f}")
        else:
            print("División entre cero es indeterminada.")
    elif opcion == 5:
        print("\n\nGracias por usar la calculadora")
        print("Adios")
        input("Presione cualquier tecla para salir ...")
        break
    input("Presione cualquier tecla para volver al MENU...")
            
            