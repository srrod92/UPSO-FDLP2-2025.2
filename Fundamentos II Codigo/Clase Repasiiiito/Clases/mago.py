from .personaje import Personaje
class Mago(Personaje):
    
    def __init__(self, nombre_:str,vida_: int, ataque_: int, defensa_:int):
        super().__init__(nombre_,vida_,ataque_, defensa_)
        self._mana = 50

    def atacar(self, enemigo: Personaje):
        super().atacar(enemigo)
        print("Por los hierbas de Gandalf")
        enemigo.recibir_ataque(self._ataque)
        self._mana += 10

        if self._mana > 100:
            self._mana = 100



    def usar_habilidad(self, enemigo: Personaje):
        if self._mana > 20:
            enemigo.recibir_ataque(self._mana + self._ataque)
            self._mana = 0
        else:
            print("Labios compartidos")
           
