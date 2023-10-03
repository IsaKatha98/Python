class Animal:

    def __init__(self, nombre, numPatas) -> None:
        
        self.nombre= nombre
        self.numPatas=numPatas

    def habla (self):
        
        res=""

        return res
        
    
    def __str__(self) -> str:
        
        res="Me llamo "+self.nombre+",\n"
        res+="tengo "+str(self.numPatas)+", \n"
        res+="y sueno así: "+str(self.habla)

        return res
