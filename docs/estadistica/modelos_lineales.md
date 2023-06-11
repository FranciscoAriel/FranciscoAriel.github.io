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

donde $f$ es una función (lineal), $\beta$ es un parámetro de interés y $e$ es un término de error aleatorio, en general se pretende explicar a la variable respuesta por medio de una relación de las variables explicativas y parámetros más un término de error aleatorio. Para fines prácticos, es preferible expresarlos en términos de matrices y vectores.

$$
\mathbf{y} = \mathbf{X} \vec{\beta} + \mathbf{e}
$$

donde $\mathbf{y}$ es el vector de observaciones de la variable respuesta, $\mathbf{X}$ es la matriz diseño que contiene las covariables o variables explicativas, $\vec{\beta}$ es un vector que contiene los parámetros del modelo y $\mathbf{e}$ es el vector de errores del modelo.

A continuación se ilustran algunos ejemplos de modelos lineales.

??? example "Regresión lineal simple"
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

??? example "Modelo ANOVA balanceado de una vía"
    Un modelo ANOVA de una vía puede expresarse como un modelo lineal.

    $$
    y_{ij} = \mu + \tau_i + e_{ij}
    $$

    donde $y_{ij}$ es la respuesta de la j-ésima observación que recibió el i-ésimo tratamiento, $\tau_{ij}$ es el efecto del tratamiento $i$, $\mu$ es la media general y $e_{ij}$ es el error experimental. Este modelo puede expresarse de forma matricial suponiendo que hay $k$ tratamientos y 2 réplicas:

    $$
    \begin{pmatrix}
    y_{11} \\
    y_{12} \\
    \vdots \\
    y_{k2}
    \end{pmatrix} = 
    \begin{pmatrix}
    1 & 1 & \dots & 0 \\
    1 & 1 & \dots & 0\\
    \vdots & \vdots & \ddots & \vdots \\
    1 & 0 & \dots & 1
    \end{pmatrix} 
    \begin{pmatrix}
    \mu \\
    \tau_1 \\
    \vdots \\
    \tau_k
    \end{pmatrix} + 
    \begin{pmatrix}
    e_{11} \\
    e_{12} \\
    \vdots \\
    e_{k2}
    \end{pmatrix}
    $$

Como se mostró en los ejemplos anteriores, la matriz diseño juega un papel muy importante ya que dependiendo de su estructura, se podrán obtener estimadores de los parámetros del modelo, por lo que es importante estudiarla con detalle. A continuación se da una definición muy importante para caracterizar a las matrices diseño que son usadas en los modelos lineales

!!! abstract "Dependencia lineal"
    Se dice que un conjunto de vectores $\mathbf{x}_1,\mathbf{x}_2,\dots,\mathbf{x}_p$ son _linealmente dependientes_ si existen escalares $c_1,c_2,\dots, c_p$ (no todos ceros) tales que

    $$
    c_1 \mathbf{x}_1 + c_2 \mathbf{x}_2 + \dots + c_p \mathbf{x}_p = \mathbf{0}
    $$

En otras palabras los vectores $\mathbf{x}_1,\mathbf{x}_2,\dots,\mathbf{x}_p$ son _linealmente independientes_ si $c_1 = c_2 = \dots = c_p = 0$.

!!! abstract "Rango de una matriz"
    Sea $\mathbf{X}$ una matriz de dimensión $n \times p$. El __rango__ de una matriz es el _número de columnas (o renglones) linealmente independientes_. Se dice que la matriz $\mathbf{X}$ es de rango completo si

    $$
    R(\mathbf{X}) = \min(n,p)
    $$

    En el caso que $R(\mathbf{X}) < \min(n,p)$, se dice que la matriz es de _rango incompleto_.


En la siguiente sección se estudiará más a detalle los modelos lineales de acuerdo a su rango.

Debido a que es común trabajr con matrices y vectores, se ilustrará de forma breve cómo usar software estadístico para introducir matrices de forma manual. En secciones posteriores se usarán rutinas más completas y eficientes para realizar estas tareas.

