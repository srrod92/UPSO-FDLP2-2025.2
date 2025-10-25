from functools import reduce
from Clases.lista_enlazada import ListaEnlazada
from Clases.nodo import Nodo


def contador():
    actual = 1
    while actual < 10:        
        yield actual
        actual+=1

lista_dinamica = [0,1,2,3,4,5,6,7,8,9,10]

lista = ListaEnlazada()

lista.agregar(Nodo(1))
lista.agregar(Nodo(3))
lista.agregar(Nodo(4))
lista.agregar(Nodo(16))
lista.agregar(Nodo(11))
lista.agregar(Nodo(2))
lista.agregar(Nodo(43))
lista.agregar(Nodo(12))
lista.agregar(Nodo(33))

gen = contador()


print(lista.__iter__())