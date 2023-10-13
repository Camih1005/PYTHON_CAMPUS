#CUENTA CORREOS DESTINATARIO EN EÑL TEXTO EN EL TEXTO
fd = open("hader_cabrera/archivos/mbox-short.txt","r")

def miFun(email):
    return len(email)

#CONTAR CORREOS DESTINATARIO
"""countCorreos = 0
for linea in fd:
    if linea.startswith("From:"):
        countCorreos += 1
        email = linea.split()[1]
        print(email)
fd.close()
print(f"La cantidad de correos de origen distintos es: {countCorreos}.")"""

#CONTAR CORREOS DESTINATARIO SIN REPETIRSE
setEmail = set()
for linea in fd:
    if linea.startswith("From:"):
        setEmail.add(linea.split()[1])
fd.close()
cl = len(setEmail)
#imprimir correos
"""for email in setEmail:
    print(email)"""
#imprimir correos en orden
"""for email in sorted(setEmail):
    print(email)"""
#imprimir por tamaño de correo
for email in sorted(setEmail, reverse= False, key=miFun):
    print(email)