letras = []
while True:
    letra = input("Ingrese una letra del Abecedario: ")
    if not letra.isalpha():
        print("Invalido")
        continue
    letras.append(letra)
    op=input("\nDesea continuar(S\\N)?")
    if op.lower()!= "s":
        break

    print("\n","="* 30)
    vocales = ["a", "u", "i","o","u"]
    canVocales = [0] * 5

    #RECORRER LA LISTA POR ELEMENTOS

    for l in letras:
        if l.lower() in vocales:
            p=vocales.index(l.lower())
            canVocales[p] += 1
        
    

    for p in range(len(vocales)):
        print(vocales[p],"=", canVocales[p])