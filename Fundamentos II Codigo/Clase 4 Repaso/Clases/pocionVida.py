from .item import Pocion

class PocionVida(Pocion):

    valor:int = 10

    def __init__(self, efecto_:str):
        super().__init__(efecto_)



    def get_efecto(self):
        print(f"Soy una pocion de Vida y mi efecto es {self.efecto}")


    def usar(self) -> int:
        print("El liquido es cristalino.")
        return self.valor