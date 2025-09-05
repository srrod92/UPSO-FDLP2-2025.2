from Clases import *
from Interfaces import *


def main():

    hacha:Hacha = Hacha()
    maria_elena:Espada = Espada()
    arco:Arco = Arco()
    arma_generica: Arma = Arma()

    kratos: Personaje = Personaje(hacha)
    wally: Personaje = Personaje(maria_elena)
    personaje_generico: Personaje = Personaje(arma_generica)
    tonto_de_legolas:Personaje = Personaje(arco)

    kratos.atacar()
    wally.atacar()
    tonto_de_legolas.atacar()
    personaje_generico.atacar()




    




if __name__ == "__main__":
    main()