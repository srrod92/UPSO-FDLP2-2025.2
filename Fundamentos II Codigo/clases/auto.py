class Auto:

    __marca:str  #Los __ indica que es un atributo privado
    __color:str  #y que no debe ser accedido por otra clase.
    __modelo:str

    def __init__(self,marca:str,color:str,modelo:str):
        self.marca = marca
        self.color = color
        self.modelo = modelo
    
    def encender(self):
        print(f"Se enciendel el {self.__marca} {self.__modelo} color {self.__color}. ")


    def __encender_burro_de_arranque(self):
        #Los __ indica que este metodo no debe ser utiliza por fuera de la clase
        print("**ruido de burro de arranque**")


