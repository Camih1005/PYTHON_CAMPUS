import json

fd = open("Campus Lands\\Ciclo 1\\Grupo-C4-Sep\\Código\\11 archivos\\lista.json", "w")

lst = [{"nombre": "Paola", "edad": 25},
       {"nombre": "Carlos", "edad": 28},
       {"nombre": "Juan", "edad": 18},
       {"nombre": "Mateo", "edad": 19},
       {"nombre": "Patricia", "edad": 21}]

json.dump(lst, fd)

fd.close()
