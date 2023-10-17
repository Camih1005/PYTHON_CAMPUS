fecha = input("fecha: ")
partes = fecha.split("/")
if len(partes[0]) == 2 and \
    len(partes[1]) == 2 and\
        len(partes[2]) == 4:
            
    valido = True
    for p in partes:
        if not p.isdigit():
            valido = False
            break
    
    if valido:
        print(f"dia: {partes[0]}, mes: {partes[1]}, año: {partes[2]}")
    else:
        print("Formato no válido")
else:
    print("Formato no válido")