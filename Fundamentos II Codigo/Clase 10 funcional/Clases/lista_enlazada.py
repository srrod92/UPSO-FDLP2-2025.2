from .nodo import Nodo
from .iterador_de_listas_enlazadas import IteradorListaEnlazada
class ListaEnlazada:   

    def __init__(self, iterable = None):
        self.head = None
        if iterable != None:
            for elemento in iterable:
                if (isinstance(elemento, Nodo)):
                    self.agregar(Nodo(elemento.data))
                else:
                    self.agregar(Nodo(elemento))






    def agregar(self, nuevo:Nodo):    
        if self.head == None:
            self.head = nuevo
        else:
            actual = self.head
            while actual.siguiente != None:
                actual = actual.siguiente                
            actual.siguiente = nuevo



    def imprimir_data(self):
        if self.head == None:
            return
        else:
            actual = self.head
            while actual != None:
                print(actual.data)
                actual = actual.siguiente


    def __iter__(self):
        return IteradorListaEnlazada(self)

      

"""
    def __iter__(self):
        return IteradorListaEnlazada(self)
    
 
    def __iter__(self):
        actual = self.head
        while actual != None:
            yield actual
            actual = actual.siguiente
"""