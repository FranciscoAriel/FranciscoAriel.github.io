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

Note que cada renglón representa una observación multivariada, mientras que cada columna denota una variable.

## Muestras aleatorias

Debido a que en estadística es de interés hacer inferencias sobre el conjunto de datos, se requiere hacer ciertos supuestos sobre la información. En particular se supondrá que la información es una *muestra aleatoria multivariada* de una población específica.

En este sentido, la matriz de datos $\mathbf{X}$ será considarada como una *muestra aleatoria* de dimensión $n$.

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

Vector de medias

Varianzas

## Bibliografía

Johnson, R., & Wichern, D. (2007). *Applied Multivariate Statistical Analysis* (6th edition). Pearson Education.
