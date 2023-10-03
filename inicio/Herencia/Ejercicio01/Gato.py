from Animal import *
class Gato(Animal):

    def __init__(self, nombre, numPatas) -> None:
        super().__init__(nombre, numPatas)

    def habla (self):

        res="Miau"

        return res
    
    def __str__(self) -> str:
        res="Soy un gato.\n"
        res+= str(super().__str__)

        return res
    