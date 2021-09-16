---
title: Primeros pasos Julia
summary: Una guía rápida sobre Julia.
authors: Francisco Vázquez
date: 2021-09-13
---

## Lectura de datos

En Julia existen diversos paquetes que nos permiten importar y leer datos de archivos externos. En esta sección nos enfocaremos a la creación de conjuntos de datos.

### Creación de datos

Para manipular conjuntos de datos, se puede usar el paquete [DataFrames](https://dataframes.juliadata.org/stable/).

!!! caution "Instalar el paquete"
    No olvide instalar el paquete `DataFrames`, de otro modo se obtendrá un error.

Por ejemplo, para crear el siguiente conjunto de datos

nombre   |grupo        |puntaje
---------|-------------|-------
ANGELICA  |A           |10
BRENDA    |A           |9
LILIANA   |B            |8
MARCO     |B            |8
FABIAN    |C            |9
MAURICIO  |C            |7

se puede escribir en la consola el siguiente comando:

````julia
using DataFrames
datos = DataFrame(nombre =["ANGELICA","BRENDA","LILIANA","MARCO","FABIAN","MAURICIO"],
    grupo = ["A","A","B","B","C","C"],
    puntaje = [10,9,8,8,9,7]);
print(datos)
````

Este código crea un objeto llamado _datos_ que es de tipo _DataFrame_. La forma de definir su contenido es mediante _constructores_ que en este caso son las columnas, aunque pueden ser vectores definidos previamente. 

Para visualizar el objeto, se puede usar el comando `print()`. El resultado se muestra a continuación.

![Resultado de los datos](img/datos.png)

### Leyendo un archivo CSV

Para leer un archivo csv, recomienda el uso de los paquetes _CSV_ y _DataFrames_.

El siguiente código muestra cómo importar un archivo csv a un objeto `DataFrame`.

````julia
using CSV, DataFrames
mi_csv = CSV.read("C:\\Users\\Francisco\\census.csv",DataFrame)
summary(mi_csv)
````

La primer línea carga los paquetes instalados previamente, para poder usar todas sus funciones y métodos. En la segunda, se usa la función `CSV.read()` especificándole el nombre de archivo y la función _sink_, en este caso será `DataFrame`, asignándolo al objeto _mi_csv_. Debido a que el archivo es grande se sugiere ver las dimensiones del dataframe usando la función `summary()`.