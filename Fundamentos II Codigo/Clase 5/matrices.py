matriz:list = []


lista1:list = [1,2,3]
lista2:list = [4,5,6,999]
lista3:list = [7,8,9]


matriz.append(lista1)
matriz.append(lista2)
matriz.append(lista3)




"""
matriz[0][0] matriz[0][1] matriz[0][2]
matriz[1][0] matriz[1][1] matriz[1][2]
matriz[2][0] matriz[2][1] matriz[2][2]
"""

for y in range(len(matriz)): 
    for x in range(len(matriz[y])): 
        print(matriz[y][x], end="")
    print()



#matriz[y][x] 






