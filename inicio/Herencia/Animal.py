class Animal:

    def __init__(self, nombre, numPatas) -> None:
        
        self.nombre= nombre
        self.numPatas=numPatas

    def habla (self):
        
        self.habla=""
    
    def __str__(self) -> str:
        
        res="Me llamo "+self.nombre+",\n"
        res+="tengo "+self.numPatas+", \n"
        res+="y sueno así: "+self.habla

        return res
