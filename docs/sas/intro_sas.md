---
title: Introducción a SAS
summary: Una guía rápida sobre SAS.
authors: Francisco Vázquez
date: 2020-02-05

---

Esta es un tutorial rápido sobre el programa.

## Instalación

Consulte el sitio web de [sas](https://www.sas.com) para más detalles.

!!! info "SAS University Edition"
    SAS no es software libre ni es gratuito, sin embargo usted puede descargar el software gratuitamente.
    Visite [SAS University edition](https://www.sas.com/en_us/software/university-edition.html) para más información.

## Interfaces gráficas

### SAS Base

Es la interfaz gráfica clásica de SAS. Contiene una verntana lateral con una lista de librerías, mientras que hay una ventana principal de mensajes (log) y otra para escribir código.

![Screenshot](sasbase.png)

### SAS Enterprise Guide

### SAS Studio

## Conceptos básicos

### Datasets

### Librerías

### Procedimientos

### Variables macro

Es posible definir variables mediante funciones especiales mediante el uso de sentencias macro. Dichas variables pueden ser llamadas en cualquier procedimiento y son evaluadas.

Se usa la sentencia `%let macro-variable = <value>;` y para mandar llamar el valor de dicha variable maro se usa `&macro-variable`.

Por ejemplo si se desea definir ciertas variables a analizar, se puede crear la siguiente sentencia;

````sas
%let x = age weight height;

proc means data = sashelp.class;
    var &x;
run;
````

Para ver el valor de la variable macro, se puede usar la sentencia macro `%PUT <&macro-variable>`, por ejemplo:

````sas
%PUT &x;
````

y el resultado será

> age weight height

Para más información acerca de sentencias y variables macro visite la [documentación de SAS](https://documentation.sas.com/?cdcId=pgmsascdc&cdcVersion=9.4_3.5&docsetId=mcrolref&docsetTarget=titlepage.htm&locale=es).
