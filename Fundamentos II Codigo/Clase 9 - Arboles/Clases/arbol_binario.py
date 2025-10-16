from .nodo import Nodo
class ArbolBinario:

    def __init__(self, raiz= None):
        self.raiz = raiz
      

    def insertar(self, data:int):
        
        if self.raiz == None:
            self.raiz = Nodo(data)
        else:
            self._insertar_rec(self.raiz, data)

    
    def _insertar_rec(self, nodoActual:Nodo, data:int):
        if data < nodoActual.data:
            if nodoActual.izquierdo == None:
                nodoActual.izquierdo = Nodo(data)
                
            else:
                self._insertar_rec(nodoActual.izquierdo, data)
        else:
            if nodoActual.derecho == None:
                nodoActual.derecho = Nodo(data)
                
            else:
                self._insertar_rec(nodoActual.derecho, data)


    def imprimir_preorden(self, nodoActual:Nodo):
        if nodoActual == None:
            return
        print(nodoActual.data)
        self.imprimir_preorden(nodoActual.izquierdo)
        self.imprimir_preorden(nodoActual.derecho)

    
    def imprimir_inorden(self, nodoActual:Nodo):
        #Izquierdo, raiz, derecho

        if nodoActual == None:
            return
        
        self.imprimir_inorden(nodoActual.izquierdo)
        print(nodoActual.data)
        self.imprimir_inorden(nodoActual.derecho)


    def imprimir_posorden(self, nodoActual:Nodo):
        if nodoActual == None:
            return
        
        self.imprimir_posorden(nodoActual.izquierdo)
        self.imprimir_posorden(nodoActual.derecho)
        print(nodoActual.data)


        





        
            


        