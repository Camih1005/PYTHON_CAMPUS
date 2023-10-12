#EMPLEADOS
empleado = {"nombre": "Camilo hernandez","Cargo":"Programador","Sueldo":"4000000"}
print(empleado["Cargo"])
print(empleado.get("Cargo"))
print(empleado.get("apellido","llave no existe"))

empleado["sexo"] = "M"#AGREGA OTRA LLAVE
print(empleado)

empleado["Sueldo"]= 4500000 #MODIFICA EL VALOR DEL SUELDO
print(empleado)

del empleado ["sexo"]#ELIMINAR LA LLAVE Y EL VALOR
print(empleado)

#BORRAR TODO EL DICCIONARIO DE CUALQUIERA DE ESTAS FORMAS
#empleado = {}
#empleado.clear()
#del empleado
oficina = empleado
print(oficina)
oficina["Sueldo"] = 5000000
print(oficina)
print(empleado)

#.copy puede modificar solo uno

#.fromkeys(x, y)
x = ("key1","key2","key3")
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#items hace identificar con dublas la llave y la clave de cada pareja()
print(empleado.items)

#keys

print(empleado.keys())

#values
print(empleado.values())

#pop
print(empleado.pop("Sueldo"))

#popitem elimina lo ultimo del diccionario
print(empleado.popitem())
print(empleado)

#setdefault
print(empleado.setdefault("nombre", "Camilo"))
print(empleado.setdefault("Ciudad","Bucaramanga"))
print(empleado)



