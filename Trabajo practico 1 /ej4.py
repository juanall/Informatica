#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayúsculas
nombreApellidos = input('Ingrese nombre y dos apellidos: ')
datos = nombreApellidos.split()
for palabra in datos:
    palabra = palabra.capitalize()
    print(palabra,end=' ')
print()