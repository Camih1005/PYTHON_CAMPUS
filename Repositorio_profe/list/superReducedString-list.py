def superReducedString(s):
    # convertir la cadena en lista
    # hace mientras haya reemplazos
        # recorrer la lista de inicio a fin-1
            # si posi igual a posi+1 entonces
                # si hay reemplazo
                # borrar posi y posi+1
                # incrementar i en 2
    
    # si lista vacia entonces
        # devolver cadena "Empty String"
    
    # devolver lista en cadena
    
    
    # convertir la cadena en lista
    ls = list(s)
    reemplazo = True
    # hace mientras haya reemplazos
    while reemplazo:
        i = 0
        reemplazo = False
        # recorrer la lista de inicio a fin-1
        while i < len(ls) - 1:
            # si posi igual a posi+1 entonces
            if ls[i] == ls[i+1]:
                # si hay reemplazo
                reemplazo = True
                # borrar posi y posi+1
                ls.pop(i)
                ls.pop(i)
                # incrementar i en 2
                # i += 1
            i += 1
    
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