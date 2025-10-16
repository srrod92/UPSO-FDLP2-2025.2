from .personaje import Personaje
from random import Random
class Arquero(Personaje):
    
    def __init__(self, nombre_:str,vida_: int, ataque_: int, defensa_:int):
        super().__init__(nombre_,vida_,ataque_, defensa_)
        self._enfoque = 30

    def atacar(self, enemigo: Personaje):
        super().atacar(enemigo)
        print("Otro gato!")
        enemigo.recibir_ataque(self._ataque)

        self._enfoque = min(100, self._enfoque + 10)


    def usar_habilidad(self, enemigo:Personaje):
        dado = Random.randint(0,99)
        if dado <= self._enfoque:
            print("En el ojo pa")
            enemigo.recibir_ataque(self._ataque*2)
            self._enfoque = 0
        else:
            print("No estoy lo suficientemente enfocado.")
            self._enfoque += 10
            


        
     



"""
enfoque es una prob. de critico.
cada vez que hacemos la habilidad tiramos un dado. Si sale critico sumamos enfoque
si pifiamos restamos enfoque.

Cada vez que atacamos normal, ganamos un poquito de enfoque.

"""