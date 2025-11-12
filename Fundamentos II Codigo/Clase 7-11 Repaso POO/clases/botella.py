#modulo botella.py
class Botella:
    
    def __init__(self, capacidad_, material_): ##metodo constructor.
        self.capacidad = capacidad_
        self.material = material_
        self.cantidad_liquido = 0
        

    def mostrar_descripcion(self):
        print(f"Soy una botella de {self.material} y tengo {self.capacidad}ml de capacidad.")

    def llenar(self, liquido_a_agregar):
        self.cantidad_liquido += liquido_a_agregar
        print(f"La botella ahora tiene {self.cantidad_liquido} liquido dentro.")


