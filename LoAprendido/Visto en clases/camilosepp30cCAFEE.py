def longString(str):
    long = 0
    try:
        long = 0
        while str[long] != None:
            long +=1
    except:
        pass
    return long        


def prepararCafe(insumo1, insumo2):
    if insumo1.lower() == "cafe" and insumo2 == "agua":
        salida = "tinto"
    else:
        salida = "daño la cafetera"    
    return salida 

#uso de la funcion
taza = prepararCafe("cafe", "agua")
print(taza)    
print(longString(taza))
