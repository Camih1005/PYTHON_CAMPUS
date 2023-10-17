# break
# Calcular si un numero es primo
# num primo: divisible por si mismo y por 1

# num = int(input("Ingrese un numero? "))

# if num < 2:
#     print("No es primo ")
# elif num == 2:
#     print("Es primo")
# else:
#     esprimo = True # variables banderas o switch
#     for i in range(2, num):
#         if num % i == 0:
#             esprimo = False
#             break
    
#     if esprimo == True:
#         print("Es primo")
#     else:
#         print("No es primo. Lo divide",i)


# CONTINUE
# Salta una iteración de un ciclo

# Imprima los numeros 1 al 100 excepto los multiplo de 7
for i in range(1, 101):
    if i % 7 == 0:
        continue
    print(i, end=", ")