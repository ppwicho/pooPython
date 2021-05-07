import random

def busqueda_lineal(lista,objetivo):
    match = False
    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break

    return match

if __name__=='__main__':
    tamanodelista=int(input('De que tamano sera la lista?:'))
    objetivo=int(input('¿Que numero quieres encontrar?:'))
    lista=sorted([random.randint(0,100) for i in range(tamanodelista)])

    encontrado=busqueda_lineal(lista,objetivo)


    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "NO esta"} en la lista')


