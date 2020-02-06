# Ejemplo de código


# cargar las librerías
import pandas as pd
import numpy as np
import os

# ver el directorio de trabajo
root=os.getcwd()

# Leer archivos en csv (mismo directorio)
datos = pd.read_csv("census.csv")

# Mostrar las primeras 5 observaciones
datos.head(n=5)