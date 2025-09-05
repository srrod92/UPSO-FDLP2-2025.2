from Clases import *
from Interfaces.idanable import IDanable

class Personaje(IDanable):

    vida:int
    carga:float
    arma_equipada:Arma

    def __init__(self, arma_:Arma, vida_:int = 100):
        self.arma_equipada = arma_
        self.vida = vida_
        self.carga = self.arma_equipada.get_peso()

    def atacar(self):
        self.arma_equipada.atacar()


    def recibir_dano():
        print("Recibe daño como un personaje lo haria.")