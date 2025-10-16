from abc import ABC, abstractmethod ##Esto nos permite generar clases abstractas.
class Personaje(ABC):

    _nombre:str
    _vida: int
    _ataque:int
    _defensa:int

    def __init__(self, nombre_:str,vida_: int, ataque_: int, defensa_:int):
        self._nombre = nombre_
        self._vida = vida_
        self._ataque = ataque_
        self._defensa = defensa_


    @abstractmethod
    def atacar(self, enemigo: "Personaje"):
        pass


    def recibir_ataque(self, ataque_enemigo:int):
        dano = ataque_enemigo - self._defensa
        if dano > 0:
            self._vida -= dano
        
        if self._vida <= 0:
            print(f"{self._nombre} cae en batalla.")


    def esta_vivo(self) -> bool:
        return self._vida > 0



    