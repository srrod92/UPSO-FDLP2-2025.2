from .nodo import Nodo
class ListaEnlazada:

    head:Nodo

    def __init__(self, head_ :Nodo = None):
        self.head = head_



    #3Inserta un nodo en la lista, Si index es None lo inserta en la ultima posicion, de lo contrario lo inserta en index desplazando todos los otros nodos.
    def insertar_nodo(self, nuevo_nodo:Nodo, index:int = None):

        if index != None and index < 0: #Este caso es si el indice es negativo.
            return None
        
        if self.head == None: # Si la cabeza no existe.
            self.head = nuevo_nodo
            print("El indice no existe, se agrego en la ultima posición.")
            return
        
        
        contador:int = 0
        puntero:Nodo = self.head

        if index == None: # Si SE que tengo que insertar al final.
            while puntero.nodo_siguiente != None:
                puntero = puntero.nodo_siguiente

            puntero.nodo_siguiente = nuevo_nodo
            return


        # Metodo default
        while puntero.nodo_siguiente != None and contador < index-1:
            puntero = puntero.nodo_siguiente
            contador += 1

        if puntero.nodo_siguiente != None:
            nuevo_nodo.nodo_siguiente = puntero.nodo_siguiente

        puntero.nodo_siguiente = nuevo_nodo

        
    #2 Retorna el nodo que se encuentra en el indice dado, retorna None si no existe el indice.
    def buscar_en_indice(self, indice:int):

        if indice < 0:
            return None

        if self.head == None:
            return None
        
        contador:int = 0
        puntero:Nodo = self.head

        while puntero.nodo_siguiente != None and contador < indice:
            puntero = puntero.nodo_siguiente
            contador += 1

        if contador != indice:
            return None
        
        return puntero

        

    #1 Pone un nuevo head en la lista enlazada. El viejo pasa a ser index 1.
    def setear_head(self, nuevo_nodo:Nodo):
        nuevo_nodo.nodo_siguiente = self.head
        self.head = nuevo_nodo
    

    #4Si index es None, elimina el ultimo, de lo contrario elimina el index.
    def eliminar_nodo(self, index:int = None):
        if self.head == None: #Si no hay cabeza, no hay nada que eliminar.
            return
        
        if index != None and index < 0: #Si el indice no es negativo no es correcto.
            return
        
        if index == 0: ##Si el indice es 0 elimino el root.
            self.head = self.head.nodo_siguiente
        

        if index != None: # Si tengo que eliminar en un indice en particular.

            puntero = self.buscar_en_indice(index-1) #Busco el anterior a ese indice.
            if puntero != None: #Si existe el anterior.
                if puntero.nodo_siguiente != None:
                    puntero.nodo_siguiente = puntero.nodo_siguiente.nodo_siguiente #Elimino en el indice correcto.
                return
            else:
                return #Si no existe el anterior, no hay nada que eliminar.


        puntero:Nodo = self.head


        if index == None: #En este caso tengo que eliminar el ultimo.
            while puntero.nodo_siguiente != None:
                if puntero.nodo_siguiente.nodo_siguiente == None: 
                    print("Entra")
                    puntero.nodo_siguiente = None
                    return
                
                
                puntero = puntero.nodo_siguiente
            return
        

       