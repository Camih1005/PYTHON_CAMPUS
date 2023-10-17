# Un programa que cuente y muestre los correos de origen distintos que hay en el mbox.txt.
def miFun(email):
    return len(email)

fd = open("Campus Lab\\Ciclo 1\\Grupo-C4-Sep\\Código\\11 archivos\\mbox-short.txt", "r")

# cl = 0
setEmail = set()
for linea in fd:
    if linea.startswith("From:"):
        # cl += 1
        # email = linea.split()[1]
        # print(email)
        setEmail.add(linea.split()[1])
        

fd.close()
cl = len(setEmail)
print("Cantidad de correos de origen distintos:", cl)
for email in sorted(setEmail, reverse=False, key=miFun):
    print(email)