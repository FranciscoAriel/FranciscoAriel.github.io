---
title: Modelos Lineales
summary: Introducción a la teoría de modelos lineales con algunas aplicaciones.
author: Francisco Vázquez
date: 2023-05-30
author_gh_user: FranciscoAriel
publish_date: 2023-05-30
read_time: 35 minutos
---

## Introducción

Los __Modelos Lineales__ es un conjunto de teorías y metodologías en los cuales se estudia la _asociación lineal_ de un conjunto de covariables $x$ con una variable respuesta $y$. Las covariables pueden ser de tipo continua o categórica, pero la respuesta debe ser continua.

Algunos de los modelos que pueden ser estudiados por los modelos lineales son los siguientes.

- Regresión lineal
- Análisis de Varianza
- Análisis de Covarianza

Los modelos lineales en general pueden expresarse de la siguiente manera

$$
y = f(x,\beta) + e
$$

donde $f$ es una función (lineal), $\beta$ es un parámetro de interés y $e$ es un término de error, en general se pretende explicar a la variable respuesta por medio de una relación de las variables explicativas y parámetros más un término de error aleatorio. Para fines prácticos, es preferible expresarlos en términos de matrices y vectores.

$$
\mathbf{y} = \mathbf{X} \mathbf{\beta} + \mathbf{e}
$$

donde $\mathbf{y}$ es el vector de observaciones de la variable respuesta, $\mathbf{X}$ es la matriz diseño que contiene las covariables o variables explicativas, $\beta$ es un vector que contiene los parámetros del modelo y $\mathbf{e}$ es el vector de errores errores del modelo.

En modelos lineales es muy importante conocer la estructura de la matriz diseño $\mathbf{X}$ ya que dependiendo de su estructura, se podrán obtener estimadores de los parámetros del modelo.

??? example "Regresión lineal"
    El siguiente ejemplo fue tomado de Rencher y Schaalje (2008). Se desea conocer si la calificación promedio de las tareas $x$ incide en la calificación final $y$ para un grupo de 18 alumnos. Un modelo de regresión lineal puede establecer esta relación de la siguiente manera:

    $$
    y_i = \beta_0 + \beta_1 x_i + e_i
    $$

    Puede ser expresado en forma matricial de la siguiente manera

    $$
    \begin{pmatrix}
    95 \\
    80 \\
    \vdots \\
    66
    \end{pmatrix} = 
    \begin{pmatrix}
    1 & 96 \\
    1 & 77 \\
    \vdots & \vdots \\
    1 & 67
    \end{pmatrix} 
    \begin{pmatrix}
    \beta_0 \\
    \beta_1
    \end{pmatrix} + 
    \begin{pmatrix}
    e_1 \\
    e_2 \\
    \vdots \\
    e_{18}
    \end{pmatrix}
    $$

En la siguiente sección se estudiará más a detalle los distintos modelos lineales.

## Modelos de rango completo

## Modelos de rango incompleto

## Referencias

- Rencher, Alvin C., y G. Bruce Schaalje. 2008. _Linear Models in Statistics_. 2nd ed. New Jersey: John Wiley & Sons.
