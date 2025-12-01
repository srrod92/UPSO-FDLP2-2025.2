from .puerta import Puerta
class PuertaTesoro(Puerta):
    bonificacion: int

    def __init__(self, nivel, bonificacion):
        self.bonificacion = bonificacion
        self.nivel = nivel


    def abrir(self):
        super().abrir()
        print(f"Dentro habia un tesoro con bonificación {self.bonificacion}")
        return self.bonificacion
    



    def __str__(self):
        return f"La puerta tesoro nivel {self.nivel} tiene {self.bonificacion} puntos de bonificación."