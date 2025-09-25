class Nodo:
    nombre: str
    nivel: int
   
 

    def __init__(self, nombre, nivel, nodo_siguiente_ = None):
        self.nombre = nombre
        self.nivel = nivel
        self.oro = nivel * 100
        self.nodo_siguiente = nodo_siguiente_
 

    def __str__(self):
        return self.nombre



  