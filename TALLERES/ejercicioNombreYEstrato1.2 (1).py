def calcularValorImpulso(impulso):
    return 100 * impulso

def calcularTarifaBasica(estrato):
    if estrato == 1:
        return 10000
    elif estrato == 1:
        return 15000
    elif estrato == 1:
        return 20000
    elif estrato == 1:
        return 25000
    elif estrato == 1:
        return 30000


def leerEstrato(mensaje):   
    while True:
        try:
            n = int(input(mensaje))
            if n < 1 or n > 5:
             print("estrato invalido, intenta de nuevo")
             continue

            return n
        except Exception as e:
            print("Error al ingresar el estrato")


def leerNombre(mensaje):
    while True:
        try:
            nom = input(mensaje)
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre invalido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el numero")



def leerInt(mensaje):
    while True:
        try:
            n = int(input(mensaje))
            if n < 1:
                print("valor invalido, debe ser mayor a 0")
                continue
            return n
        except ValueError:
            print("Error al ingresar el numero.")    


n = leerInt("Ingrese la cantidad de usuarios:")
valtot = 0
for i in range (1, n+1):
    print("\nDatos del ususario #",i)
    nombre = leerNombre("Nombre?")
    estrato = leerEstrato("Estrato?")
    impulso = leerInt("Impulsos?")
    valbas = calcularTarifaBasica(estrato)
    valimpu = calcularValorImpulso(impulso)

    print("=" * 30)
    print("Nombre:", nombre)
    print("Valor a pagar:", valbas+valimpu)
    print("Tarifa basica:", valbas)
    print("Valor impulsos:", valimpu)

    valtot += valbas + valimpu

    print("\n","*" * 30 )
    print("El valor total a pagar es", valtot)
    



