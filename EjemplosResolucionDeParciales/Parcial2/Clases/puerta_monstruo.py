from .puerta import Puerta
import random
class PuertaMostruo(Puerta):
    ataque:int
    ataque_posible: list[int]

    def __init__(self, nivel:int):
        
        self.nivel = nivel
        self.ataque_posible = []

        for i in range(10):
            self.ataque_posible.append(random.randint(1,10))

        self.ataque = random.choice(self.ataque_posible)
        


    def abrir(self):
        super().abrir()
        fuerza = self.ataque + self.nivel
        print(f"Dentro habia un feroz monstruo cuya fuerza es {fuerza}")
        return fuerza
    

    def imprimir_ataques_posibles(self):
        print("Los ataques posibles de la puerta son:")
        print(self.ataque_posible)


    def __str__(self):
        return f"La puerta monstruo nivel {self.nivel} tiene {self.ataque} puntos de ataque."