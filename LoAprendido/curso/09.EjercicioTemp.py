temperatura = float(input("Ingrese temperatura a convertir: "))
convertir = input("Fahrenheit(F) O Celsius(C?: ").lower()

if convertir == ("f"):
    celsius = (temperatura - 32) * 5/8
    print(celsius)

elif convertir == ("c"):
    fahrenheit = (temperatura * 1.8 ) + 32  
    print(fahrenheit)
else:
    print("incorrecto")         




