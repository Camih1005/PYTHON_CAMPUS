                #0      #1     #2    #3      #4
lenguajes = ["python","ruby","php","java","javascript"]

i = 1
while i <= 5: # while repite la secuencia hasta que termine de cumpli la condicion, en este caso es while si i es menor o igual a 5 sigue con la secuencia, pero si no cumple pues hasta ahii para el bucle
    print(i* "el gordo") #es lo mismo pero en texto
    i = i + 1

i = 0
while i < len(lenguajes):
        print(lenguajes[i])
        i = i + 1