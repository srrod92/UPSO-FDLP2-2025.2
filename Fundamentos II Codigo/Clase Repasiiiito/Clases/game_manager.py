#Esto esta incompleto

from Clases import *
from collections import deque

class GameManager():

    lista_jugador: deque
    lista_enemigo: deque
    def __init__(self):
        self.lista_jugador = deque()
        self.lista_enemigo = deque()

    
    def pasar_al_final_de_la_cola(self, lista:deque):
        personaje = lista.popleft()
        lista.append(personaje)


    def turno(self):
        self.turno_de_jugador()

        if len(self.lista_enemigo) != 0:
            self.turno_de_enemigo()


    def turno_de_jugador(self):
        print(f"Es el turno de {self.lista_jugador[0]._nombre}")

        print("Que desea hacer?")

        

        
