from Clases import *
from collections import deque

personajes_jugador: deque = deque()
personajes_enemigo: deque = deque()

personajes_jugador.append(Guerrero("Ramon", 100, 60, 40))
personajes_jugador.append(Mago("Frognoer", 90, 50, 25))
personajes_jugador.append(Arquero("El Chino de los juegos olimpicos", 80, 30, 30))

personajes_enemigo.append(Guerrero("Mandinga", 90, 50, 25))
personajes_enemigo.append(Mago("Mantequita", 30, 50, 30))
personajes_enemigo.append(Arquero("Impresora", 70, 50, 34))


while len(personajes_enemigo) != 0 and len(personajes_jugador) != 0:
    jugador:Personaje = personajes_jugador.popleft()
    enemigo:Personaje = personajes_enemigo.popleft()

    if not jugador.esta_vivo():
        if len(personajes_jugador) != 0:
            jugador = personajes_jugador.popleft()
        else:
            continue

    jugador.atacar(enemigo)
    

    personajes_jugador.append(jugador)

    if not enemigo.esta_vivo():
        if len(personajes_enemigo):
            enemigo = personajes_enemigo.popleft()
        else:
            continue
    
    enemigo.atacar(personajes_jugador[0])
    personajes_enemigo.append(enemigo)



print("El combate termino El ganador es:")

if len(personajes_enemigo) > len(personajes_jugador):
    print("Enemigo")
else:
    print("Jugador")

    




