

import math
def distancia(xt, yt, xs, ys):
   d = math.sqrt((xt-xs)**2+(yt-ys)**2)
   return d

def PerimetroTriangulo(xp,yp,xq,yq,xr,yr):
    perimetro=distancia(xp,yp,xr,yr)+distancia(xr,yr,xq,yq)+distancia(xq,yq,xp,yp)
    return perimetro

X1 = 1
Y1 = 4
X2 = 3
Y2 = 0
X3 = 5
Y3 = 3

print(f"el perimetro del triangulo {PerimetroTriangulo(X1,Y1,X2,Y2,X3,Y3):.3f}")  

