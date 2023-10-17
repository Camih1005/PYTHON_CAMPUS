archivo = open("Campus Lab/Ciclo 1/Grupo-C4-Sep/Código/11 archivos/salas.txt", "w")

archivo.write("sputnik\n\t")
archivo.write("apolo\n")

archivo.writelines(["houston\n", "artemis\n"])

archivo.close()