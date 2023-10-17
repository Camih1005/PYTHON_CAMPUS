num = input("Ingrese el número:")

if num.startswith("+") and num.count("-") == 2:
    partes = num.split("-")
    print("El telefono es:", partes[1])
else:
    print("Error. El número no cumple con el formato")