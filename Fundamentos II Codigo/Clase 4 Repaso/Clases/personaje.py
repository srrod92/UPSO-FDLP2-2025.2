from .item import Pocion
class Personaje:

    vida:int
    
    mochila:Pocion = None

    def __init__(self, vida_:int):
        self.vida = vida_

    def agregar_objeto_a_la_mochila(self, objeto:Pocion):
        self.mochila = objeto

    def usar_objeto(self):
        if self.mochila != None:
            self.vida += self.mochila.usar()
            self.mochila = None
        else:
            print("La mochila esta vacia.")

    def get_vida(self):
        print(f"El personaje tiene {self.vida} puntos de vida.")