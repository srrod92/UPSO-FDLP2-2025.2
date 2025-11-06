from .elemento import Elemento
class Puerta(Elemento):
    def __init__(self, posFila, posColumna):
        super().__init__("🚪")
        self.pos_fila = posFila
        self.pos_columna = posColumna

    def colision(self, objeto):
        pass

    def get_position(self):
        return self.pos_fila, self.pos_columna


    def __str__(self):
        return self.imagen