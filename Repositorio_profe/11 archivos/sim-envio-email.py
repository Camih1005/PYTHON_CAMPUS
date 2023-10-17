fd = open("Campus Lands\\Ciclo 1\\Grupo-C4-Sep\\Código\\11 archivos\\mbox-short.txt", "r")

fd2 = open("Campus Lands\\Ciclo 1\\Grupo-C4-Sep\\Código\\11 archivos\\envio-emails.txt", "w")

lstEmails = []
for linea in fd:
    if linea.startswith("From:"):
        email = linea.split()[1]
        if email not in lstEmails:
            lstEmails.append(email)

for i in range(len(lstEmails)-1, -1, -1):
    # Enviar el correo
    msj = f"{lstEmails[i]} enviado [ok]"
    print(msj)
    fd2.write(msj+"\n")

fd.close()
fd2.close()