#Ejercicio 15
#Creá un programa para gestionar datos de los socios de un club, el cual permita:

#Cargar la información de los socios en un diccionario para acceder por número de socio. Los datos que se deben almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al dia (s/n) (el programa tiene que dejar de cargar cuando se ingrese el número 0). El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:

#Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día

#Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día

#Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día

#Informar la cantidad de socios que tiene el club.

#Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.

#Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.

#Solicitar el nombre y apellido d eun socio y darlo de baja (eliminarlo del listado).

#Imprimir el listado de socios completos.

#Definir las funciones que creas necesarias.

socios = {}
socios["1"] = ["Florencia Ocampo", "14/09/2001", "cuota al día"]
socios["2"] = ["David Estevez", "14/09/2001", "cuota al día"]
socios["3"] = ["Sofia Caceres", "14/09/2001", "cuota al día"]
numero_socio = int(input("ingresar el numero de socio:"))
while numero_socio > 0:
    nombre_y_apellido = input("ingresar el nombre y el apellido:")
    fecha_ingreso = input("ingresar la fecha de ingreso con el siguiente formato = ddmmaa : ")
    estado_cuota = input("ingresar 'cuota al día' o 'cuota atrasada': ")
    socios[numero_socio] = [nombre_y_apellido, fecha_ingreso, estado_cuota]
    numero_socio = int(input("ingresar el numero de socio:")



def pago_cuotas(nro):
    if socios[nro][2] == "cuota al día":
        return print("el socio", nro, "no tiene deudas")
    else:
        return print("el socio", nro, "tiene deudas")

socios["444"] = ["Mario Fernandez", "21/10/2017", "cuota al día"]
socios["555"] = ["Juan Peres", "21/10/2017", "cuota al día"]
socios["666"] = ["Maria Martinez", "21/10/2017", "cuota al día"]
def cambiar_fecha (fecha_nueva):
    for a in socios.keys():
        if socios[a][1] == "21/10/2017":
                socios[a][1] = fecha_nueva
		else:
                socios[a][1]
cambiar_fecha("22/10/2017")
print(socios.values())

def dar_de_baja (nombre):
    for a in socios.keys():
        if socios[a][0] == nombre:
	del socios[a]
dar_de_baja ("Florencia Ocampo")
print(socios.values())