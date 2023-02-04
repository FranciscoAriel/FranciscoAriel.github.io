---
title: Introducción a la Estadística Bayesiana
summary: Inferencia estadística desde el punto de vista Bayesiano.
author: Francisco Vázquez
date: 2022-05-19
author_gh_user: FranciscoAriel
publish_date: 2022-05-19
read_time: 25 minutos
---

## Introducción

La estadística bayesiana es un paradigma completo de inferencia basado en la *teoría de la decisión* y por lo tanto se basa en los conceptos de probabilidad.

A diferencia del enfoque frecuentista, la estadística bayesiana se basa en el enfoque de *probabilidad subjetiva*. Dicha probabilidad subjetiva es una medida o grado de creencia de qué tan verosímil sea un evento.

Por ejemplo, si le preguntáramos a cada persona sobre la probabilidad de que llueva $\theta$, cada una nos responderá según su creencia o nivel de conocimiento sobre $\theta$. Todo ese conocimiento podría resumirse en una función de distribución que llamaremos *distribución a priori*, denotada $f_\Theta(\theta)$ o $p(\theta)$.

Esta información *a priori* se combina con la *información de los datos* o *verosimilitud*, denotada como $f_{X| \Theta}(x|\theta)$ o $L(\theta|x)$ con el fin de obtener la *distribución a posteriori*, denotada como $f_{\Theta|X}(\theta|x)$ o $p(\theta|x)$ usando la regla de Bayes.

\(
    p(\theta|x)=\frac{p(\theta,x)}{p(x)}=\frac{L(\theta|x)p(\theta)}{p(x)}
\)

!!! abstract "Verosimilitud bajo muestreo aleatorio"
    Sea $X_1,X_2,\dots, X_n \sim f(X_i|\theta)$ una muestra aleatoria.

    Entonces la función de verosimilitud $L(\theta|\mathbf{x})$ se puede representar como:

    $$L(\theta|\mathbf{x}) = \prod_{i=1}^{n}f(X_i|\theta)$$

    Note que en este caso, **es una función que depende del parámetro** ya que los datos ya fueron *observados*.

!!! abstract "Distribución a posteriori"
    La distribución a posteriori puede escribirse como:

    $$p(\theta|\mathbf{x})\propto L(\theta|\mathbf{x})p(\theta) = p(\theta|\mathbf{x})p(\theta)$$

    Note que $p(x)$ es una densidad que _no depende_ de $\theta$ (es considerada una "constante"), por lo cual en estadística bayesiana se utiliza el símbolo $\propto$ para denotar que la distribución _a posteriori_ es _proporcional_ a $L(\theta|\mathbf{x})p(\theta)$.

El siguiente ejemplo ilustra una forma de obtener la distribución a posteriori.

??? example "Lanzamiento de una moneda 1"
    Suponga que se tiene una moneda y se realizan 10 lanzamientos. Sea $\theta$ la probabilidad de que caiga águila, mientras que $1-\theta$ es la probabilidad de que caiga sol. No se tiene información acerca del comportamiento de la moneda, pero se sospecha es una moneda honesta. Supóngase que se han observado 7 águilas.

    Debido a que no se tiene información sobre $\theta$, se pude asumir una función de distribución uniforme en el intervalo [0,1], esto es: $p(\theta)=I_{(0,1)}(\theta)$.

    Note que los datos pueden ser modelados mediante la verosimilitud, es decir $p(\mathbf{x}|\theta)=L(\theta|\mathbf{x})=\prod_{i=1}^{n}\theta^{x_i}\left(1-\theta\right)^{1-x_i}=\theta^{\sum_{i=1}^{n}x_i}\left(1-\theta\right)^{n-\sum_{i=1}^{n}x_i}$.

    Sustituyendo

    \(p(\theta|x)\propto \theta^{7}\left(1-\theta\right)^{3}I_{(0,1)}(\theta)\)

    Note que como tal, **no es una función de densidad**, debido a que la integral no es 1, sin embargo, es proporcional a una función de densidad beta con parámetros 8 y 4.

    Por lo tanto, la distribución *a posteriori* es $p(\theta|x)=\frac{\theta^{8-1} \left(1-\theta\right)^{4-1}}{B(8,4)}I_{(0,1)}(\theta)$.

!!! note "Densidad conjugada"
    Se dice que $p(\theta)$ es conjugada con $L(\theta|x)$ si $p(\theta|x)$ es de la misma familia que $p(\theta)$.

