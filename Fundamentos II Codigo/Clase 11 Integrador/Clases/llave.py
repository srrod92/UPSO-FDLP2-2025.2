from .elemento import Elemento
class Llave(Elemento):
    def __init__(self):
        super().__init__("🔑")

    def colision(self, objeto):
        pass


    def __str__(self):
        return self.imagen