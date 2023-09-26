print("introduzca ocho números:")

lista =[]

for i in range (0,8):

    lista.append(int(input()))

print (lista)

for num in lista:
    if num%2==0:
        print(num,"-> par")

    else:
        print(num,"-> impar")      