??? example "Modelo lineal con software"
    Se usará el ejemplo 6.2 de Rencher y Schaalje (2008) para mostrar cómo introducir los datos en forma matricial
    
    === "Julia"

        Primero se definirá el vector `y` que contiene las calificaciones finales y posteriormente la matriz diseño `X`.

        ``` julia
        y = [95, 80, 0, 0, 79, 77, 72, 66, 98, 90, 0, 95, 35, 50, 72, 55, 75, 66]
        X = [1 96; 1 77; 1 0; 1 0; 1 78; 1 64; 1 89; 1 47; 1 90; 1 93; 
            1 18; 1 86; 1 0; 1 30; 1 59; 1 77; 1 74; 1 67;]
        ```

    === "Python"

        Para poder trabajar con vectores y matrices, se debe cargar la librería `numpy`.

        ``` python
        import numpy as nu
        y =  nu.array([95, 80, 0, 0, 79, 77, 72, 66, 98, 90, 0, 95, 35, 50, 72, 55, 75, 66])
        X = nu.array([[1, 96], [1, 77], [1, 0], [1, 0], [1, 78], [1, 64], [1, 89], [1, 47], [1, 90],
            [1, 93], [1, 18], [1, 86], [1, 0], [1, 30], [1, 59], [1, 77], [1, 74], [1, 67]])
        ```
    
    === "R"

        En R existen funciones nativas para crear matrices y vectores de forma sencilla.

        ``` r
        y = c(95, 80, 0, 0, 79, 77, 72, 66, 98, 90, 0, 95, 35, 50, 72, 55, 75, 66)
        X = matrix(c(1, 96, 1, 77, 1, 0, 1, 0, 1, 78, 1, 64, 1, 89, 1, 47, 1, 90, 1, 93,
            1, 18, 1, 86, 1, 0, 1, 30, 1, 59, 1, 77, 1, 74, 1, 67), ncol = 2, byrow = T)
        ```
    
    === "SAS"

        En SAS se requiere el uso del módulo SAS/IML con el fin de usar el lenguaje de matrices y vectores.

        ``` sas
        PROC IML;
        y = {95, 80, 0, 0, 79, 77, 72, 66, 98, 90, 0, 95, 35, 50, 72, 55, 75, 66};
        X = {1  96, 1  77, 1  0, 1  0, 1  78, 1  64, 1  89, 1  47, 1  90, 1  93, 1  18,
            1  86, 1  0, 1  30, 1  59, 1  77, 1  74, 1  67};
        QUIT;
        ```

## Inferencia

Dado el modelo lineal $\mathbf{y} = \mathbf{X} \vec{\beta} + \mathbf{e}$ donde $\mathbf{y}$ es el vector de observaciones de la variable respuesta, $\mathbf{X}$ es la matriz diseño que contiene las covariables o variables explicativas, $\vec{\beta}$ es un vector que contiene los parámetros del modelo y $\mathbf{e}$ es el vector de errores del modelo. Se asume que $E(\mathbf{e}) = \mathbf{0}$ y $V(\mathbf{e}) = \sigma^2 I$.

Para encontrar el estimador de $\vec{\beta}$, denotado como $\hat{\beta}$ mediante el _método de Mínmos Cuadrados Ordinarios_.

??? example "Derivación del método de Mínimos Cuadrados Ordinarios"
    El estimador de _mínimos cuadrados_ es el vector que minimiza la suma de cuadrados del vector $\mathbf{y}$ con respecto a $\mathbf{X} \vec{\beta}$.

    \(
    \begin{align*}
    S(\vec{\beta}) &= (\mathbf{y}-\mathbf{X} \vec{\beta})^´(\mathbf{y}-\mathbf{X} \vec{\beta})\\
    & = \mathbf{y}^´\mathbf{y} - 2 \vec{\beta}^´ \mathbf{X}^´\mathbf{y} + \vec{\beta}^´\mathbf{X}^´\mathbf{X}\vec{\beta}
    \end{align*}
    \)

    Para hallar el mínimo se deriva con respecto a $\vec{\beta}$ y se iguala a cero.

    $$
    \frac{\partial}{\partial \vec{\beta}}S(\vec{\beta}) = - 2 \mathbf{X}^´\mathbf{y} + 2 \mathbf{X}^´\mathbf{X}\vec{\beta} = 0
    $$

    Al sistema de ecuaciones resultante $\mathbf{X}^´\mathbf{X}\vec{\beta} = \mathbf{X}^´\mathbf{y}$ se le conoce como _Ecuaciones Normales_. Al resolver este sistema de ecuaciones si la inversa $(\mathbf{X}^´\mathbf{X})^{-1}$ existe  , se obtiene el estimador de mínimos cuadrados ordinarios, dados por:

    $$
    \hat{\beta} = (\mathbf{X}^´\mathbf{X})^{-1}\mathbf{X}^´\mathbf{y}
    $$

## Modelos de rango completo

## Modelos de rango incompleto

## Referencias

- Rencher, Alvin C., y G. Bruce Schaalje. 2008. _Linear Models in Statistics_. 2nd ed. New Jersey: John Wiley & Sons.
