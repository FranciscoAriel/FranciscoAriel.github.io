---
title: SAS básico
summary: Conociendo SAS.
authors: Francisco Vázquez
date: 2020-09-26
---

# Bloques DATA y PROC

La programación en SAS está basada en dos grandes bloque DATA y PROC. El bloque DATA sirve para leer o generar datos, mientras que el bloque PROC sirve para analizar dichos datos.

Por ejemplo, el siguiente código crea una copia de un dataset existen y posteriormente lo imprime en pantalla.

````sas
DATA clase;
    SET SASHELP.CLASS;
RUN;

PROC PRINT DATA = clase;
RUN;
````

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

El resultado se muestra a continuación

![Ejemplo 1](ds1.png)
