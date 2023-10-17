archivo = open("Campus Lab/Ciclo 1/Grupo-C4-Sep/Código/11 archivos/nombres.txt", "r")

texto = archivo.read()
print(texto)

archivo.seek(0)
texto2 = archivo.readline()
print(texto2)

texto3 = archivo.readlines()
print(texto3)

archivo.close()