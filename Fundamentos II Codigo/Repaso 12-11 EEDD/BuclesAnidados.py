##Crear una rutina que imprima todos los números enteros del 1 al 5 una X cantidad de veces.

def ejercicio1(veces:int):
    print(f"Se contara del 1 al 5, {veces} veces")
    for iteracion in range(veces):

        for entero in range(1,6):
            print(f"iteracion N°: {iteracion+1}: {entero}")


 
def ejercicio2(): ## Yanina
    for tabla in range(11): 
        for entero in range(0,11):
            print(f"tabla Nro. {tabla}: {tabla} X {entero} = {tabla*entero}")
 

def hacer_tablas_del_0_al_10 (): # Lucas
    for i in range(0,11):
        for j in range(0,11):
            print(f"{i} por {j} es igual a {i*j}")


def multiplicar_por_todas_las_tablas(veces:int):
    for iteracion in range(veces):
        print(f"\n🧌Tabla del {iteracion}:\n")
        for entero in range(0,11):
            valor = iteracion * entero
            print(f"{iteracion} * {entero} = {valor}")
        iteracion+1


def ImprimirCoordenadas(alto:int, ancho:int):
    for y in range(alto):
        for x in range (ancho):
            print(f"({x},{y})", end= " ")
        print()





ImprimirCoordenadas(3,3)





