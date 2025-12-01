import random
class CascadaDeMonedas:

    def __init__(self, alto:int, ancho:int):
        self.maquina = self._crear_maquina(alto,ancho)
        self.alto = alto
        self.ancho = ancho


    def _crear_maquina(self, alto: int, ancho:int):
        maquina = []
        for y in range(alto):
            maquina.append([])
            for x in range(ancho):
                maquina[y].append(random.randint(0,5))

        return maquina
    

    def __str__(self):
        for y in range(self.alto):
            for x in range(self.ancho):
                print(self.maquina[y][x], end = " ")
            print()