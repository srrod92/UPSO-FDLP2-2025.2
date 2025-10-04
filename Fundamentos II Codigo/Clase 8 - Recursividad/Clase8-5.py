def fibonacci(posicion:int)-> int:
    print("Se llama a fibonacci")
    if posicion < 0:
        posicion = abs(posicion)

    if posicion == 0:
        return 0
    
    if posicion == 1:
        return 1
    
   
    return fibonacci(posicion-1) + fibonacci(posicion-2)



def torre_hanoi(cantidad_discos:int)-> int:
    if cantidad_discos == 1:
        return 1
    
    return 2* torre_hanoi(cantidad_discos-1) + 1



print(torre_hanoi(4))