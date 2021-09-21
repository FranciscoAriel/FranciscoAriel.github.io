---
title: Python básico
summary: Primer sesión con Python - lectura y exploración de datos.
authors: Francisco Vázquez
date: 2020-02-06
---

# Introducción

En esta sección aprenderemos acerca de cómo leer datos en python, así como el manejo de datos con python.

## Lectura de datos

Para manejar datos en python se usan librerías especiales

El primer paso es llamar las librerías que se utilizarán en la sesión.

````python
import pandas as pd
import numpy as np
import os
````

La librería __pandas__ es la que nos permite manejar objetos de tipo _dataframe_.

### Ingreso de datos de forma manual

Para introducir datos de manera manual, se puede usar la siguiente sintaxis:

````python
import pandas as pd

nombres = ["ANGELICA","BRENDA","LILIANA","MARCO","FABIAN","MAURICIO"]
gpo = ["A","A","B","B","C","C"]
puntajes = [10,9,8,8,9,7]

dic = {"nombre":nombres,"grupo":gpo,"puntaje":puntajes}

mi_base = pd.DataFrame(dic)
print(mi_base)
````

La forma más sencilla de crear un dataframe es mediante la definición de un diccionario con las listas definidas y posteriormente se usa la función `DataFrame` del paquete _pandas_ y se crea el objeto `datos`. El objeto `datos` hereda las claves del diccionario y los valores se escriben en el dataset.

La siguiente imagen muestra el dataframe definido.

![Resultado del dataset](img/dataframe.png)

### Lectura de archivos externos

Para leer archivos externos, se usa la función `read_csv` de la librería _pandas_ para leer los datos.

````python
import pandas as pd

datos = pd.read_csv("census.csv")
````

Como puede observarse, `datos` es un objeto **DataFrame** que se define gracias a la función `read_csv()` de pandas. Se puede obtener información del objeto usando el siguiente comando.

````python
datos.info()
````

Para ver un resumen de los datos se puede usar

````python
datos.describe()
````

La siguiente imagen muestra el resultado obtenido de la consola.

![Salida del objeto dataframe](img/info.png)

Para visualizar los primeros 5 datos se puede usar este código

````python
datos.head(n=5)
````
