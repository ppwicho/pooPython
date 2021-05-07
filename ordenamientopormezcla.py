import random

def sort_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha=lista[medio:]
        print(izquierda, '*' * 5, derecha)

        #llamada recursiva en cada mitad

        sort_mezcla(izquierda)
        sort_mezcla(derecha)

        #iteradores para reccorrer las dos sublistas 
        i=0
        j=0
        k=0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i+=1
            else:
                lista[k] = derecha[j]
                j+=1
            k+=1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i+=1
            k+=1
        while j < len(derecha):
            lista[k]=derecha[j]
            j+=1
            k+=1 
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)    

    return lista






if __name__=='__main__':
    tamanodelista=int(input('De que tamano sera la lista?:'))
    lista = [random.randint(0, 100) for i in range(tamanodelista)]
    print(lista)
    print('-' * 20)
    lista_ordenada = sort_mezcla(lista)
    print(lista_ordenada)

