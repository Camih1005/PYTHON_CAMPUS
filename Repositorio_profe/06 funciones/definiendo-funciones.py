# La definición de la funcion
def longString(str):
    try:
        long = 0
        while str[long] != None:
            long +=1
    except:
        pass
    return long
                
def prepararCafe(insumo1, insumo2):
    salida = ""
    if insumo1.lower() == "cafe" and insumo2.lower() == "agua":
        salida = "tinto"
    else:
        salida = "Daño la cafetera"
    return salida

# Uso de la función
taza = prepararCafe("cafe", "agua")
print(taza)
print(longString(taza))
print(len(taza))


    