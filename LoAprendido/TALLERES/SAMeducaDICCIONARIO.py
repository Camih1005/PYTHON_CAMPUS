n = int(input("Cantidad de docentes? "))

dicCategoria = {1:25000, 2:30000, 3:40000, 4:45000, 5:60000}

# *** SOLUCIÓN CON DICCIONARIOS ***

# dicDocentes = {}
# totalHonorarios = 0

# for i in range(1, n+1):
#     print("\nDatos del docente #", i)
#     datDocente = {}
#     ced = input("Cedula: ")
#     datDocente["nombre"] = input("Nombre: ") 
#     datDocente["categoria"] = int(input("Categoria (1 al 5): "))
#     datDocente["horas_lab"] = int(input("Horas laboradas: "))
#     datDocente["honorarios"] = dicCategoria.get(datDocente["categoria"], 0) * datDocente["horas_lab"]
    
#     totalHonorarios += datDocente["honorarios"]
    
#     dicDocentes[ced] = datDocente
    
    
# print("\n\n", "=" * 30)
# print("INFORME")
# print("=" * 30)
# print("NOMBRE\t\tHONORARIOS")
# print("-" * 30)

# for k, v in dicDocentes.items():
#     print(f'{v["nombre"]}\t\t${v["honorarios"]:,}')

# print("\n", "-" * 30)
# print(f"Total honorarios: ${totalHonorarios:,}")


# *** SOLUCIÓN CON LISTAS ***
lstDocentes = []
totalHonorarios = 0

for i in range(1, n+1):
    print("\nDatos del docente #", i)
    datDocente = {}
    ced = input("Cedula: ")
    datDocente["ced"] = ced
    datDocente["nombre"] = input("Nombre: ") 
    datDocente["categoria"] = int(input("Categoria (1 al 5): "))
    datDocente["horas_lab"] = int(input("Horas laboradas: "))
    datDocente["honorarios"] = dicCategoria.get(datDocente["categoria"], 0) * datDocente["horas_lab"]
    
    totalHonorarios += datDocente["honorarios"]
    
    lstDocentes.append(datDocente)
    
    
print("\n\n", "=" * 30)
print("INFORME")
print("=" * 30)
print("NOMBRE\t\tHONORARIOS")
print("-" * 30)

# for d in lstDocentes:
    # print(f'{d["nombre"]}\t\t${d["honorarios"]:,}')

for i in range(len(lstDocentes)):
    print(f'{lstDocentes[i]["nombre"]}\t\t${lstDocentes[i]["honorarios"]:,}')

print("\n", "-" * 30)
print(f"Total honorarios: ${totalHonorarios:,}")