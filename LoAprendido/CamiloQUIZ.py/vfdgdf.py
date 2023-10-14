# Solicitar al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

try:
    # Abrir el archivo en modo lectura
    with open(nombre_archivo, 'r') as archivo:
        total_spam = 0
        total_correos = 0

        # Leer cada línea del archivo
        for linea in archivo:
            if linea.startswith("X-DSPAM-Confidence:"):
                # Extraer el valor de confianza del SPAM de la línea
                valor_confianza = float(linea.split(":")[1].strip())
                total_spam += valor_confianza
                total_correos += 1

        if total_correos > 0:
            promedio_spam = total_spam / total_correos
            print(f"El índice promedio de SPAM es: {promedio_spam}")
        else:
            print("No se encontraron correos con información de SPAM en el archivo.")

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no existe.")
except Exception as e:
    print(f"Se produjo un error: {str(e)}")
