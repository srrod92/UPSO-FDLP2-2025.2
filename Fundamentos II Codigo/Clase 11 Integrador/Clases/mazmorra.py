import random
from .vacio import Vacio
from .mc import Mc
from .pinche import Pinche
from .puerta import Puerta
from .llave import Llave
class Mazmorra:
    def __init__(self, alto:int, ancho:int ):
        self.alto = alto
        self.ancho=ancho
        self.mazmorra = []
        self.__construir_mazmorra()
        
    def __calcular_nueva_posicion(self, elemento, direccion:str):
        nueva_pos_fila = None
        nueva_pos_columna = None
        match direccion:
                    case "w":
                        if elemento.pos_fila > 0:
                            nueva_pos_fila = elemento.pos_fila - 1
                            nueva_pos_columna = elemento.pos_columna
                    case "a":
                        if elemento.pos_columna > 0:
                            nueva_pos_columna = elemento.pos_columna - 1
                            nueva_pos_fila = elemento.pos_fila
                    case "s":
                        if elemento.pos_fila < self.alto-1:
                            nueva_pos_fila = elemento.pos_fila + 1
                            nueva_pos_columna = elemento.pos_columna
                    case "d":
                        if elemento.pos_columna < self.ancho-1:
                            nueva_pos_columna = elemento.pos_columna + 1
                            nueva_pos_fila = elemento.pos_fila

        if nueva_pos_columna == None and nueva_pos_fila == None:
            nueva_pos_fila = elemento.pos_fila
            nueva_pos_columna = elemento.pos_columna

        return nueva_pos_fila, nueva_pos_columna


        
    def mover_mc(self, direccion:str) -> bool:
        direccion = direccion.lower()

        if self.mc.get_position() == self.puerta.get_position():
            self.mazmorra[self.mc.pos_fila][self.mc.pos_columna] = self.puerta
        else:
            self.mazmorra[self.mc.pos_fila][self.mc.pos_columna] = Vacio()

            
        match direccion:
            case "w":
                if self.mc.pos_fila > 0:
                    self.mc.pos_fila -= 1
            case "a":
                if self.mc.pos_columna > 0:
                    self.mc.pos_columna -= 1
            case "s":
                if self.mc.pos_fila < self.alto-1:
                    self.mc.pos_fila += 1
            case "d":
                if self.mc.pos_columna < self.ancho-1:
                    self.mc.pos_columna += 1
        colision = self.mazmorra[self.mc.pos_fila][self.mc.pos_columna]
        self.mazmorra[self.mc.pos_fila][self.mc.pos_columna] = self.mc
        terminar = self.mc.colision(colision)

        if terminar:
            return True

       

        


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
                    self.mazmorra[alto_aleatorio][ancho_aleatorio] = Pinche()
                    break

        for personaje in range(mc_restante): 

            while True:
                alto_aleatorio = random.randint(0,self.alto-1)
                ancho_aleatorio = random.randint(0, self.ancho-1)

                if isinstance(self.mazmorra[alto_aleatorio][ancho_aleatorio], Vacio):
                    self.mazmorra[alto_aleatorio][ancho_aleatorio] = Mc(alto_aleatorio, ancho_aleatorio)
                    self.mc = self.mazmorra[alto_aleatorio][ancho_aleatorio]
                    
                    break

        for puerta in range(puerta_restante):

            while True:
                alto_aleatorio = random.randint(0,self.alto-1)
                ancho_aleatorio = random.randint(0, self.ancho-1)

                if isinstance(self.mazmorra[alto_aleatorio][ancho_aleatorio], Vacio):
                    self.mazmorra[alto_aleatorio][ancho_aleatorio] = Puerta(alto_aleatorio, ancho_aleatorio)
                    self.puerta = self.mazmorra[alto_aleatorio][ancho_aleatorio]
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
                    self.mazmorra[alto_aleatorio][ancho_aleatorio] = Llave()
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
🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲
🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲 🔲 
🔲 🔲 🔲 🔲 👹 🔲 🔲 🔲 🔲 🔲 
🔲 🔲 🔲 🔲 🔲 🔲 👹 🔲 👹 🔲 
🔲 🔲 🔲 🔲 🔲 🔲 🔲 😝 🔲 🔲 
👹 🔲 🔲 🔲 🔲 🔑 🔲 🔲 🔲 🔲 


    """