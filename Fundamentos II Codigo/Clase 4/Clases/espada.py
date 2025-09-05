from Clases.arma import Arma

class Espada(Arma):

    def __init__(self):
        self.dano = 30
        self.peso = 2.3

    
    def estocada(self):
        print("La espada estoca al enemigo.")


    def atacar(self):
        self.estocada()

