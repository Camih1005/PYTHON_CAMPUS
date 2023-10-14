import json
nombre_archivo = input("ingrese el nombre del archivo a procesar: ")

try:
    with open(nombre_archivo, 'r') as archivo:
        total_spam_confidence = 0.0
        cantidad_correos = 0

        
        for linea in archivo:
            if linea.startswith("X-DSPAM-Confidence:"):
                spam_confidence = float(linea.split(":")[1].strip())
                total_spam_confidence += spam_confidence
                cantidad_correos += 1

        if cantidad_correos > 0:
            
            promedio_spam = total_spam_confidence / cantidad_correos
            print(f"El índice promedio de SPAM en el servidor de correo es: {promedio_spam}")
        else:
            print("No se encontraron registros de X-DSPAM-Confidence en el archivo.")

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error al procesar el archivo: {str(e)}")

