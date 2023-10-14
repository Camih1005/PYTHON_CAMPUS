import json
nombre_archivo= open("/home/spukN01-/Documents/CCamilo/LoAprendido/CamiloQUIZ.py/mbox.txt","r")
spam = open("/home/spukN01-/Documents/CCamilo/LoAprendido/CamiloQUIZ.py/mbox.txt","r")
archivo = input("Dijite el nombre del archivo:")

try:
    with open(nombre_archivo, 'r') as archivo:
        total_spam_confidence = 0.0
        cantidad_correos = 0
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error al procesar el archivo: {str(e)}")
emailss=[]
listSpam=[]
for linea in spam:
    if linea.startswith("From:"):
        email = linea.split()[1]
        emailss.append()(email)
    if linea.startswith("X-DSPAM-Confidence"):
        sPam = linea.split()[1]
        if sPam not in listSpam:
            listSpam.append(sPam)
            
for i in range(len(listSpam)-1, 0, -1):
    msj = (f"{listSpam[i]} Spam")
    print(msj)
    
setEmail = set()
for linea in spam:
    if linea.startswith("X-DSPAM-Confidence"):
        setEmail.add(linea.split()[1])
    
            
            
spam.close()          

