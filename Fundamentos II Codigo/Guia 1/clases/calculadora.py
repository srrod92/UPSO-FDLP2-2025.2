class Calculadora:

    energia:int


    def __init__(self, energia_inicial:int = 100):
        self.energia = energia_inicial
        pass


    def sumar(self,num1:float, num2:float) -> float:
        if self.__tiene_energia_suficiente():
            return num1+num2
        else:
            print("No hay energia suficiente.")
            return None
    

    def resta(self, minuendo:float, sustraendo:float)-> float:
        if self.__tiene_energia_suficiente():
            return minuendo-sustraendo
        
        print("No hay energia suficiente.")
        return None
    

    def multiplicar(self, num1:float, num2:float)-> float:
        if self.__tiene_energia_suficiente():
            return num1*num2

        print("No hay energia suficiente.")
        return None
            
    

    def div(self, dividendo:float, divisor:float) -> float:
        if self.__tiene_energia_suficiente():
                
            if divisor != 0:
                return dividendo/divisor
            else:
                print("Error: divisor es 0.")
                return None            

        print("No hay energia suficiente.")
        return None
        

    def __tiene_energia_suficiente(self) -> bool:
        if self.energia>=10:
            self.energia-=10
            return True
        else:
            return False


    def get_energia_disponible(self):
        print(f"Energía disponible: {self.energia}")