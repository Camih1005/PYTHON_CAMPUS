texto = "Hola Mundo"

print(texto.upper()) #METODO QUE PONE EL TEXTO EN MAYUSCULA PERO SIMPRE TIENE QUE TENRE UN PARENTISIS AL LADO DEL TEXTO()
print(texto.lower()) #lo mismo que upper pero pone en minuscula
print(texto.find("M")) # .find sirve para saber en que numero de pocision esta la letra que se le asigne
nuevoTexto = texto.replace("Mun", "Hola mundo")#este metodo remplaza una palabra que selecciones por la que pongas
print(texto, nuevoTexto)
print("Mundo" in texto) # (boolean) in significa Mundo esta "in" texto y imprime si es true o false
