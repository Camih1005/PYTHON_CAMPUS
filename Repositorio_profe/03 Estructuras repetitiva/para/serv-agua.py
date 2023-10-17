n = int(input("Cuantos usuarios? "))

for i in range(1, n+1):
    print(f"\nDatos del usuario #{i}")
    cod = input("Codigo? ")
    nom = input("Nombre? ")
    est = input("Estado [V: vigente o S: Supendido]?")
    estr = int(input("Estrato [1 al 6]? "))
    con = float(input("Consumo agua al mes [cm3]? "))
    
    if est == "V" or est == "v":
        # Calcular la tarifa basica
        if estr == 1:
            tbas = 10000
        elif estr == 2:
            tbas = 20000
        elif estr == 3:
            tbas = 30000
        elif estr == 4:
            tbas = 45000
        elif estr == 5:
            tbas = 60000
        elif estr == 6:
            tbas = 70000
        else:
            tbas = 0
        
        # calcular el valor del consumo
        valcons = con * 200
        
        # calcular el valor a pagar
        valpagar = tbas + valcons
        
        # imprimir el informe del usuario
        print("\n", "=" * 40)
        print("\tNombre: ", nom)
        print(f"\tValor tarifa básica: ${tbas:,}")
        print(f"\tValor consumo: ${valcons:,.0f}")
        print(f"\tValor de la factura de agua: ${valpagar:,.0f}")