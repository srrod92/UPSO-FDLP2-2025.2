from abc import ABC, abstractmethod
from Clases.personaje import Personaje
class IHabilidadEspecial(ABC):

    @abstractmethod
    def usar_habilidad(self, enemigo:Personaje):
        pass