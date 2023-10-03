class Empleado:

    def __init__(self, nombre):
        self.nombre=nombre

    def __str__(self):
        res= "Empleado "+self.nombre

        return res