from Animal import *

class Perro:

     def __init__(self, nombre, numPatas) -> None:
        super().__init__(nombre, numPatas)

    def habla (self):

        res="Guau"

        return res
    
    def __str__(self) -> str:
        res="Soy un perro.\n"
        res+= super().__str__

        return res
    