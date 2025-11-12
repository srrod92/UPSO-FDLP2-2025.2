from .botella import Botella
class Lata(Botella):

    def __init__(self,capacidad:int):
            super().__init__(capacidad, "Aluminio")
            self.cantidad_liquido = capacidad
            self.abierto = False

    
    def abrir(self):
          self.abierto=True
          print("psssc.")

    
    def mostrar_descripcion(self):
        print(f"Soy una rica lata de {self.material} y tengo {self.capacidad}ml de capacidad.")




    
        
