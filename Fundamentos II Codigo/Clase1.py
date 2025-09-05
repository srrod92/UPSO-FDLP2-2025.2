def saludar(nombre:str) -> None:  ##Define la funcion
    print(f"Bienvenido {nombre}.\n")  ##Esta es la instrucción que ejecutará al llamarse.


def crear_lista() -> list: #Definimos la función
    lista:list = list()  #Declaramos y creamos una lista vacía.

    for i in range(5):    # creamos un bucle que se repetirá 5 veces.
        lista.append(int(input(f"Ingrese el {i+1}° número.\n")))
    
    return lista  #Retornamos la lista completa.


def imprimir_lista_por_indice(lista:list) ->None: 
    print("Se imprimira la lista. \n")
    for i in range(len(lista)):
        print(lista[i])


def imprimir_lista_por_referencia(lista:list) -> None:
    print("Se imprimira la lista. \n")
    for numero in lista:
        print(numero)


def lista_ordenada(lista:list) -> bool: #Creamos la función que devuelve un bool.
    ordenada:bool = True    #Variable booleana que indica si la lista esta ordenada.
    for i in range(len(lista)-1):  #Recorremos la lista hasta el anteultimo elemento
        if lista[i] > lista[i+1]:  #Comparamos el elemento actual con su elemento siguiente.
            ordenada = False    
            break  #Si el elemento actual es mayor al siguiente sabemos que la lista esta desordenada.

    return ordenada #Retornamos el valor que tenga ordenada.


def insertar_numero(lista:list, num:int) -> list:  #Declaramos la función. Devuelve una lista.
    if lista_ordenada(lista):  #Utilizamos la función que nos dice si la lista esta ordenada.
        insertado:bool = False #Declaramos una bandera para determinar si ya se inserto el numero.
        for i in range(len(lista)): #Si esta ordenada la recorremos utilizando el indice.
            if lista[i] > num:  #Buscamos el numero primer numero que sea mayor al numero que debemos insertar
                lista.insert(i,num)  #Insertamos. 
                insertado =True #Activamos la bandera de insertado
                break #Rompemos el bucle.
        if not insertado:# Si el numero no fue insertado lo agregamos al final.
            lista.append(num)
    else: #Si la lista esta desordenada avisamos.
        print("La lista esta desordenada.")
    return lista #Retornamos la lista como este.



def ordenar_lista(lista:list) -> list:
    while not lista_ordenada(lista):  # Bucleamos hasta que la lista este ordenada.
        for i in range(len(lista)-1): #recorremos la lista utilizando los indices.
            if lista[i] > lista[i+1]:  #Si el numero actual es mayor que el siguiente los intercambio.
                aux:int = lista[i]
                lista[i]= lista[i+1]
                lista[i+1]= aux

                ##Este proceso se repite hasta que la lista este ordenada. 
    
    return lista   


##########################################


print("Hola Usuario, bienvenido")

nombre:str = input("Por favor, ingrese su nombre.")

saludar(nombre)

entrada:str = input("Desea utilizar el super programa ordenador de numeros? Si/No \n")
while entrada =="Si":
    lista:list = crear_lista()
    imprimir_lista_por_indice(lista)
    lista = ordenar_lista(lista)
    imprimir_lista_por_referencia(lista)

    numero_insertar:int = int(input("Ingrese un número para insertar ordenado en la lista.\n"))    
    lista = insertar_numero(lista, numero_insertar)
    imprimir_lista_por_indice(lista)

    entrada = input("Desea volver a utilizar el super programa ordenador de numeros? Si/No \n")

else:
    print("Adios.")