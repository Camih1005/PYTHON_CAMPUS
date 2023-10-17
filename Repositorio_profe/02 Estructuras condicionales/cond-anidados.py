nombre = input("Nombre del Estudiante: ")
nota = int(input("Ingrese una nota [0-100]: "))

if nota >= 0 and nota <= 59:
    notaCual = "D"
elif nota >= 60 and nota <=79:
    notaCual = "C"
elif nota >= 80 and nota <= 89:
    notaCual = "B"
elif nota >= 90 and nota <= 100:
    notaCual = "A"
else:
    notaCual = ""
    print("Error. Nota inválida.")

print("\n", "-" * 30)
print("Estudiante:", nombre)
print("Nota cuantitativa:", nota)
print("Nota cualitativa:", notaCual)