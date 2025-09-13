def mover_personaje(tecla:str, posicion_actual:int, mazmorra:list):
    mazmorra[posicion_actual] = "*"
    match tecla:
        case "a":            
            posicion_actual -=1

        case "d":
            posicion_actual +=1
            

    mazmorra[posicion_actual] = "@"
    return posicion_actual, mazmorra


    



#########################
mazmorra:list = ["*","*","*","*","@","*","*","","*","*"]
posicion_personaje = 4

while True:
    print(mazmorra)
    entrada = input("a. Izquierda   d. Derecha")
    posicion_personaje, mazmorra = mover_personaje(entrada, posicion_personaje,mazmorra)








