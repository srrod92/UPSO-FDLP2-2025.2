import random
from Clases import Vacio, Mc
class Mazmorra:
    def __init__(self, alto:int, ancho:int ):
        self.alto = alto
        self.ancho=ancho
        self.mazmorra = []
        self.__construir_mazmorra()

        


    def __construir_mazmorra(self):
        pinches_restante = 4
        mc_restante = 1
        puerta_restante = 1
        troll_restante = 4
        llave_restante = 1        

        for fila in range(self.alto):
            nueva_lista = []
            for columna in range(self.ancho):
                nueva_lista.append(Vacio())
            self.mazmorra.append(nueva_lista)

        for pinche in range(pinches_restante):    ## [0,1,2,3]        

            while True:
                alto_aleatorio = random.randint(0,self.alto-1)
                ancho_aleatorio = random.randint(0,self.ancho-1)

                if isinstance(self.mazmorra[alto_aleatorio][ancho_aleatorio], Vacio):
                    self.mazmorra[alto_aleatorio][ancho_aleatorio] = "🔪"
                    break

        for personaje in range(mc_restante): 

            while True:
                alto_aleatorio = random.randint(0,self.alto-1)
                ancho_aleatorio = random.randint(0, self.ancho-1)

                if isinstance(self.mazmorra[alto_aleatorio][ancho_aleatorio], Vacio):
                    self.mazmorra[alto_aleatorio][ancho_aleatorio] = Mc()
                    break

        for puerta in range(puerta_restante):

            while True:
                alto_aleatorio = random.randint(0,self.alto-1)
                ancho_aleatorio = random.randint(0, self.ancho-1)

                if isinstance(self.mazmorra[alto_aleatorio][ancho_aleatorio], Vacio):
                    self.mazmorra[alto_aleatorio][ancho_aleatorio] = "🚪"
                    break

        for troll in range(troll_restante):

            while True:
                alto_aleatorio = random.randint(0,self.alto-1)
                ancho_aleatorio = random.randint(0, self.ancho-1)

                if isinstance(self.mazmorra[alto_aleatorio][ancho_aleatorio], Vacio):
                    self.mazmorra[alto_aleatorio][ancho_aleatorio] = "👹"
                    break

        for llave in range(llave_restante):

            while True:
                alto_aleatorio = random.randint(0,self.alto-1)
                ancho_aleatorio = random.randint(0, self.ancho-1)

                if isinstance(self.mazmorra[alto_aleatorio][ancho_aleatorio], Vacio):
                    self.mazmorra[alto_aleatorio][ancho_aleatorio] = "🔑"
                    break
                
        


    def imprimir_mazmorra(self):
        for fila in self.mazmorra:
            for casilla in fila:
                print(casilla, end = " ")
            print()

    def imprimir_por_indice(self):

        for fila in range(self.alto):
            for columna in range(self.ancho):
                print(self.mazmorra[fila][columna], end = " ")
            print()

            
    """
          [6,7]       
    [7,6] [7,7] [7,8]
          [8,7]

🔲 🔲 🔲 🔑 🔲 🔲 🔲 🔲 🔲 🔲 
🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲 
🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲  🔲 
🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲 
🔲 🔲 🔲 🔲 👹 🔲 🔲 🔲 🔲 🔪 
🔲 🔲 🔲 🔲 🔲 🔲 👹 🔲 👹 🔲 
🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲 
👹 🔲 🔲 🔪 🔲 🔑 🔲 😝 🔲 🔲 


    """