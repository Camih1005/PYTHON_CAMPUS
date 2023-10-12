def suma (num1, num2):
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
            print("****MENU CALCULADORA****")
            print("\t1.Suma")
            print("\t2.Restar")
            print("\t3.Multiplicar")
            print("\t4.Dividir")
            print("\t5.Salir")
            op = int(input("\t>>> OPCION (1-5)?"))
            if op <1 or op >5:
                print("opcion no valida\nEscoja de 1 a 5.")
                input("Presione cualquier tecla para continuar")
                continue
            return op
            
        except ValueError:
           print("Opcion no valida.\nEscoja de 1 a 5.")

           return op

 #programa principal
def leerNum(mensaje):
     while True:
         try:
             num = float(input(mensaje))
             return num
         except ValueError:
             print("Error. Numero invalido")
             input("presione cualquier tecla para funcionar")
while True:
    opcion = menu()
    num1 = leerNum("INGRESE EL PRIMER NUMERO")
    num2 = leerNum("INGRESE EL SEGUNDO NUMERO")
    if opcion == 1:
        print("\n\n1.SUMAR")
        num1 = leerNum("INGRESE EL PRIMER NUMERO")
        num2 = leerNum("INGRESE EL SEGUNDO NUMERO")
        print(f"El resultado de la suma es: {suma(num1, num2):.3f}")
        
    elif opcion == 2:
         print("\n\n2.RESTAR") 
         num1 = leerNum("INGRESE EL PRIMER NUMERO")
         num2 = leerNum("INGRESE EL SEGUNDO NUMERO")  
         print(f"El resultado de la resta es: {resta(num1, num2):.3f}")
    elif opcion == 3:
         print("\n\n3.MULTIPLICAR")
         num1 = leerNum("INGRESE EL PRIMER NUMERO")
         num2 = leerNum("INGRESE EL SEGUNDO NUMERO")
         print(f"El resultado de la multiplicaicon es: {multiplicacion(num1, num2):.3f}")    
    elif opcion == 4:
        print("\n\n4.DIVIDIR")
        num1 = leerNum("INGRESE EL PRIMER NUMERO")
        num2 = leerNum("INGRESE EL SEGUNDO NUMERO")
        res = division(num1, num2)
        
        print(f"El resultado de la division es: {division(num1, num2):.3f}")    
    elif opcion == 5:
        num1 = leerNum("INGRESE EL PRIMER NUMERO")
        num2 = leerNum("INGRESE EL SEGUNDO NUMERO")
        input("Presione cualquier tecla para salir..")
        break
    input("Presione cualquier tecla para volver al menu")       
    print("\nGracias por usar la calculadora")
    print("\tAdios")
    print()
    break


              