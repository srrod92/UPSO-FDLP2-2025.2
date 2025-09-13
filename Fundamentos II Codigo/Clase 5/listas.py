""" Este metodo pide al usuario 5 numeros y los mete en una lista. Luego retorna la lista."""
def crear_lista() -> list:
    lista:list = []

    for _ in range(5):
        entrada = int(input("Ingrese un numero entero."))
        lista.append(entrada)

    return lista




def imprimir_lista(lista:list) -> None:
    
    for numero in lista:
        print(numero, end="\n ")


#######################################



lista = crear_lista()

imprimir_lista(lista)
    













