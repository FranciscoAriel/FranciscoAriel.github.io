---
title: Python básico
summary: Primer sesión con Python - lectura y exploración de datos.
authors: Francisco Vázquez
date: 2020-02-06
---

## Librerías

El primer paso es llamar las librerías que se utilizarán en la sesión. Usaremos __pandas__ y __numpy__ y otra librería adicional llamada __os__.

````python
import pandas as pd
import numpy as np
import os
````

!!! Nota
    En ocasiones es preferible usar nombres más cortos para referirnos a
    los nombres de las librerías. Por ejemplo, a `pandas` le llamaremos `pd` y `np` para referirnos a `numpy`.

Ahora llamaremos a la función para leer los datos.

````python
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

Para visualizar los primeros 5 datos se puede usar este código

````python
datos.head(n=5)
````
