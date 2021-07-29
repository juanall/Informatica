#Ejercicio 5
#Creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente. Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.

dia_num = int(input('Que dia de la semana es en numeros?'))
if dia_num == 1:
        print("Es Lunes")
elif dia_num == 2:
        print("Es Martes")
elif dia_num == 3:
        print("Es Miercoles")
elif dia_num == 4:
        print("Es Jueves")
elif dia_num == 5:
        print("Es Viernes")
elif dia_num == 6:
        print("Es Sabado")
elif dia_num == 7:
        print("Es Domingo")
else: 
        print("El numero es incorrecto")
