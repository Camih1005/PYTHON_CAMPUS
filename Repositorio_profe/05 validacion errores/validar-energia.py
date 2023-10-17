# validar el nombre del usuario
while True:
    try:
        nombre = input("Ingrese el nombre del usuario: ")
        nombre = nombre.strip()
        if len(nombre) == 0 or nombre.isalnum() == False:
            print("Nombre inválido. Vuelva a digitarlo.")
            continue
        break
    except Exception as e:
        print("Error al ingresar el nombre.\n", e)

# Validar el estrato
while True:
    try:
        estrato = int(input("Ingrese el estrato (1-5): "))
        if estrato < 1 or estrato > 5:
            print("El estrato no esta en el rango (1-5). Intente de nuevo")
            continue
        break
    except ValueError:
        print("Error. Estrato inválido.")
        
if estrato == 1:
    tbas = 10000
elif estrato == 2:
    tbas = 15000
elif estrato == 3:
    tbas = 30000
elif estrato == 4:
    tbas = 50000
else:
    tbas = 60000

print ("\n", "=" * 30)
print("Nombre:", nombre)
print("Tarifa Básica: ", tbas)