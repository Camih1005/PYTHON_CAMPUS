s = "yo soy tu padre"
# print(s[7])
# print(s[-8])

# recorrer las cadenas
# recorrido por indice
# for i in range(len(s)):
#     print(s[i], end=", ")
    
# recorrido por elemento
# print("")
# for e in s:
#     print(e, end=", ")

# # slice
# print("")
# print(s[2:])
# print(s[4:7])
# print(s[::-1])


# Operador in
print("tu" in s)  
print ("yt" not in s)

# count
print(s.count("o"))

# find
print(s.find("pa"))
print(s.find("ma"))

# isdigit()
snum = "100"
print(snum.isdigit())
snum = "100a"
print(snum.isdigit())

#split()
nombre = "Juan Daniel  Ramirez Salazar"
email = "juandaniel@gmail.com"
miles = "1.234.231"
print(nombre.split())
print(nombre.split("Daniel"))
print(email.split("@"))
print(miles.split("."))