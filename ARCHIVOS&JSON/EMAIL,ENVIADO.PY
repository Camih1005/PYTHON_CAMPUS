fd = open("/home/spukN01-/Documents/CCamilo/LoAprendido/ArchivosY_JSON/mbox-short.txt","r")
setEmail = set()
for linea in fd:
    if linea.startswith("To:"):
        setEmail.add(linea.split()[1])

fd.close()
for email in setEmail:
    print(f"{email} ENVIADO [OK]")