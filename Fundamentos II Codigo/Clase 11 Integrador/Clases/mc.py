from .elemento import Elemento
from .vacio import Vacio
from .pinche import Pinche
from .puerta import Puerta
from .llave import Llave

class Mc(Elemento):

    def __init__(self, posFila, posColumna):
        super().__init__("🎃")
        self.pos_fila = posFila
        self.pos_columna = posColumna
        self.llave = 0
    
        

    def colision(self, objeto)-> bool:

        if isinstance(objeto, Vacio):
            return False
        
        if isinstance(objeto, Pinche):
            return True
        
        if isinstance(objeto, Puerta):
            if self.llave > 0:
                print("Escapaste")
                return True
            else:
                print("Te falta la llave.")
                input("Presione una tecla para continuar.")
                return False
        
        if isinstance(objeto, Llave):
            self.llave +=1

        
        pass

    def get_position(self):
        return self.pos_fila, self.pos_columna

    