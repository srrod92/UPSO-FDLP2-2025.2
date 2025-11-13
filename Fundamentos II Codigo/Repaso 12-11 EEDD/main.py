"""
Listas dinamicas DONE

pilas -> list   -> Se agarra el ultimo elemento de la lista. .pop
colas -> queue  -> Se agarra el primer elemento de la lista.  .pop(0)
queue

deque -> pila de doble final

Implementar las propias.


Matrices -> listas que contienen listas
"""
import random
#Vamos a crear un metodo que cree una lista por largo que yo le agregue
def CrearListaDeEnteros(largo:int) -> list:
    lista = []
    for i in range(largo):
        #Esta es una forma
        #lista.append(random.randint(0,9))

        #Otra forma más clara y prolija es
        numero = random.randint(0,9) #números aleatorios entre 0 y 9
        lista.append(numero)
    
    return lista

def main():

    lista = CrearListaDeEnteros(23)
    print(lista)




if __name__ == "__main__":
    main()





