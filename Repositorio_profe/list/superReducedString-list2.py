def superReducedString(s):
    # convertir la cadena en lista
    ls = list(s)
    reemplazo = True
    # hace mientras haya reemplazos
    while reemplazo:
        i = 0
        reemplazo = False
        # recorrer la lista de inicio a fin-1
        newls = []
        lenls = len(ls)
        while i < lenls:
            # si posi igual a posi+1 entonces
            if i == lenls-1 or ls[i] != ls[i+1]:
                # no hay reemplazo entonces agregue a la nueva lista
                newls.append(ls[i])
                i += 1
            else:
                # si hay reemplazo, incremente 2
                reemplazo = True
                i += 2
                
        # copie la nueva lista en la original
        ls = newls
        lenls = len(ls)
            
    
    # si lista vacia entonces
    if ls == []:
        # devolver cadena "Empty String"
        return "Empty String"
    
    # devolver lista en cadena
    return "".join(ls)


# programa prueba
str = "zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"
rta= "tqauhujtmxnsbzpykwlvpfyqijvdhuhirdmuxiobyvxupqwydkpbxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"
# str = "oolaa"
# rta = "l"

# str = "baab"
# rta = "Empty String"

print(str)
print(superReducedString(str))
print(rta)