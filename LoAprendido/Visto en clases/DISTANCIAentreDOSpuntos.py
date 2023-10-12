#DISTANCIA ENTRE DOS PUNTOS

import math
def distancia(xt, yt, xs, ys):
   d = math.sqrt((xt-xs)**2+(yt-ys)**2)
   return d 

x1=1
x2=3
y1=2
y2=4   

dist = distancia(x1,y1,x2,y2)
print(f"Si la distancia es {dist:.3f}")

#SUMA DE LADOS(TRIANGULO)

def PerimetroTriangulo(xp,yp,xq,yq,xr,yr):
   Perimetro = distancia()
   return distancia
X1 = 1
Y1 = 4
X2 = 3
Y2 = 0
X3 = 5
Y3 = 3

print(f"el perimetro del triangulo {PerimetroTriangulo(X1,Y1,X2,Y2,X3,Y3):.2f}")   

