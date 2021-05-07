import random

def busqueda_binaria(lista,comienzo,final,objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2 # // División de enteros 

    if lista[medio] == objetivo: 
        return True
    
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista,medio +1 ,final,objetivo)
    else:
        return busqueda_binaria(lista,comienzo,medio-1,objetivo)


if __name__=='__main__':
    tamanodelista=int(input('De que tamano sera la lista?:'))
    objetivo=int(input('¿Que numero quieres encontrar?:'))
    lista=sorted([random.randint(0,100) for i in range(tamanodelista)])


    print(lista)

    encontrado=busqueda_binaria(lista,0,len(lista),objetivo)

    

    print(f'El elemento {objetivo} {"esta" if encontrado else "NO esta"} en la lista')

