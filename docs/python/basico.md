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

Para visualizar los primeros 5 datos se puede usar este código

````python
datos.head(n=5)
````
