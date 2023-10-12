def menu():
    print("*"*6 + "MENU DE OPERACIONES" + "*"*6)
    print("1.Calculo de la convinacion.")
    print("2.Convertir texto a numero.")
    print("3.Calcular IVA de una factura.")
    print("4.SALIR")
    print("*"*10)

    while True:
        try:
            opcion=int(input("Elija un numero del 1 al 4: "))
            if(opcion <1 or opcion >4):
                print("Dijitaste mal. Repita la opcion")
                continue
            return opcion
        except Exception as e: #La e significa poner en la consola el tipo de error
    
            print("Error de validacion",e)   



def factorial (num):
    fact = 1
    for i in range(num, 1, -1):
        fact = fact * i
        return fact

def Combinatoria(n , k):

    NumN = factorial(n)
    Numk = factorial(k)
    Numt = (factorial(n-k))

    C = NumN / ((Numk)*(Numt))
    return C

def ElimitarTexto(cadena):
    textCadena = ""
    for i in range(len(cadena)):
      if(cadena[i].isdigit()):
          textCadena = textCadena + cadena[i] 
    return textCadena

def Factura(CsinIva, PorIva):
    PorIva = PorIva / 100
    Total = CsinIva + (CsinIva * PorIva)
    return Total


def leernum1(msg):
    while True:
        try:
            num = int(input(msg))
            if(num<0):
                print("Numero no puede ser negativo")
                continue
            return num                
        except Exception as e:
            print("ERROR , VALOR INCORRECTO", e)
            
def leernum2(msg, n):
    while True:
        try:
            num = int(input(msg))
            if(num<0 or num>n):
                print("Numero no puede ser negativo o mayor a el valor de n")
                continue
            return num                
        except Exception as e:
            print("ERROR , VALOR INCORRECTO", e)

def LeerCadena(msg):
      while True:
        try:
            cadena = input(msg)
            cadena = cadena.strip()
            if(cadena == ""):
                print("Cadena no puede ser vacia, no puede contener caracteres especiales")
                continue
            return cadena             
        except Exception as e:
            print("ERROR , VALOR INCORRECTO", e)
            
def LeerValorsinIva(msg):
        while True:
            try:
                num = float(input(msg))
                if(num<0):
                    print("Numero no puede ser negativo")
                    continue
                return num                
            except Exception as e:
                print("ERROR , VALOR INCORRECTO", e)
    
            
def LeerPorcentaje(msg):
        while True:
            try:
                Porc = float(input(msg))
                if(Porc<0):
                    print("Numero no puede ser negativo")
                    continue
                return Porc        
            except Exception as e:
                print("ERROR , VALOR INCORRECTO", e)
                
def main():
    opcion = menu()
    
    while opcion!=4:
        if(opcion==1):
            n = leernum1("Digite el valor de n: ")
            k = leernum2("Digite el valor de k: ", n)
            C = Combinatoria(n,k)
            print(f" eL VALOR DE LA COMBINATORIA ES: {C}")
        elif(opcion==2):
            Cadena = LeerCadena("Digite una cadena de texto y numeros : ")
            CadenasinTexto = ElimitarTexto(Cadena)
            print(f" Cadena sin Letras: {CadenasinTexto}")
        elif(opcion==3):
            ValorsinIva = LeerValorsinIva("Digite el valor sin el iva: ")
            porcentaje = LeerPorcentaje("Digite el porcentaje aplicado al valor: ")
            ValorConiVA= Factura(ValorsinIva,porcentaje)
            print(f"El valor Total con iva es: {ValorConiVA:,.1f}")
    
        if(opcion==4):
            return True
            
        else:
            opcion = menu()
            
main()   





