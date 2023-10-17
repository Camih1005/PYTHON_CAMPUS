while True:
    try:
        num1 = int(input("Ingrese un numero: "))
        break
    except ValueError:
        print("Error. Número entero no válido.")
        
while True:
    try:
        num2 = int(input("Ingrese otro numero: "))
        break
    except ValueError:
        print("Error. Número entero no válido.")
        

try:
    num2 = "a"
    suma = num1 + num2
    print("La suma es: ", suma)
except Exception as e:
    print("Error al intentar sumar.\n", e )