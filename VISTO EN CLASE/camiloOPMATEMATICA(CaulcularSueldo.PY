def menu():
    print("*"*15)
    print(".Menu operaciones.")
    print("1.Factorial de un numero")
    print("2.Calcular salario de un empleado")
    print("3.Calcular palabras en un parrafo")
    print("4.SALIR.")
    print("*"*15)
    
    while True:
        try:
            opcion = int(input("Dijite el numero correspondiente:"))
            if(opcion<1 or opcion>4):
                print("Dijite el numero correspondiente")
                continue
            return opcion
        except Exception as e:
            print("Error", e)

def factorial(num):
    fac = 1
    for i in range(num, 1, -1):
        fac = fac * i
        return fac 

def salarioEmpleado(NumeroHora, SalarioHora):
    SalarioRegular=0
    SalarioExtra=0
    GananciaTotal=0

    if(NumeroHora <= 40): 
        SalarioRegular = NumeroHora * SalarioHora
        SalarioExtra = (NumeroHora-40) * (1.5*SalarioHora)
        GananciaTotal = SalarioRegular + SalarioExtra
        print(f"El salario regular del empleado es de: {SalarioRegular}")
        print(f"El salario regular de horas extras del empleado es de: {SalarioExtra}")
    return(GananciaTotal)

def NumeroPalabras(texto):
    texto = texto.strip()
    cont=0
    texto =texto.split(" ")
    for i in range(len(texto)):
        