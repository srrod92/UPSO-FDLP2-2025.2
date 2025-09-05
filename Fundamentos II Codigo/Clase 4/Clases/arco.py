from Clases.arma import Arma

class Arco(Arma):

    def __init__(self):
        self.dano = 15
        self.peso = 1

    def apuntar(self):
        print("El arco esta apuntando a su enemigo.")


    def atacar(self):
        self.apuntar()
        print(f"La flecha impacta sobre el enemigo causando {self.dano} puntos de daño")