
#Ejercicio 6
#Escribí un programa que dado dos diccionarios genere dos DataFrame y los una tanto en el eje de las columnas como en el eje de las filas.
import pandas as pd
def unirDF(df1,df2):
    return pd.concat([df1, df2], ignore_index=True, sort=False)