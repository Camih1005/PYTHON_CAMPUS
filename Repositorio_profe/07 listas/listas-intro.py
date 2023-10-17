milista= [] # lista vacia
milista2 = list() # lista vacia

nomCampers = ["Juan", "Yulieth", "Lorenzo", "Manuel", "David"]
print(nomCampers)
print(nomCampers[1])
nomCampers[1] = "Julieth"
print(nomCampers[1])

# SLICES
print(nomCampers[2:4])
print(nomCampers[::-1])

nomCampers_juan = ["Daniela", "Maria", "Juliana", "Sandra", "Carolina"]
print(nomCampers_juan)
# nomCampers += nomCampers_juan
# print(nomCampers)

# METODOS DE LISTAS
nomCampers.append("Kevin")
print(nomCampers)

nomCampers.extend(nomCampers_juan)
print(nomCampers)
print(nomCampers[-1])

nomCampers.insert(1, "Carlos")
print(nomCampers)

nomCampers.pop()
print(nomCampers)

nomCampers.pop(-3)
print(nomCampers)

nomCampers.remove("Sandra")
print(nomCampers)

nomCampers.sort()
print(nomCampers)

nomCampers.insert(2,"Daniel")
nomCampers.sort()
print(nomCampers)

# list2 = [0,1,15,"115"]
# list2.sort()
# print(list2)

nomCampers.sort(reverse=True)
print(nomCampers)
