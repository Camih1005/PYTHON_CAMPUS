import json

fd = open("Campus Lands\\Ciclo 1\\Grupo-C4-Sep\\Código\\11 archivos\\lista.json", "r")

lst = []

lst = json.load(fd)

for e in lst:
    print(f"Nombre: {e['nombre']}")
    print(f"Edad: {e['edad']}")
    print("-" * 30)

fd.close()