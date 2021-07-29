#Ejercicio 12
#Creá un programa que permita guardar los nombres de los alumnos de una 
# clase y las notas que han obtenido. Cada alumno puede tener distinta 
# cantidad de notas. Guardá la información en un diccionario cuya claves 
# serán los nombres de los alumnos y los valores serán listas con las notas 
# de cada alumno. El programa tiene que pedir el número de alumnos que se va a
# introducir, luego su nombre y sus notas hasta que introduzcamos un número negativo. Al final el programa
#tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre
#de un alumno que ya existe el programa tiene que dar un error.


alumnos = {}
cantidad = int(input("Introduce la cantidad de alumnos que vamos a guradar:"))
for num in range(cantidad):
    alumno = input("Nombre del alumno:")
    while alumno in alumnos:
        print("Alumno ya existe.")
        alumno = input("Nombre del alumno:")
    notas=[]
    nota = int(input("Dame una nota del alumno (negativo para terminar):"))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Dame una nota del alumno (negativo para terminar):"))
    alumnos[alumno] = notas.copy()

for alumno, notas in alumnos.items():
    print("%s ha sacado de nota media %f" % (alumno,sum(notas)/len(notas)))

