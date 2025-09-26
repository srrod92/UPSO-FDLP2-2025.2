from Clases import *

head = Nodo("Falso Caballero", 1)


lista = ListaEnlazada()

lista.setear_head(head)

lista.insertar_nodo(Nodo("Gollum", 10))

lista.insertar_nodo(Nodo("Javier", 9000))
lista.insertar_nodo(Nodo("Ian", 9000))
lista.insertar_nodo(Nodo("Luz", 9000))
lista.insertar_nodo(Nodo("Lucas", 9000))
lista.insertar_nodo(Nodo("Sauron", 9999))
lista.insertar_nodo(Nodo("Ramon", 10000))




lista.eliminar_nodo(0)

print(lista.buscar_en_indice(0))





