#crear lista
def crear_lista() -> list:
    lista:list=[]
    for i in range(5):
        entrada:str = input(f"Ingrese elemento {i} de la lista: ")
        lista.append(int(entrada))
    return lista


#imprimir lista
def imprimir_lista(lista:list):
    print("Imprimiendo lista:")
    for i in range(len(lista)):
        print(lista[i])

#principal
def main():
    lista:list = crear_lista()
    imprimir_lista(lista)

#ejecutar todo
main()