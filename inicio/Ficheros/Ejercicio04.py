f= open ('inicio\\Ficheros\\enteros.txt', 'rt')

num= []
for linea in f.readlines():
   
   if linea!="":
        num+= linea

f.close()

print(num)