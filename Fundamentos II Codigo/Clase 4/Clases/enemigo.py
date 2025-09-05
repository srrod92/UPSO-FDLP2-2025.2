from Interfaces.idanable import IDanable

class Enemigo():
    
    vida:int = 100
    escudo:int = 30

    def recibir_dano(self, dano_a_recibir:int):
        resultado: int = max(0, dano_a_recibir - (self.escudo/2))
        self.vida -= resultado
        print(f"El enemigo recibirio {resultado} puntos de daño")
