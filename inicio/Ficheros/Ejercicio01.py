f= open ('inicio\\Ficheros\\Alumnos.txt', 'rt')

cont=0
nombre=""
sumaEdad=0
sumaAlt=0
lista=[]

for linea in f.readlines():
   print(linea, end='')
   lista+= linea.split() 
    
   nombre+=str(lista[0])
   sumaEdad+=int(lista[1])
   sumaAlt+= float(lista[2])
    
   cont+=1

   lista=[]



f.close()

mediaEdad= sumaEdad/cont
mediaAlt=sumaAlt/cont

print("Los nombres son:", nombre)
print("La media de la edad es:", mediaEdad)
print("La media de la altura es:", mediaAlt)