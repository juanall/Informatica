#Ejercicio 8
#Realizá un programa que declare tres listas lista1, lista2 y lista3, 
#donde las dos primeras listas deben tener cinco enteros cada una, ingresados por teclado y
#asigne para cada elemento de la lista3 la suma de los elementos de la lista1 y la lista2
#(es decir, el primer elemento de la lista3 tiene que ser la suma del primer elemento de la lista1 y el primero de la lista2)

lista1 = []
lista2 = []
lista3 = []
for indice in range(1,6):
	lista1.append(int(input("Introduce el elemento %d :" % indice)))
for indice in range(1,6):
	lista2.append(int(input("Introduce el elemento %d :" % indice)))

for indice in range(0,5):
	lista3.append(lista1[indice] + lista2[indice])

print("La suma de las listas es:")
for numero in lista3:
	print(numero," ",end="")