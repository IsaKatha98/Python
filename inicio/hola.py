print ("""Hola mundo,
       qué tal?""")

a= 5
b=4.5
c="hola"

#res= input ("Introduzca un número: ")
#print(res)

#no hay double en python
a1= float (input ("Introduzca un número: "))
a2= float (input ("Introduzca un número: "))
suma=a1+a2
print(suma)

num= int (input("Número: "))

if num%2==0:
    print ("Es par")

else: 
    print ("No es par")

if num>0 and num<=100:
    print ("El número está entre 1 y 100")

if num<0 or num>=100:
    print ("El número no está en el rango.")

if not num%2==0:
    print ("El número es impar.")


num1= int (input("Número: "))

var= "par" if (num1%2==0) else "impar"

print (var)


num2= int (input("Número: "))
i=1
suma=0
while i<=num:
    print (i)
    suma+=i
    i+=1

print (suma)

for contador in range(1, 101):
    print(contador)