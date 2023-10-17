fd = open("/home/spukN01-/Documents/CCamilo/LoAprendido/ArchivosAprendido/mbox-short.txt","r")

fd2 = open("/home/spukN01-/Documents/CCamilo/LoAprendido/ArchivosAprendido/ARCHIVOCREADO.txt","w")

LstEmails = []
for linea in fd:
    if linea.startswith("From:"):
        email = linea.split()[1] #"el [] esta en la pocision 1" 
        if email not in LstEmails:
            LstEmails.append(email)
            
for i in range(len(LstEmails)-1, 0, -1):
    msj = f"{LstEmails[i]} enviado [ok]"
    print(msj)
    fd2.write(msj+"\n")
            
            
fd.close()
fd2.close()