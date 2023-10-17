fd = open("Campus Lab\\Ciclo 1\\Grupo-C4-Sep\\Código\\11 archivos\\mbox-short.txt", "r")

cl = 0
cp = 0
for linea in fd:
    linea = linea.strip()
    cp += len(linea.split(" "))
    # for lin in linea.split(" "):
    #     if lin.isalnum():
    #         cp += 1
    cl += 1

fd.close()
print("Cantidad de líneas:", cl)
print("Cantidad de palabras:", cp)