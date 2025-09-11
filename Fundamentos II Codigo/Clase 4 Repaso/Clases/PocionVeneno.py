from .item import Pocion

class PocionVeneno(Pocion):

    _valor:int = -30
    def __init__(self):
        self._efecto = "Envenenar"


    def usar(self) -> int:
        print("La pocion era un liquido verde.")
        return self._valor
    

    def get_efecto(self):
        print(f"Mi efecto es {self.efecto}")