letras = []
while True:
    letra = input("Ingrese una letra del abecedario: ")
    if not letra.isalpha():
        print(">> Error. Letra no válida\n")
        input()
        continue
    
    letras.append(letra)
    
    op = input("\nDesea continuar (S\\N)? ")
    if op.lower() != "s":
        break
    
print("\n", "=" * 30)
vocales = ["a", "e", "i", "o", "u"]
canVocales = [0] * 5
# recorrer la lista por elementos
for l in letras:
    if l.lower() in vocales:
        p = vocales.index(l.lower())
        canVocales[p] += 1

# RECORRIDO POR POSICION
for p in range(len(vocales)):
    print(vocales[p], " = ", canVocales[p])
    