from Interfaces.idanable import IDanable

class Jugador(IDanable):
    
    vida:int
    fuerza:int
    defensa:int

    def __init__(self, vida:int, fuerza:int, defensa:int):
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa
    
    def recibir_dano(self, dano_a_recibir:int):
        resultado=max(0, dano_a_recibir-self.defensa)
        self.vida -= resultado
        print(f"El jugador recibe {resultado} de daño")

    


    