En el ejemplo anterior se pudo observar que la distribución Beta(1,1) es conjugada con la verosimilitud Bernoulli.

## Teoría Bayesiana

### Intervalos

### Factor de Bayes

## Modelo Normal

Una de las distribuciones más utilizadas en estadística es la normal, debido a que no solo muchos fenómenos tiene un comportamiento similar, sino por que los promedios tienden a una distribución normal.

En esta sección se usará esta distribución para hacer inferencia sobre los parámetros de interés usando estadística Bayesiana.

### Inferencia sobre la media (Modelo Normal - Normal)

Debido a que la distribución Normal es ampliamente utilizada en estadística, se ilustrarán algunas de propiedades de la distribución _a posteriori_ de la media $\mu$.

El siguiente ejemplo ilustra cómo obtener la distribución posterior de la media $\mu$ asumiendo varianza conocida y distribución _a priori_ para la media una distribución normal.

??? example "Derivación de la distribución posterior para la media"
    Suponga que se tiene una muestra aleatoria $X_1,X_2,\dots, X_n \sim N(\mu,\sigma^2)$ con $\sigma^2$ conocida. Se propone utilizar una distribución _a priori_ normal para $\mu$, es decir $\mu \sim N(\mu_0,\sigma_0^2)$, donde $\mu_0$ y $\sigma_0^2$ son conocidos.

    La distribución a posteriori puede encontrarse de la siguiente manera:

    $$p(\mu|\mathbf{x}) \propto L(\mu|\mathbf{x})p(\mu)$$

    Note que la verosimilitud puede expresarse como: 
    
    $$
    \begin{align*}
    L(\mu|\mathbf{x}) &= \prod_{i=1}^{n}\left(\frac{1}{2 \pi \sigma^2}\right)^{\frac{1}{2}}e^{\frac{1}{2\sigma^2}(x_i-\mu)^2}\\
    &=\left(\frac{1}{2 \pi \sigma^2}\right)^{\frac{n}{2}}e^{\frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i-\mu)^2}\\
    &\propto e^{\frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i-\mu)^2}
    \end{align*}
    $$

    Usando la suma de cuadrados $\sum_{i=1}^{n}(X_i-\mu)^2 =n(\bar{X}-\mu)^2 + \sum_{i=1}^{n}(X_i-\bar{X})^2$, se propone usar $L(\mu|\mathbf{x}) \propto e^{-\frac{n}{2\sigma^2}(\mu-\bar{x})^2}$ ya que la exponencial es una función _simétrica_.
    
    Al usar $p(\mu) \propto e^{-\frac{1}{2\sigma_0^2}(\mu-\mu_0)^2}$, por lo tanto la distribución _a posteriori_ es:

    $$
    \begin{align*}
    p(\mu|\mathbf{x}) &\propto e^{-\frac{n}{2 \sigma^2}(\mu-\bar{x})^2} e^{-\frac{1}{2 \sigma_0^2}(\mu-\mu_0)^2}\\
    &\propto e^{-\frac{1}{2}\left(\frac{n}{\sigma^2}\left(\mu^2-2\mu \bar{x}+\bar{x}^2\right)+\frac{1}{ \sigma_0^2}\left(\mu^2-2\mu \mu_0 +\mu_0^2\right)\right)}\\
    &\propto e^{-\frac{1}{2}\left(\frac{n}{\sigma^2}\left(\mu^2-2\mu \bar{x}\right)+\frac{1}{ \sigma_0^2}\left(\mu^2-2\mu \mu_0\right)\right)}\\
    &\propto e^{-\frac{1}{2}\left(\mu^2\left(\frac{n}{\sigma^2}+\frac{1}{\sigma_0^2}\right)-2\mu \left(\frac{n \bar{x}}{\sigma^2} + \frac{\mu_0}{\sigma_0^2} \right)\right)}\\
    &\propto e^{-\frac{1}{2 V}(\mu-M)^2}
    \end{align*}
    $$

    Por lo que se concluye que $\mu|\mathbf{x} \sim N \left(M,V \right)$, donde $V = \frac{n}{\sigma^2}+\frac{1}{\sigma_0^2}$ y $M = \frac{\frac{n }{\sigma^2}\bar{x}+\frac{1}{\sigma_0^2}\mu_0}{V}$

Del ejemplo anterior, se puede deducir el siguiente teorema:

