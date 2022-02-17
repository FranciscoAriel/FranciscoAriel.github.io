---
title: Introducción a Procesos Estocásticos
summary: Introducción a Procesos estocásticos, definiciones y ejemplos.
authors: Francisco Vázquez
date: 2022-02-16
---

En esta sección se estudiará a los procesos estocásticos, los cuales pueden ser considerados una generalización de una muestra aleatoria.

El estudio de procesos estocásticos requiere el uso de varios conceptos de probabilidad, por que se recomienda leer la página de [Introducción a la probabilidad](probabilidad.md).

## Introducción

Un proceso estocástico (o probabilístico) puede considerarse una generalización de una muestra aleatoria, en el sentido de que las variables aleatorias __no son necesariamente independientes__ y su distrbución podría cambiar.

!!! note "Proceso estocástico"
    Un _proceso estocástico_ $\lbrace X(t) : t \in T \rbrace$ es una colección de variables aleatorias _indizadas_ con valores en un conjunto $T$, en donde $T$ es un conjunto a lo más numerable o un intervalo de números reales en $[0,\infty)$.

De la definición anterior se entiende que las variables _dependerán_ del parámetro $t$ (usualmente el tiempo) y están ordenadas. Además el conjunto $T$ puede ser discreto o continuo.

Si el conjunto de índices $T$ es discreto,se le conoce como _proceso estocástico de tiempo discreto_ mientras que si $T$ es continuo, se le conoce como _proceso estocástico de tiempo coninuo_. 

Una realización de realización del proceso $X(t)$ se le conoce como _camino muestral_ y se entiende como el estado del proceso en el tiempo $t$ (Ross, 1996).

## Bibliografía

Ross, S. M. (1996). Stochastic Processes (Second Edition). John Wiley & Sons.
