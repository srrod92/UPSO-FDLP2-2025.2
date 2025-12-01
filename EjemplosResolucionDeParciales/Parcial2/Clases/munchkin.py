from .puerta import Puerta
from .puerta_tesoro import PuertaTesoro
from .puerta_monstruo import PuertaMostruo
class Munchkin:
    ataque:int
    nivel:int

    def __init__(self, nivel, ataque):

        self.nivel = nivel
        self.ataque = ataque


    def abrir_puerta(self, puerta:Puerta):
        if (isinstance(puerta, PuertaTesoro)):
            bonificacion = puerta.abrir()
            print(f"Munchkin gana {bonificacion} puntos de fuerza")
            self.ataque += bonificacion

        elif (isinstance(puerta, PuertaMostruo)):
            ataque = puerta.abrir()
            
            if (ataque < (self.ataque+self.nivel)):
                print(f"Munchkin gana el combate.")
                self.nivel +=1
            else:
                print("Muchking no consiguio derrotar al monstruo.")
