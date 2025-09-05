from Clases.jugador import Jugador
from Clases.barril_explosivo import BarrilExplosivo
from Clases.enemigo import Enemigo
from Interfaces.idanable import IDanable

def main():
    ramon: Jugador = Jugador(100,10,30)
    bunk: BarrilExplosivo = BarrilExplosivo()
    malito: Enemigo = Enemigo()
    aplicar_dano(bunk,20)
    if bunk.estado == "explotó":
        print("Le pegaste muy fuerte a bunk, bunk explota, bunk hace aca todo")
        aplicar_dano(malito,bunk.get_fuerza())
        aplicar_dano(ramon,bunk.fuerza)

def aplicar_dano(objetivo:IDanable, cantidad:int):
    objetivo.recibir_dano(cantidad)

if __name__ == "__main__":
    main()