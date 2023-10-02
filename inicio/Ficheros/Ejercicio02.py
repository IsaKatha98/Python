f= open ('inicio\\Ficheros\\Texto.txt', 'w')


texto=input("Escriba lo que quiera: ")

while texto!="fin":

    
    f.write(texto)

    texto=input()

f.close()

