class Arma():

    dano:int = 0
    peso:float = 0 


    def atacar(self):
        print("El Arma Ataca de forma de generica.")

    
    def get_dano(self) -> int:
        return self.dano
    

    def get_peso(self) -> float:
        return self.peso