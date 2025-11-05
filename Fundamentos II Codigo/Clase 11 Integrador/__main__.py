import os
from Clases import *

mazmorrilla = Mazmorra(10,10)



while True:
    os.system("cls")
    mazmorrilla.imprimir_mazmorra()
    direccion = input("W. Arriba.  A. Izquierda.  S. Abajo.  D. Derecha.\n")
    terminar = mazmorrilla.mover_mc(direccion)

    if terminar:
        break

os.system("cls")
print("El juego termino.")
    
    



    
    
