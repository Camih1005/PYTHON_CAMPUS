                #0      #1     #2    #3      #4
lenguajes = ["python","ruby","php","java","javascript"]
lenguajes.insert(3, "GO")#.insert significa insertar en (3) en el numero de de la lista
lenguajes.insert(0,"c")
lenguajes.remove("ruby") #este metodo de .remove quita el elemento que quieras quitar de la lista
print("php" in lenguajes)#pregunta si php esta en la variable lenguaje
#lenguajes.clear() #hace que se elimine todo lo que hay en la variable lenguaje

print(len(lenguajes))#len significa la cantidad de elementos en la variable en numero enteros
