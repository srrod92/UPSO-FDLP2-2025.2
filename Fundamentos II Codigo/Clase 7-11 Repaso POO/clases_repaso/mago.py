from .criatura import Criatura
class Mago(Criatura):
    
    def __init__(self, nombre: str, vida:int, ataque:int, defensa:int, mana:int):
        super().__init__(nombre, vida,ataque,defensa)
        self.mana = mana

    
    def atacar(self, objetivo:Criatura):
        dano_real = self.ataque + self.mana / 2
        objetivo.recibir_dano(dano_real)
        