!!! note "Distribución normal posterior"
    Sea $X_1,X_2,\dots, X_n \sim N(\mu,\sigma^2)$ una muestra aleatoria con $\sigma^2$ conocida y $\mu \sim N(\mu_0,\sigma_0^2)$. Entonces se cumplen las siguientes propiedades.

    - La distribución _a posteriori_ es conjugada.
    - $E(\mu|\mathbf{x}) = p_1\bar{x} + p_2\mu_0$ es un promedio ponderado de la media _a priori_ y el _estimador de máxima verosimilitud_, cuyos pesos son proporcionales a la suma del inverso de las varianzas.
    - Cuando $n \to \infty$ la media _a posteriori_ coincide con el estimador de máxima verosimilitud.
    - Si $p(\mu) \propto 1$, entonces $p(\mu|\mathbf{x}) = N\left(\bar{x},\frac{\sigma^2}{n}\right)$ coincide con el resultado frecuentista que asume varianza conocida.

Esta propiedad será usada posteriormente para obtener de manera fácil distibuciones posteriores, por ejemplo en un modelo lineal.

Finalmente es de interés encontrar la distribución _predictiva a posteriori_ para este modelo.

$$p(X_{n+1}|x_1,\dots,x_n) = N\left(\bar{x},\left(1+\frac{1}{n}\right)\sigma^2\right)$$

El siguiente ejemplo muestra detalles para hallar dicha distribución.

??? example "Derivación de la distribución predictiva"
    Asumiendo que $X_{n+1}$ tambien proviene de la misma población, se tiene que

    $$
    \begin{align*}
    p(X_{n+1} |\mathbf{x}) &\propto \int_{-\infty}^{\infty} p(x_{n+1}|\mu) p(\mu|\mathbf{x}) d \mu\\
    &\propto \int_{-\infty}^{\infty} e^{\frac{-1}{2\sigma^2}\left(n(\mu-\bar{x})^2+(x_{n+1}-\mu)^2\right)}d\mu
    \end{align*}
    $$

    Note que $Q(\mu)=n(\mu-\bar{x})^2+(x_{n+1}-\mu)=(n+1)(\mu-\bar{x}_{n+1})^2+\frac{n}{n+1}(x_{n+1}-\bar{x})^2$, donde $\bar{x}_{n+1}=\frac{n\bar{x}+x_{n+1}}{n+1}$, por lo que:

    $$
    \begin{align*}
    p(x_{n+1} |\mathbf{x}) & \propto e^{\frac{-1}{2\sigma^2}\left(\frac{n}{n+1}(x_{n+1}-\bar{x})^2\right)} \int_{-\infty}^{\infty} e^{\frac{-1}{2\sigma^2}\left((n+1)(\mu-\bar{x}_{n+1})^2\right)}d\mu\\
    &\propto e^{\frac{-n}{2(n+1)\sigma^2}\left(x_{n+1}-\bar{x}\right)^2}
    \end{align*}
    $$

    Por lo tanto $X_{n+1}|\mathbf{x} \sim N\left(\bar{x},(1+\frac{1}{n})\sigma^{2}\right)$.

!!! note "Reparametrización de la varianza"
    Algunos autores, por ejemplo Hoff (2009), recomiendan reparametrizar la distribución normal usando la precisión que es la inversa de la varianza.

    La ventaja de esta reparametrización es que es más fácil hacer cálculos con la precisión que con la varianza, ya que se evitan hacer suma de fracciones. Sin embargo las conclusiones son las mismas.

    En la siguiente sección se hará uso de la precisión para facilitar los cálculos.

### Inferencia sobre la media y varianza (Modelo Normal - Gamma)

En la sección anterior se hizo inferencia únicamente sobre la media $\mu$, asumiendo la varianza $\sigma^2$ conocida. Ahora se considerará inferencia sobre ambos parámetros, es decir $\theta = (\mu, \sigma^2)´$.

El objetivo será encontrar la distribución _a posteriori_ de $\theta$ dados los datos $\mathbf{x}$, es decir:

$$p(\theta|\mathbf{x}) \propto L(\theta|\mathbf{x})p(\theta)$$

Se puede proponer una densidad _a priori conjunta_, la cual sea producto de una _condicional_ y una marginal.

$$p(\mu,\sigma^2) = p(\mu|\sigma^2)p(\sigma^2)$$

o en términos de precisión $\tau=\frac{1}{\sigma^2}$:

$$p(\mu,\tau) = p(\mu|\tau)p(\tau)$$

