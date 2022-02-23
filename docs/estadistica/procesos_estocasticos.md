---
title: Introducción a Procesos Estocásticos
summary: Introducción a Procesos estocásticos, definiciones y ejemplos.
author: Francisco Vázquez
date: 2022-02-16
author_gh_user: FranciscoAriel
publish_date: 2022-02-16
read_time: 5 minutos
---

En esta sección se estudiará a los procesos estocásticos, los cuales pueden ser considerados una generalización de una muestra aleatoria.

El estudio de procesos estocásticos requiere el uso de varios conceptos de probabilidad, por que se recomienda leer la página de [Introducción a la probabilidad](probabilidad.md).

## Introducción

Un proceso estocástico (o probabilístico) puede considerarse una generalización de una muestra aleatoria, en el sentido de que las variables aleatorias __no son necesariamente independientes__ y su distrbución podría cambiar.

!!! note "Proceso estocástico"
    Un _proceso estocástico_ $\lbrace X(t) : t \in T \rbrace$ es una colección de variables aleatorias _indizadas_ con valores en un conjunto $T$, en donde $T$ es un conjunto a lo más numerable o un intervalo de números reales en $[0,\infty)$.

De la definición anterior se entiende que las variables _dependerán_ del parámetro $t$ (usualmente el tiempo) y están ordenadas. Además el conjunto $T$ puede ser discreto o continuo. Si el conjunto de índices $T$ es discreto,se le conoce como _proceso estocástico de tiempo discreto_ mientras que si $T$ es continuo, se le conoce como _proceso estocástico de tiempo coninuo_.

Note que si se fija un punto $t$, se tiene $X_t$ una variable aleatoria. Una _realización_ del proceso $X(t)$, es decir si se observa la variable aleatoria, se le conoce como _camino muestral_ y se entiende como el estado del proceso en el tiempo $t$ (Ross, 1996).

!!! note "Proceso completamente especificado"
    S dice que un proceso estocástico está completamente especificado si para cualquier valor del tiempo $t_1<t_2<\dots<t_n$ con $n \in \mathbb{N}$,la distribución conjunta de $(X_{t_1},X_{t_2},\cdots,X_{t_n})$ es conocida.

De la definición anterior se entiende que es difícil conocer el comportamiento de un proceso estocástico, por lo que en ocasiones se deben imponer ciertas condiciones para su estudio.

!!! note "Procesos con incrementos independientes"
    Se dice que un proceso estocástico tiene _incrementos independientes_ si dados $t_0,t_1,t2,\dots,t_n$ las variables aleatorias $X_{t_1}-X_{t_0},X_{t_2}-X_{t_1},\dots,X_{t_n}-X_{t_{n-1}}$ son independientes.

El siguiente ejemplo muestra un proceso con incrementos independientes.

!!! note "Proceso de Weiner"
    Se dice que el proceso $\lbrace W_t:t \ge 0 \rbrace$ es un _Proceso de Weiner_ si satisface las siguientes condiciones:

    a)    $W_0 = 0$ (El proceso comienza en cero).

    b)    Tiene incrementos independientes.

    c)    $W_t-W_s \sim N(0,C)$ para $0<s<t$.

!!! note "Movimiento Browniano"
    Este proceso también recibe el nombre de _movimiento browniano_ debido a que el biólogo R. Brown en 1827 observó que algunas partículas en el agua exhibían movimiento irregulares (Karlin & Taylor, 1975).

Un resultado interesante de este proceso es que los incrementos son independientes y estacionarios y su varianza depende de $t$. Es decir:

\(W_{t-s}=W_{t-s}-W_0 \sim N(0,\sigma^2(t-s))\)

es igual es distribución que $W_t-W_s$, donde $\sigma^2$ es la varianza del proceso en el tiempo 1.

??? example "Varianza del incremento del proceso de Weiner"
    Para calcular la varianza de los incrementos, se puede proceder con la fórmula de la varianza, teniendo en cuenta que la esperanza de las diferencias es cero.

    \(
    \begin{align*}
    \mathbb{V}(W_t-W_s) &= \mathbb{E}\left( (W_t-W_s)^2\right)\\
    &=\mathbb{E}\left( W_t^2 -2 W_t W_s +W_s^2\right)\\
    &=\mathbb{E}(W_t^2)-2\mathbb{E}(W_t W_s)+\mathbb{E}(W_s^2)
    \end{align*}
    \)

    Para calcular $\mathbb{E}(W_t W_s)$, se puede realizar un "truco" expresando $W_t = (W_t -W_s) + W_s$ y $W_s = W_s-W_0$, por lo que

    \(
    \begin{align*}
    \mathbb{E}( W_s W_t) &= \mathbb{E}( (W_s-W_0) ((W_t -W_s) + W_s))\\
    &=\mathbb{E}((W_s-W_0)(W_t-W_s)+W_s^2)\\
    &=\mathbb{E}((W_s-W_0)(W_t-W_s))+\mathbb{E}(W_s^2)\\
    &=\mathbb{E}((W_s-W_0))\mathbb{E}((W_t-W_s))+\mathbb{E}(W_s^2)\\
    &=\mathbb{E}(W_s^2)
    \end{align*}
    \)

    Entonces, la varianza del los incrementos es

    \(
    \begin{align*}
    \mathbb{V}(W_t-W_s) &= \mathbb{E}(W_t^2)-2\mathbb{E}(W_s^2)+\mathbb{E}(W_s^2)\\
    &= \mathbb{E}(W_t^2)-\mathbb{E}(W_s^2)\\
    &= \mathbb{V}(W_t)-\mathbb{V}(W_s)
    \end{align*}
    \)

    Ahora supóngase que $s=1$ y $t>1$ y $\mathbb{V}(W_1)=\sigma^2$. Entonces necesariamente la varianza en el tiempo será $t-1$ será la constante $\sigma^2$ por la diferencia de $t-1$. Por lo tanto $\mathbb{V}(W_t-W_s)=\sigma^2(t-s)$ es una función lineal que depende de $t$ y $s$.

## Bibliografía

Ross, S. M. (1996). __Stochastic Processes__ (Second Edition). John Wiley & Sons.

Karlin, S., & Taylor, H. (1975). __A first course in stochastic processes__ (Second Edition). Academic Press.

> Muchas de las ideas fueron tomadas del curso _Procesos estocásticos_ impartido por el Dr. José Villaseñor en Primavera del 2022 en el Colegio de Postgraduados, Campus Montecillo.
