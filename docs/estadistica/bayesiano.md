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

Esta información *a priori* se combina con la información de los datos, denotada como $f_{X| \Theta}(x|\theta)$ o $p(x|\theta)$ con el fin de obtener la *distribución a posteriori*. denotada como $f_{\Theta|X}(\theta|x)$ o $p(\theta|x)$ usando la regla de Bayes.
