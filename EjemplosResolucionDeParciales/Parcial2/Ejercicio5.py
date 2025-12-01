from Clases import PuertaMostruo, Puerta, PuertaTesoro, Munchkin
import random
import os

def crear_matriz():
    matriz = []

    for i in range(5):
        array_puerta=[]
        rng = random.randint(0,1)

        if rng == 0:
            array_puerta.append(PuertaMostruo(random.randint(1,3)))
            array_puerta.append(4)
        else:
            array_puerta.append(PuertaTesoro(random.randint(1,3), random.randint(1,5)))
            array_puerta.append(4)

        matriz.append(array_puerta)

    return matriz


def obtener_puerta(matriz:list):
    
    while True:
        if len(matriz) == 0:
            return None
        indice = random.randint(0,len(matriz)-1)

        puerta = matriz[indice]

        if puerta[1] >0:
            puerta[1] -= 1
            return puerta[0]
        else:
            matriz.pop(indice)
           



def imprimir_stats(munchkin: Munchkin):
    print("-"*50)
    print(f"--- Nivel: {munchkin.nivel} --- Fuerza: {munchkin.ataque+munchkin.nivel} ---")




###########################

ramon = Munchkin(1,1)

matriz = crear_matriz()

while ramon.nivel < 10:

    if len(matriz)==0:
        print("No hay mas puertas!")
        break

    imprimir_stats(ramon)
    
    print("El Munchkin se enfrenta a una puerta. Que desea hacer?")
    print("1. Abrirla")
    print("2. Esquivarla")
    respuesta = input()

    if respuesta == "1":
        puerta = obtener_puerta(matriz)        
        ramon.abrir_puerta(puerta)
    
    elif respuesta =="2":
        print("Ignoras la puerta.")

    input("Ingresa una tecla para continuar.")
    os.system("cls")


if ramon.nivel == 10:
    print("Felicidades, pasaste el Munchkin")

else:
    print("Te quedaste sin puertas Ramon.")

