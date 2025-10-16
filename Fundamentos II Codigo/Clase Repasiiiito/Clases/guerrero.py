from .personaje import Personaje
from Interfaces.ihabilidad_especial import IHabilidadEspecial
class Guerrero(Personaje, IHabilidadEspecial):
    
    def __init__(self, nombre_:str,vida_: int, ataque_: int, defensa_:int):
        super().__init__(nombre_,vida_,ataque_, defensa_)
        self._furia = 40

    def atacar(self, enemigo: Personaje):
        print("Por el Reino de Ramon!")
        enemigo.recibir_ataque(self._ataque)
    

    def recibir_ataque(self, ataque_enemigo):
        super().recibir_ataque(ataque_enemigo)
        
        if self.esta_vivo:
            self._furia += 20

            if self._furia > 100:
                self._furia = 100


    def usar_habilidad(self, enemigo):
        if self._furia > 30:
            print("SANGRE!!")
            enemigo.recibir_ataque(self._ataque*2)
            self._furia -= 30
        else:
            print("Me duele el dedo.")

        
        