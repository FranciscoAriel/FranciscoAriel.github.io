---
title: Python básico
summary: Primer sesión con Python - lectura y exploración de datos.
authors: Francisco Vázquez
date: 2020-02-06
---

# Introducción

En esta sección aprenderemos acerca de cómo leer datos en python, así como el manejo de datos con python.

Para manejar datos en python se usan librerías especiales. En particular se usará la librería *pandas* para realizar estas operaciones.

El primer paso es llamar las librerías que se utilizarán en la sesión.

````python
import pandas as pd
import numpy as np
import os
````

La librería __pandas__ es la que nos permite manejar objetos de tipo _dataframe_ que es la estructura de datos usada en python para almacenar la información. La librería __numpy__ nos permitirá crear arreglos y manipularlos de forma más fácil. La librería __os__ nos ayudará a usar funciones y otras utilidades del sistema operativo.

Los códigos mostrados se realizaron en un cuaderno interactivo de python (archivo ipynb) usando Visual Studio Code.

## Creando un objeto DataFrame

La forma más sencilla de crear un *dataframe* es mediante la definición de un diccionario con las listas definidas y posteriormente se usa la función `DataFrame` del paquete _pandas_ para crear un objeto `DataFrame` en donde se almacenará la información. El objeto creado hereda las claves del diccionario y los valores se escriben en el dataset.

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

La siguiente imagen muestra el dataframe definido.

![Resultado del dataset](img/dataframe.png)

Note que el objeto creado es un objeto especial. Si escribimos en la consola el comando `type(mi_base)`, obtenemos la siguiente información.

> pandas.core.frame.DataFrame

Como tal, este objeto va a tener diversos métodos para manipularlo o conocer sus propiedades. Consulte la [referencia de DataFrame](https://www.w3schools.com/python/pandas/pandas_ref_dataframe.asp) para saber más de sus propiedades.

## Lectura de archivos externos

Para leer archivos externos, por ejemplo de tipo csv, se usa la función `read_csv` de la librería _pandas_ para leer los datos.

El siguiente código muestra cómo leer un archivo que está almacenado en la misma carpeta del directorio de trabajo.

````python
import pandas as pd

datos = pd.read_csv("census.csv")
````

Como puede observarse, `datos` es un objeto **DataFrame** que se define gracias a la función `read_csv()` de pandas. En este caso, el archivo estaba en la misma carpeta que el directorio de trabajo.

Para conocer cual es el directorio de trabajo, se puede usar el siguiente comando:

````
root=os.getcwd()
print(root)
````

El resultado devolverá la ruta del directorio de trabajo, por ejemplo:

> 'c:\\Users\\Usuario\\Documents\\proyectos\\python\\src'

Para modificar el directorio de trabajo, se puede usar el siguiente código:

````python
os.chdir("C:\\Users\\Usuario\\Documents\\proyectos\\python\\datos")
````

Por lo que solo basta copiar los archivos a esta carpeta para poder importarlos sin problema.

## Exploración de la base

Se puede obtener información de un objeto **DataFrame** usando el siguiente comando.

````python
datos.info()
````

La siguiente imagen muestra el resultado obtenido de la consola.

![Salida del objeto dataframe](img/info.png)

Para ver un análisis descriptivo de las variables numéricas datos se puede usar el método `describe`.

````python
datos.describe()
````

El resultado se muestra a continuación

![Análisis descriptivo](img/descriptivo.png)

!!! caution "Métodos sin argumentos"
    Note que los métodos anteriores no requieren ningún argumento, porlo que solo se ponen los paréntesis vacíos.

Para visualizar los primeros 5 datos se puede usar este código

````python
datos.head(n=5)
````

La siguiente imagen muestra las primeras 5 observaciones

![Primeros 5 datos](img/primeros.png)

De manera similar, los últimos 5 registros se pueden ver con este código

````python
datos.tail(n=5)
````

La siguiente imagen muestra las últimas 5 observaciones

![Últimos 5 datos](img/ultimos.png)

!!! tip "Argumentos opcionales"
    Algunos métodos no requieren argumentos, mientras que en otros son opcionales. Los métodos `head()` y `tail()` tienen un valor predeterminado de 5.

Al igual que otros lenguajes de programación, es posible acceder a los elementos de un dataframe. Para ello se puede hacer uso del método `iloc`.

El siguiente código muestra cómo acceder al segundo renglón de un dataframe y el resultado que se obtiene.

````python
mi_base.iloc[1,]
````

El resultado se muestra a continuación

![Segundo elemento](img/elemento.png)

!!! caution "Método sin paréntesis"
    Note que el método `iloc` __no__ usa paréntesis.

## Transformación y manipulación de un dataframe

Al igual que en otros lenguajes de programación, es posible modifcar las bases en python a través de los métodos del objeto dataframe.

### Ordenando una base

Para ordenar una base, se usa el método `sort.values()` en donde se le pasa una lista con los nombres de las variables a ordenar.

El siguiente código muestra su uso.

````python
base_ord = mi_base.sort_values(by=["nombre"])
print(datos_ord)
````

La siguiente imagen muestra el resultado, note que la base se ha guardado en un nuevo objeto.

![Base ordenada](img/sort.png)
