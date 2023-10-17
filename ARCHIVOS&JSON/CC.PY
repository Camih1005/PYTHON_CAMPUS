fd = open("/home/spukN01-/Documents/CCamilo/LoAprendido/ArchivosY_JSON/mbox-short.txt","r")

cantLineas = 0
#contar cantidad de lineas
"""for linea in fd:
    cantLineas += 1"""
#contar cantidad de palabras

cantPalabras = 0
for linea in fd:
    linea.strip() #elimino espacion antes y al final
    cantPalabras += len(linea.split(" "))


fd.close() #  cerrar archivo a penas no lo necesito
print(f"Hay {cantLineas} lineas en el archivo.")
print(f"Hay {cantPalabras} palabras en el archivo.")