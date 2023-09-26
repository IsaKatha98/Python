class Persona:

    def __init__(self):
        self.nombre=""
        self.edad=0
    
    def __innit__ (self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    
    def __str__(self):
        cadena="Nombre",self.nombre,"\n"
        cadena+= "Edad:", str(self.edad)

        return cadena

    def __eq__(self, persona2):
        res=False

        if self.nombre==persona2.nombre:
            res=True


        return res
    
    def __lt__ (self, persona2):
        res= False

        if self.edad

        return res