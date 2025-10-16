from Clases import *

arbolito = ArbolBinario()
# 6, 10, 12, 8, 20, 15, 3, 1, 0
arbolito.insertar(6)
arbolito.insertar(10)
arbolito.insertar(12)
arbolito.insertar(8)
arbolito.insertar(20)
arbolito.insertar(15)
arbolito.insertar(3)
arbolito.insertar(1)
arbolito.insertar(0)

print("Pre orden")
arbolito.imprimir_preorden(arbolito.raiz)

print("in orden")
arbolito.imprimir_inorden(arbolito.raiz)

print("pos orden")
arbolito.imprimir_posorden(arbolito.raiz)
