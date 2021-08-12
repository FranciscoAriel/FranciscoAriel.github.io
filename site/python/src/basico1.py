# Ejemplo de código


# cargar las librerías
import pandas as pd
import numpy as np
import os

# cambiar y ver el directorio de trabajo
os.chdir("C:\\Users\\Francisco\\FranciscoAriel.github.io\\site\\python\\src")
root=os.getcwd()
print(root)

# Leer archivos en csv (mismo directorio)
datos = pd.read_csv("census.csv")

# ver la info del archivo
datos.info()
datos.describe()

# Mostrar las primeras 5 observaciones
datos.head(n=5)