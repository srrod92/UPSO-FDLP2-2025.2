from Interfaces.idanable import IDanable

class Enemigo(IDanable):
    vida:int
    fuerza:int
    defensa:int

    def __init__(self, vida:int=60, fuerza:int=10, defensa:int=5):
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa
    
    def recibir_dano(self, dano_a_recibir:int):
        resultado=max(1, dano_a_recibir-self.defensa)
        self.vida -= resultado
        print(f"El enemigo recibe {resultado} de daño")