La distribución a priori propuesta es la siguiente:

!!! abstract "Distribución Normal-Gama"
    Se dice que la densidad conjunta $p(\mu,\tau)$ es Normal-Gama(m,c,a,b) si:

    - $p(\tau) = Ga(a,b)$, donde $a$ es el parámetro de forma y $b$ es parámetro de tasa (inverso de la escala).
    - $p(\mu|\tau) = N\left(m,\frac{1}{c\tau}\right)$ donde $m$ es la media a priori y la varianza es $\sigma^2=\frac{1}{c\tau}$.
    - $p(\mu,\tau) \propto \tau ^{a-\frac{1}{2}-1}e^{-\frac{\tau}{2}(c(\mu-m)^2+2b)}$

!!! tip "Usando la varianza"
    Se puede usar la varianza, sin embargo la distribución _a priori_ sería la Normal-Inversa Gama y los resultados serían similares a los anteriores.
    
    Si $\tau = \frac{1}{\sigma^2} \sim Ga(a,b)$, entonces $p(\sigma^2) \sim IGa(a,b)$, es decir Inversa-Gama. Se puede encontrar más información de esta densidad en este [link](https://en.wikipedia.org/wiki/Inverse-gamma_distribution).

Se puede mostrar que la distribución _a posteriori_ tiene la siguiente forma:

$$p(\mu,\tau|\mathbf{x}) \propto \tau ^ {\frac{n}{2}+a+\frac{1}{2}-1}e^{-\frac{\tau}{2}((n-1)S^2 + 2b + (n+c)(\mu-m_n)^2+\frac{nc}{n+c}(\bar{X}-m)^2)}$$

donde $m_n = \frac{n\bar{x}+cm}{n+c}$. Esta densidad no tiene forma conocida. Sin embargo comunmente es de interés conocer la distibución _condicional posterior_ de $\mu$ dada la precisión $\tau$ y los datos. 

!!! note "Inferencia en el modelo Normal-Gama"
    Sea $X_1,X_2,\dots, X_n \sim N(\mu,\sigma^2)$ una muestra aleatoria con $\tau = \frac{1}{\sigma^2}$ y $p(\mu,\tau) = NG(m,c,a,b)$. Entonces se cumplen las siguientes propiedades.

    - $\mu|\tau,\mathbf{x} \sim N\left(m_n,\frac{1}{\tau (n+c)}\right)$ con $m_n = \frac{n\bar{x}+cm}{n+c}$.
    - $\tau|\mathbf{x} \sim Ga\left(\frac{n-1}{2},\frac{n-1}{2}S^2\right)$ o equivalentemente $\sigma^2|\mathbf{x} \sim iGa\left(\frac{n-1}{2},\frac{n-1}{2}S^2\right)$ con $S^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i-\bar{X})^2$.
    - $\mu|\mathbf{x} \sim t_{n-1}\left(\bar{x},\frac{S^2}{n}\right)$ o equivalentemente $\frac{\sqrt{n}(\mu-\bar{x})}{S}|\mathbf{x} \sim t_{n-1}$.
    - $X_{n+1}|\mathbf{x} \sim t_{n-1}\left(\bar{x},(1+\frac{1}{n})S^2\right)$ o equivalentemente $\frac{(X_{n+1}-\bar{x})}{\sqrt{(1+\frac{1}{n})S^2}}|\mathbf{x} \sim t_{n-1}$.

No es difícil mostrar que:

$$p(\mu|\tau,\mathbf{x}) \propto e^{-\frac{\tau}{2}(n+c)(\mu-m_n)^2}$$

por lo que $\mu|\tau,\mathbf{x} \sim N\left(m_n,\frac{1}{\tau (n+c)}\right)$ o equivalentemente $\mu|\sigma^2,\mathbf{x} \sim N(m_n,\sigma^2 (n+c))$.

Sin embargo obtener las otras distribuciones requiere algunos conocimiento de cálculo integral.

## Modelo Lineal Normal

### Análisis de Referencia

## Métodos numéricos

### Métodos MCMC

### Metropolis - Hastings

### Muestreo de Gibss

## Referencias

Hoff, Peter. 2009. _A First Course in Bayesian Statistical Methods_. New York: Springer.

> Muchas de las ideas fueron tomadas del curso _Análisis Bayesiano_ impartido por el Dr. Sergio Pérez en el cuatrimestre Verano de 2022 en el Colegio de Postgraduados, Campus Montecillo.
