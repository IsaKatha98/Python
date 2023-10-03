from Animal import*

class Perro(Animal):

     def __init__(self, nombre, numPatas) -> None:
        super().__init__(nombre, numPatas)

     def habla (self):

        res="Guau"

        return res
    
     def __str__(self) -> str:
        res="Soy un perro.\n"
        res+= str(super().__str__)

        return res
    