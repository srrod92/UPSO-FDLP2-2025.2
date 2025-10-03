import math
def suma_recursiva(lista_de_tornillos: list) -> int:
    if len(lista_de_tornillos) == 1: #Este es el caso base.
        return lista_de_tornillos[0]
    
    return lista_de_tornillos[0] + suma_recursiva(lista_de_tornillos[1:])


def factorial(numero:int) -> int:
    if numero == 1 or numero == 0:
        return 1
    
    return numero * factorial(numero-1)


def primo_recursivo(n:int)-> bool: ##Funcion recursiva que revisa si un numero es primo o no
    if n<1:
        print("Numero invalido.")
        return
    if n == 1:
        return False
    
    valor_actual = int(math.sqrt(n))
    return _caso_recursivo(n,valor_actual)


def _caso_recursivo(valor_original, valor_actual)->bool: ## Funcion de apoyo a la funcion primo_recursivo.
    if valor_actual == 1:
        return True
    
    if valor_original % valor_actual == 0:
        return False
    
    return _caso_recursivo(valor_original, valor_actual-1)

###################################################################

primos_encontrados = 0
for i in range(1,5000):
    if primo_recursivo(i):
        primos_encontrados +=1

print(f"Se encontraron {primos_encontrados} numeros primos entre el 1 y el 5000")


"""

#prueba de suma_recursiva.
lista:list = [15,45,80,10, 50] 


print(suma_recursiva(lista))

acumulado = 0
for numero in lista:
    acumulado += numero


print(f"El valor de la suma iterativa es {acumulado}")

"""




