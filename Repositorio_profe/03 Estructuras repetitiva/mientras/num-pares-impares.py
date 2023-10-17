num = int(input("Ingrese un número: "))
cpares= 0
cimpares= 0
while num != -1:
    if num % 2 == 0:
        print("El número es par")
        cpares += 1
    else:
        print("El número es impar")
        cimpares += 1
    
    num = int(input("Ingrese un número: "))
    
print("\n", "=" * 30)
print("Cantidad de números pares es: ", cpares)
print("Cantidad de números impares es: ", cimpares)