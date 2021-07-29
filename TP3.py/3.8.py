
#Escribí un programa que separe y devuelva los caracteres numéricos de un string.

import re
edad_y_nombre = "Me llamo Juana y tengo 19 años"
print(edad_y_nombre)
print([float(s) for s in re.findall(r'-?\d+\.?\d*', edad_y_nombre)])