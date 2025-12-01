from Clases import PuertaMostruo, PuertaTesoro, Munchkin

tesoro = PuertaTesoro(1,5)

monstruo = PuertaMostruo(2)

ramon = Munchkin(1,7)

ramon.abrir_puerta(tesoro)
ramon.abrir_puerta(monstruo)