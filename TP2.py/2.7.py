#Ejercicio 7
#Creá un programa que declare una lista y la vaya llenando de números leídos por teclado hasta 
#que se introduzca un número negativo. Una vez hecho esto se deben imprimir los elementos de la lista.

lista = []
numero = int(input("Introduce un número en la lista:"))
while numero>=0:
	lista.append(numero)
	numero = int(input("Introduce un número en la lista:"))

for numero in lista:
	print(numero," ",end="")

