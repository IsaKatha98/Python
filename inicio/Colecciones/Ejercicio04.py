print("introduzca diez números:")

lista =[]

for i in range (0,10):

    lista.append(int(input()))

print (lista)

print("Máximo:", max(lista))
print("Mínimo:", min(lista))