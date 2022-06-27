---
title: Introducción a la Estadística Multivariada
summary: Una introducción a lo métodos multivariados con algunas aplicaciones.
author: Francisco Vázquez
date: 2022-05-31
author_gh_user: FranciscoAriel
publish_date: 2022-05-31
read_time: 15 minutos
---

La estadística multivariada es un área que estudia datos recolectados de individuos a los cuales se les mide una o más características.

Usualmente los datos, denotados por $\mathbf{X}$, son registrados en forma rectangular por medio de columnas y renglones. Esta forma permite representar los datos en forma *matricial*.

\(\mathbf{X} =\lbrace X_{i,j}\rbrace = 
\begin{bmatrix}
X_{1,1} & X_{1,2} & \dots & X_{1,p} \\
X_{2,1} & X_{2,2} & \dots & X_{2,p} \\
\vdots & \vdots &\ddots & \vdots \\
X_{n,1} & X_{n,2} & \dots & X_{n,p} \\
\end{bmatrix}
\)

Note que cada renglón representa una observación multivariada, mientras que cada columna denota una variable, se usarán letras minúsculas pára refereirse a *observaciones* o *realizaciones*.

## Muestras aleatorias

Debido a que en estadística es de interés hacer inferencias sobre el conjunto de datos, se requiere hacer ciertos supuestos sobre la información. En particular se supondrá que la información es una *muestra aleatoria multivariada* de una población específica.

En este sentido, la matriz de datos $\mathbf{X}$ será considerada como una *muestra aleatoria* de dimensión $n$.

\(\mathbf{X} =
\begin{bmatrix}
X_{1,1} & X_{1,2} & \dots & X_{1,p} \\
X_{2,1} & X_{2,2} & \dots & X_{2,p} \\
\vdots & \vdots &\ddots & \vdots \\
X_{n,1} & X_{n,2} & \dots & X_{n,p} \\
\end{bmatrix} =
\begin{bmatrix}
\mathbf{X}_{1}^t \\
\mathbf{X}_{2}^t \\
\vdots \\
\mathbf{X}_{n}^t \\
\end{bmatrix}
\)

!!! note "Muestra aleatoria"
    Se dice que los vectores renglón $\mathbf{X}_{1}^t,\mathbf{X}_{2}^t,\dots,\mathbf{X}_{n}^t$ son una muestra aleatoria de una función de distribución conjunta $f(X)$. La función de distribución conjunta está dada por $f(\mathbf{X}_{1})f(\mathbf{X}_{2})\dots f(\mathbf{X}_{n})$.

Note que generalmente en cada observación, $\mathbf{X}_i=(X_{i,1},X_{i,2},\dots,X_{i,p})$, las $p$ variables pueden estar correlacionadas debido a que se mide a un mismo individuo; sin embargo, se asume que los individuos han de ser independientes unos de otros.

Debido a que se tiene una muesta aleatoria, es de interés conocer los momentos o características de dicha función de distribución, para ello se usan los estimadores insesgados para estimar el vector de medias. A continuación se mostrará cómo estimar dichos parámetros.

### Vector de medias y matriz de covarianzas muestrales

Para estimar a $\mathbf{\mu}$ de la matriz de datos se puede usar el *vector de medias muestrales* $\bar{\mathbf{X}}=\frac{1}{n}\mathbf{X}^t\mathbf{1}$, donde $\mathbf{1}^t=\begin{pmatrix}1&1&\dots&1\end{pmatrix}$ es de $1\times n$.

De manera similar, para estimar la matriz de covarianzas, se usa la *matriz de covarianzas muestrales* $\mathbf{S}=\frac{1}{n-1}\mathbf{X}^t\left(\mathbf{I}-\frac{1}{n}\mathbf{1}\mathbf{1}^t\right)\mathbf{X}$.

Se usará la notación $\bar{\mathbf{x}}$ y $\mathbf{s}$ para referirse a realizaciones

