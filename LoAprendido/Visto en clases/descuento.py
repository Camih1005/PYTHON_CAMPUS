def descuento (VAlorart):
    if VAlorart > 150.000:
        descuento = VAlorart * 0.05
        
    else:
        descuento = 0
    return descuento
valor = int(input("Ingrese el valor del articulo:"))
descuento = descuento(valor)
print(f"el valor del descuento es:${descuento:,}")
 