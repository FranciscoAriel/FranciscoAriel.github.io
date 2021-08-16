---
title: SAS básico
summary: Conociendo SAS.
authors: Francisco Vázquez
date: 2020-09-26
---

## Lectura de datos

Los dataset son el insumo principal para analisis de datos en SAS, por ello iniciaremos con una rápida exploración.

La creación de un dataset inicia con un bloque `DATA` y termina con un `RUN`.

### Introducción de valores de forma manual

La forma más fácil de crear un dataset, es con el uso de la sentencia `INPUT` y `DATALINES` con el fin de introducir valores manualmente.

La sentencia `INPUT` sirve para indicar el nombre de las variables del dataset. Se puede poner el símbolo `$` para indicar que la variable es de tipo caracter.

La sentencia `DATALINES` indica el inicio de los datos y finaliza con un punto y coma.

El siguiente ejemplo crea un dataset llamado **calificaciones** y contiene 2 variables categóricas y una numérica.

````sas
DATA calificaciones;
    INPUT nombre $ Grupo $ puntaje;
    DATALINES;
    ANGELICA A 10
    BRENDA A 9
    MARCO B 8
    LILIANA B 8
    FABIAN C 9
    MAURICIO C 7
    ;
RUN;
````

SAS no muestra directamente los resultados, en su lugar, se escribe un mensaje en la ventana de log.

![Log del DATA STEP](img/log1.png)

Para visualizar el dataset creado, se debe ejecutar el siguiente código:

````sas
PROC PRINT DATA = calificaciones;
RUN;
````

El resultado se muestra a continuación

![Ejemplo 1](img/ds1.png)

Aunque se ha producido un resultado, nuevamente aparece un mensaje en la ventana del log:

![Log del PROC PRINT](img/log2.png)

En el log aparecen las instrucciones que se ejecutaron, seguido de un mensaje indicando que los resultados se estan escribiendo en un archivo html. Finalmente en el log se nos indica el número de observaciones leídas y el tiempo de ejecución del procedimiento.

Como puede verse, el log siempre está activo y registra todas las acciones ejecutadas. Posteriormente se verán como nos puede ayudar a encontrar errores y nos apoyará en la resolución de estos.

### Lectura de datos desde un archivo externo

### Leyendo archivos desde web

### Usando un procedimiento para leer datos externos
