import json

fd = open("/home/spukN01-/Documents/CCamilo/LoAprendido/ArchivosY_JSON/lista.json","w")

lst = [{"nombre": "Paola", "Edad":25},{"nombre": "Camilo", "Edad":22},{"nombre": "Daniel", "Edad":23},{"nombre": "Claudia", "Edad":40},{"nombre": "Juan", "Edad":21}]

json.dump(lst, fd)

fd.close()