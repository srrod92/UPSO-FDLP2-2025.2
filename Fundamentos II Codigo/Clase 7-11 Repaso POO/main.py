##MAIN - PUNTO DE ENTRADA AL PROYECTO

import os
from clases.botella import Botella
from clases.lata import Lata
from clases_repaso.criatura import Criatura
from clases_repaso.mago import Mago


os.system("cls")


gandalf = Mago("Gandalf", 100, 30,10,50)
saruman = Mago("Saruman", 90, 50, 5, 40)


gandalf.atacar(saruman)






