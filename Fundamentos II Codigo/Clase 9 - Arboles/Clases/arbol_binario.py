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


    def eliminar(self, raiz:Nodo, valor:int):
        if raiz == None:
            return
        
        #Primero buscar el nodo a eliminar.
        if valor < raiz.data:
            raiz.izquierdo = self.eliminar(raiz.izquierdo, valor)
            

        elif valor > raiz.data:
            raiz.derecho = self.eliminar(raiz.derecho, valor)
            

        else: #Este caso es el que encuentra el nodo a eliminar.

            if raiz.izquierdo == None and raiz.derecho == None: #Caso donde tengo que eliminar una hoja
                return None
            
            elif raiz.izquierdo == None: #Caso donde hay un solo hijo y esta a la derecha
                return raiz.derecho
            
            elif raiz.derecho == None: #Caso donde hay un solo hijo y esta a la izquierda
                return raiz.izquierdo
            
            else: #Caso donde hay dos hijos -> Esto se lo dificil.

                posterior = self._busqueda_menor(raiz.derecho)

                raiz.data = posterior.data

                raiz.derecho = self.eliminar(raiz.derecho, posterior.data)
        return raiz

   
    
    def _busqueda_menor(self, raiz:Nodo)-> Nodo:
        if raiz == None:
            return None
        
        nodo_actual = raiz
        while nodo_actual.izquierdo != None:
            nodo_actual = nodo_actual.izquierdo

        return nodo_actual
    
