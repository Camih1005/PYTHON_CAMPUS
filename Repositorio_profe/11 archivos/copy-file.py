fd = open("Campus Lab\\Ciclo 1\\Grupo-C4-Sep\Código\\11 archivos\\nombres.txt", "r")

fd2 = open("Campus Lab\\Ciclo 1\\Grupo-C4-Sep\Código\\11 archivos\\nombres-bak.txt", "w")

for linea in fd:
    fd2.write(linea)

fd2.close()
fd.close()

print("Proceso terminado")
