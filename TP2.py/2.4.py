#Ejercicio 4
#Una compañía de transporte internacional tiene servicio en algunos países de América del Sur, América Central, América del Norte, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido, tal como se muestra en la tabla:
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. Realizá un programa para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

AMERICA_DEL_SUR = 1
AMERICA_CENTRAL = 2
AMERICA_DEL_NOR = 3
EUROPA          = 4
ASIA            = 5
pesoPaquete = float(input('Ingrese el peso del paquete en gramos: '))
if (pesoPaquete < 5000):
        print('\t Ubicación \t Costo/gramo')
        print('\t 1 - {0} \t U$S{1}'.format('América del Sur',10.00))
        print('\t 2 - {0} \t U$S{1}'.format('América Central',15.00))
        print('\t 3 - {0} \t U$S{1}'.format('América del Norte',18.00))
        print('\t 4 - {0} \t\t U$S{1}'.format('Europa',24.00))
        print('\t 5 - {0} \t\t U$S{1}'.format('Asia',30.00))
        ubicacion = int(input(''))
        if   (ubicacion == AMERICA_DEL_SUR):
            print('El cobro por enviar el paquete es U$S {0:.2f}'.format(pesoPaquete*10))
        elif (ubicacion == AMERICA_CENTRAL):
            print('El cobro por enviar el paquete es U$S {0:.2f}'.format(pesoPaquete*15))
        elif (ubicacion == AMERICA_DEL_NOR):
            print('El cobro por enviar el paquete es U$S {0:.2f}'.format(pesoPaquete*18))
        elif (ubicacion == EUROPA):
            print('El cobro por enviar el paquete es U$S {0:.2f}'.format(pesoPaquete*24))
        elif (ubicacion == ASIA):
            print('El cobro por enviar el paquete es U$S {0:.2f}'.format(pesoPaquete*30))
        else:
            print('Código inválido')
else:
    print('El paquete no puede transportarse')


nombre = input()
apellido1 = input()
apellido2 = input()

#O

gramos = int(input("ingrese el peso e gramos:"))
zona = input("ingrese la zona:")
if gramos < 5000:
    if zona == "america del sur":
        print(10 * gramos)
    if zona == "america central":
	        print(15 * gramos)
    if zona == "america del norte":
    	print(18 * gramos)
	if zona == "europa":
		    print(24 * gramos)
	if zona == "asia":
		    print(30 * gramos)
else:
        print("su paquete fue rechazado")