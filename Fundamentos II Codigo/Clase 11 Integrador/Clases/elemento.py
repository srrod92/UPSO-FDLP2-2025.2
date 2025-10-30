from abc import ABC, abstractmethod
class Elemento(ABC):
    def __init__(self, imagen):
        self.imagen = imagen        
    

    def imprimir(self):
        print(self.imagen, end = "")

    @abstractmethod
    def colision(self, objeto):
        pass


    def __str__(self):
        return self.imagen
    