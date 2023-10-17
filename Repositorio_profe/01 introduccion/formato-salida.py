# ejemplos de formatear la salida

# CON FORMAT
sueldo = 5600000
print("Sueldo: ${:,}".format(sueldo))

interes = 2568.568954112568
print("Valor del interes: {:,.3f}".format(interes))

# f-string
print(f"Sueldo: ${sueldo:,}")
print(f"Valor del interes: {interes:,.3f}")