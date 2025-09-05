from Clases.arma import Arma

class Hacha(Arma):

    def __init__(self):
        self.dano = 60
        self.peso  = 5


    def golpe_con_el_canto(self):
        print("El hacha golpea con el canto")

    
    def atacar(self):
        self.golpe_con_el_canto()


    