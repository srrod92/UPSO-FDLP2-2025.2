from .elemento import Elemento
from .vacio import Vacio
from .pinche import Pinche

class Mc(Elemento):

    def __init__(self, posFila, posColumna):
        super().__init__("🎃")
        self.pos_fila = posFila
        self.pos_columna = posColumna
    
        

    def colision(self, objeto)-> bool:

        if isinstance(objeto, Vacio):
            return False
        
        if isinstance(objeto, Pinche):
            return True
        
        pass

    