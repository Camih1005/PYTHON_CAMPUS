# for numero in range(5):
#     print(numero, numero* "hola mundo")

#for mas complejo


buscar = int(input("numero que desea buscar del 1 al 10: "))
for numero in range(10):
    print(numero)
    if numero == buscar:
        print(f"encontrado el numero {buscar}")
        break
else:
    print("NO APARECE")    

for char in "ultimate python":
    print(char)
