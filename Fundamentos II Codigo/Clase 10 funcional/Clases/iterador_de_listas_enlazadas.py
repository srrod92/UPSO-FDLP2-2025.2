class IteradorListaEnlazada:

    def __init__(self, lista_enlazada):
        self.actual = lista_enlazada.head


    def __next__(self):
        ##Devolver el dato actual
        ## Actualizar la referencia a actual.
        ## cuando no tenga mas datos para devolver tiene que avisar que termino
        if self.actual != None:
            aux = self.actual
            self.actual = self.actual.siguiente
            return aux
        else:
            raise StopIteration
        

  

        