??? example "Cálculo del vector de medias y matriz de covarianzas muestrales"
    En este ejemplo se mostrará cómo calcular el vector de medias muestrales. Supónga que se tiene la siguiente matriz de datos con $n=3$ y $p=2$.

    \(\mathbf{x} =
    \begin{bmatrix}
    9 & 1 \\
    5 & 3 \\
    1 & 2 \\
    \end{bmatrix} 
    \)

    Haciendo la sustitución se tiene que el vector de medias es:

    \(
    \bar{\mathbf{x}}= \frac{1}{3}\begin{bmatrix}
    9 & 5 & 1 \\
    1 & 3 & 2\\
    \end{bmatrix}
    \begin{bmatrix}
    1 \\
    1 \\
    1 \\
    \end{bmatrix} = \frac{1}{3}\begin{bmatrix}
    15\\
    6\\
    \end{bmatrix} =
    \begin{bmatrix}
    5\\
    2\\
    \end{bmatrix}
    \)

    y la matriz de covarianzas:

    \(
    \begin{align*}
    \mathbf{s}&=\frac{1}{2}\begin{bmatrix}
    9 & 5 & 1 \\
    1 & 3 & 2\\
    \end{bmatrix}\left( \begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0\\
    0 & 0 & 1\\
    \end{bmatrix} -\frac{1}{3}    \begin{bmatrix}
    1 \\
    1 \\
    1 \\
    \end{bmatrix}
    \begin{bmatrix}
    1 & 1 & 1 
    \end{bmatrix}\right)
    \begin{bmatrix}
    9 & 1 \\
    5 & 3 \\
    1 & 2 \\
    \end{bmatrix} \\
    & = \frac{1}{2}
    \begin{bmatrix}
    9 & 5 & 1 \\
    1 & 3 & 2\\
    \end{bmatrix}
    \begin{bmatrix}
    2/3 & -1/3 & -1/3 \\
    -1/3 & 2/3 & -1/3\\
    -1/3 & -1/3 & 2/3\\
    \end{bmatrix}
    \begin{bmatrix}
    9 & 1 \\
    5 & 3 \\
    1 & 2 \\
    \end{bmatrix}\\
    & =\frac{1}{2}
    \begin{bmatrix}
    4 & 0 & -4 \\
    -1 & 1 & 0\\
    \end{bmatrix}
    \begin{bmatrix}
    9 & 1 \\
    5 & 3 \\
    1 & 2 \\
    \end{bmatrix}\\
    & =\frac{1}{2}
    \begin{bmatrix}
    32 & -4 \\
    -4 & 2 \\
    \end{bmatrix}\\
    &=\begin{bmatrix}
    16 & -2 \\
    -2 & 1 \\
    \end{bmatrix}
    \end{align*}
    \)

### Matriz de Combinaciones lineales

En estadística multivariada es posible realizar combinaciones lineales de variables para formar una nueva variable. Las combinaciones lineales estudiadas tienen la forma:

\(
\mathbf{a}^t\mathbf{X}=a_1 \mathbf{X}_1 + a_2 \mathbf{X}_2 + \dots + a_p \mathbf{X}_p
\)

Note que el vector $\mathbf{a}^t$ es de dimensión $1 \times p$ y la matriz $\mathbf{X}=\begin{pmatrix}\mathbf{X}_1&\mathbf{X}_2&\dots&\mathbf{X}_p\end{pmatrix}$ es de dimensión $n\times p$, aunque solo nos interesa trabajar con las $p$ variables.

Es posible calcular la media, la varianza y las covarianzas muestrales de dichas combinaciones lineales sin la necesidad de calcular las nuevas variables.

Estadístico|Combinación lineal|Fórmula
-----------|------------------|-------
Media muestral|$\mathbf{a}^t\mathbf{X}$|$\mathbf{a}^t\bar{\mathbf{x}}$
Varianza muestral|$\mathbf{a}^t\mathbf{X}$|$\mathbf{a}^t\mathbf{s}\mathbf{a}$
Covarianzas muestrales|$\mathbf{a}^t\mathbf{X}$ y $\mathbf{b}^t\mathbf{X}$|$\mathbf{a}^t\mathbf{s}\mathbf{b}$

## Distribución normal multivariada

## Bibliografía

Johnson, R., & Wichern, D. (2007). *Applied Multivariate Statistical Analysis* (6th edition). Pearson Education.
