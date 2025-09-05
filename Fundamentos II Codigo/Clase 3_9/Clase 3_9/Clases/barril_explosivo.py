from Interfaces.idanable import IDanable

class BarrilExplosivo(IDanable):
    vida:int = 10
    fuerza:int
    defensa:int


    def __init__(self, fuerza:int=50, defensa:int=0):
        self.fuerza = fuerza
        self.defensa = defensa
    
    def recibir_dano(self, dano_a_recibir:int):
        if self.vida>= 0:
            resultado=max(0, dano_a_recibir-self.defensa)
            self.vida -= resultado
            print(f"El barril recibe {resultado} de daño")
            if self.vida < 0 :
                print(f"El barril Explota")

    def get_fuerza(self) -> int:
        return self.fuerza
    
    def set_fuerza(self, nueva_fuerza:int):
        #la clase determina COMO es valido setear la fuerza
        if nueva_fuerza > self.fuerza:
            self.fuerza = nueva_fuerza