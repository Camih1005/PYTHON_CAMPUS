fd = open("Campus Lab\\Ciclo 1\\Grupo-C4-Sep\\Código\\11 archivos\\datos-empleados.dat", "r")

for linea in fd:
    if not linea.startswith("ID"):
        datos = linea.split(",")
        print(f"ID:{datos[0]}\nNOMBRE:{datos[1]}\nEDAD:{datos[2]}")
        print(f"SEXO:{datos[3]}\nCELULAR:{datos[4].strip()}")
        print("-" * 30)

fd.close()