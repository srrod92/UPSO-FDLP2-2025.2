from abc import ABC, abstractmethod

class Vehiculo(ABC):
    ruedas:int
    puertas:int
    def __init__(self,ruedas_:int, puertas_:int):
        self.ruedas = ruedas_
        self.puertas = puertas_
    
    def get_ruedas(self):
        print(f"Tengo {self.ruedas} ruedas.")

    @abstractmethod
    def get_puertas(self):
        pass