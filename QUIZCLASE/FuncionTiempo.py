import time

empiezo = time.time()
input("Dijiste algo para calcular lo que te demoras:")
termino = time.time()
segundos = termino-empiezo
print(f"Tardaste  {segundos:,.3f},Segundos")