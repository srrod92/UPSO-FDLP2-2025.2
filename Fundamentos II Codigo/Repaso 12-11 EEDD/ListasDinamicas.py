import random
def CrearListaDeEnterosAleatorios(largo:int) -> list:
    #[0,1,2,3,.....largo]
    lista = []
    for i in range(largo):
        #lista.append(random.randint(0,9)) 
        numero = random.randint(0,3)
        lista.append(numero)

    return lista


def BuscarNumero(buscado:int, lista:list) -> bool:
    for numero in lista:
            if numero == buscado:
                 return True
    return False






## Crear un metodo que elimine todas las 
# instancias de un numero en particular


## Recibir la lista, y lo que hay que eliminar
## Recorro la lista por indice, 
# y si el dato que esta en ese indice es el que tengo que eliminar,
# hago pop(indice)


def eliminar(buscado, lista): #MAriela
    i = 0
    while i < len(lista):
        if lista[i] == buscado:
            lista.pop(i)  
        else:
            i += 1        
    return lista


def sacar_x_numero_de_la_lista(lista:list, x:int) -> list: #Lucas
    i=0
    while i < len(lista):
        if lista[i]==x:
            print(i)
            print(lista[i])
            lista.pop(i)
        else:
            i +=1
    return lista

        

    
                    





def main():

    lista = CrearListaDeEnterosAleatorios(20)
    print(lista)
    sacar_x_numero_de_la_lista(lista,2)
    print(lista)



main()



