from abc import ABC, abstractmethod


class Pocion(ABC):
    _efecto:str

    def __init__(self, efecto_:str):
        self.efecto = efecto_
        

    @abstractmethod
    def get_efecto(self):
        pass


    @abstractmethod
    def usar(self):
        pass


    