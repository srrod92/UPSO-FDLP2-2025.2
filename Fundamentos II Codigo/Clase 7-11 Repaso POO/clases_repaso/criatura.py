class Criatura:

    def __init__(self, nombre: str, vida:int, ataque:int, defensa:int):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa


    def mostrar_info(self):
        print(f"La criatura {self.nombre} tiene {self.vida} puntos de vida, {self.ataque} puntos de daño y {self.defensa} puntos de armadura.")

    
    def recibir_dano(self, dano:int):
        dano_real = dano - self.defensa
        
        if dano_real>0:
            print(f"{self.nombre} recibe {dano_real} daño")
            self.vida -= dano_real
    

    