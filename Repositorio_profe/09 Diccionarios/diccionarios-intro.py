# empleado = {}
# empleado = dict()
empleado = {"Nombre": "Sergio Medina", "cargo":"programador", "salario":4000000}

print(empleado["cargo"])
print(empleado.get("cargo"))
# print(empleado["apellido"])
print(empleado.get("apellido", "llave no existe"))

# agregar una llave
empleado["sexo"] = "M"
print(empleado)

# Modificar un valor
empleado["salario"] = 4500000

# borrar una llave y su valor
del empleado["sexo"]
print(empleado)

# borrar todo el diccionario
# empleado = {}
# empleado.clear()
# del empleado

#copy
oficina = empleado.copy()
print(oficina)
oficina["salario"] = 5000000
print(oficina)
print(empleado)

# fromkeys
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#items
print(empleado.items())

#keys
print(empleado.keys())

#values
print(empleado.values())

#pop
print(empleado.pop("salario"))
print(empleado)

#popitem
print(empleado.popitem())
print(empleado)

#setdefault
print(empleado.setdefault("Nombre", "Carlos"))
print(empleado.setdefault("Ciudad", "Bucaramanga"))
print(empleado)




