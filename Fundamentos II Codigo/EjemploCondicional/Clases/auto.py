from Clases.vehiculo import Vehiculo
class Auto(Vehiculo):
    marca:str
    color:str
    modelo:str
    encendido:bool
    baul:list 

    def __init__(self, marca_:str, color_:str, modelo_:str): #Metodo constructor
        super().__init__(4,5)
        self.marca = marca_
        self.color = color_
        self.modelo = modelo_
        self.encendido = False
        self.baul = list()


    def enceder(self):
        self.encendido = True
        print(f"Se encendio el auto {self.marca} {self.color}")


    def apagar(self):
        self.encendido = False
        print(f"Se apago el auto {self.marca} {self.color}")


    def guardar_en_baul(self, algo:str):
        self.baul.append(algo)
        self.ver_baul()


    def ver_baul(self):
        print(self.baul)

    def get_puertas(self):
        print(self.puertas)
