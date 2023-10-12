def findElemListPos(lst, elem):

#funcion que busca elemenro en le lista
#si lo encuentra devuelve la p(posicion)
#si no lo encuentra devuelve a menos -1 (return -1)
    for p in range(len(lst)):
        if elem == lst[p]:
            return p
        
    return -1    

def findElenList(lst, elem):
#funcion que busca un elemento en la lista
#si lo encuentra devuelve true
#si no lo encuentra devielve false
 for e in lst:
    if e == elem:
        return True
 return False
