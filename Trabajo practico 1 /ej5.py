#Realizar un programa que lea tres números por teclado y calcule el promedio de ellos.
numero = 0.0
for num in range(3):
    print('Ingrese numero {0}'.format(num),end=': ')
    numero += float(input())
    print('El promedio es: {0:.2f}'.format(numero/3))



