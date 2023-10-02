

nombre=input("Introduzca su nombre: ")
edad= input ("Introduzca su edad: ")

#Si el archivo existe, añadimos
if f.isfile==True:
    
    f=open('inicio\\Ficheros\\datos.txt', 'a')

else:

    f=open ('inicio\\Ficheros\\datos.txt', 'w')