# Ejemplo de código


# cargar las librerías
import pandas as pd
import numpy as np
import os

# cambiar y ver el directorio de trabajo
os.chdir("C:\\Users\\Francisco\\FranciscoAriel.github.io\\site\\python\\src")
root=os.getcwd()
print(root)

nombres = ["ANGELICA","BRENDA","LILIANA","MARCO","FABIAN","MAURICIO"]
gpo = ["A","A","B","B","C","C"]
puntajes = [10,9,8,8,9,7]

dic = {"nombre":nombres,"grupo":gpo,"puntaje":puntajes}

mi_base = pd.DataFrame(dic)

print(mi_base)

# Leer archivos en csv (mismo directorio)
datos = pd.read_csv("census.csv")

# ver la info del archivo
datos.info()
datos.describe()

# Mostrar las primeras 5 observaciones
datos.head(n=5)
# vectores
x=(1,2,3,4,5)
type(x)
print(x)
y=(2,4,6,8,10)
z=x+y
print(z)