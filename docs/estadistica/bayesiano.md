---
title: Introducción a la Estadística Bayesiana
summary: Inferencia estadística desde el punto de vista Bayesiano.
author: Francisco Vázquez
date: 2022-05-19
author_gh_user: FranciscoAriel
publish_date: 2022-05-19
read_time: 15 minutos
---

La estadística bayesiana es un paradigma completo de inferencia basado en la *teoría de la decisión* y por lo tanto se basa en los conceptos de probabilidad.

A diferencia del enfoque frecuentista, la estadística bayesiana se basa en el enfoque de *probabilidad subjetiva*. Dicha probabilidad subjetiva es una medida o grado de creencia de qué tan verosímil sea un evento.

Por ejemplo, si le preguntáramos a cada persona sobre la probabilidad de que llueva $\theta$, cada una nos responderá según su creencia o nivel de conocimiento sobre $\theta$. Todo ese conocimiento podría resumirse en una función de distribución que llamaremos *distribución a priori*, denotada $f_\Theta(\theta)$ o $p(\theta)$.

Esta información *a priori* se combina con la *información de los datos*, denotada como $f_{X| \Theta}(x|\theta)$ o $L(\theta|x)$ con el fin de obtener la *distribución a posteriori*, denotada como $f_{\Theta|X}(\theta|x)$ o $p(\theta|x)$ usando la regla de Bayes.

\(
    p(\theta|x)=\frac{p(\theta,x)}{p(x)}=\frac{L(\theta|x)p(\theta)}{p(x)}
\)

Note que $p(x)$ es una densidad que no depende de $\theta$, por lo que la distribución a posteriori pude escribirse como:

\(
    p(\theta|x)\propto p(x|\theta)p(\theta)
\)

??? example "Lanzamiento de una moneda 1"
    Suponga que se tiene una moneda y se realizan 10 lanzamientos. Sea $\theta$ la probabilidad de que caiga águila, mientras que $1-\theta$ es la probabilidad de que caiga sol. No se tiene información acerca del comportamiento de la moneda, pero se sospecha es una moneda honesta. Supóngase que se han observado 7 águilas.

    Debido a que no se tiene información sobre $\theta$, se pude asumir una función de distribución uniforme en el intervalo [0,1], esto es: $p(\theta)=I_{(0,1)}(\theta)$.

    Note que los datos pueden ser modelados mediante la verosimilitud, es decir $p(\mathbf{x}|\theta)=L(\theta|\mathbf{x})=\prod_{i=1}^{n}\theta^{x_i}\left(1-\theta\right)^{1-x_i}=\theta^{\sum_{i=1}^{n}x_i}\left(1-\theta\right)^{n-\sum_{i=1}^{n}x_i}$.

    Sustituyendo

    \(p(\theta|x)\propto \theta^{7}\left(1-\theta\right)^{3}I_{(0,1)}(\theta)\)

    Note que como tal, **no es una función de densidad**, debido a que la integral no es 1, sin embargo, es proporcional a una función de densidad beta con parámetros 8 y 4.

    Por lo tanto, la distribución *a posteriori* es $p(\theta|x)=\frac{\theta^{8-1} \left(1-\theta\right)^{4-1}}{B(8,4)}I_{(0,1)}(\theta)$.
