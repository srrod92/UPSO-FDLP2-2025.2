from .IVolar import IVolar
class Avion(IVolar):

    def despegar(self):
        print("Despegando")


    def volar(self):
        print("Volando")


    def aterrizar(self):
        print("Aterrizando")