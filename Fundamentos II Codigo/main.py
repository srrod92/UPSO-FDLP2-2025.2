from clases.auto import Auto #Importo la clase desde el path del script -> clases.auto

def main():

    mi_auto:Auto = Auto("Chevrolet", "Gris", "2025") #Creo una instancia de Auto.

    mi_auto.encender() #Le pido a la instancia que llame al metodo encender.


if __name__ == "__main__":
    main()

