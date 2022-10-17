---
title: Modelos Lineales Generalizados
summary: Introducción a modelos lineales cuya variable respuesta no es normal.
author: Francisco Vázquez
date: 2022-10-11
author_gh_user: FranciscoAriel
publish_date: 2022-10-11
read_time: 35 minutos
---

## Introducción

Los modelos lineales generalizados (MLG) son una poderosa herramienta para el análisis de datos, cuya característica principal es que la variable respuesta no necesariamente es normal, por lo que se extiende a varias distribuciones.

Un caso particular de estos modelos es el modelo de regresión lineal, aunque también lo son la regresión Poisson o regresión Logística.

A continuación se definirá a los modelos lineales generalizados.

!!! note "Definición"
    Sean $Y_1,Y_2,\dots,Y_n$ variables aleatorias independientes con distribución $f_{Y}(y_i;\theta_i)=e^{y_i b(\theta_i)+c(\theta_i)+d(y_i)}$. Entonces se tienen las siguientes características:

    1) $f_Y(y_i;\theta_i)$ pertenece a la [familia exponencial](inferencia.md#la-familia-exponencial).

    2) Si $E(Y_i)=\mu_i$, con $h(\theta_i)=\mu_i$, entonces $g(\mu_i)=\eta_i$.

    3) $g$ es una función monótona y diferenciable y se le conoce como _función enlace_.

Note que $g(\mu_i)$ es una función del predictor lineal $\eta_i=\beta_0+\beta_1X_{i1}+\dots+\beta_p X_{ip}$ el cual está formado por por covariables $X_j,j=1,2,\dots,p<n$ y parámetros desconocidos $\beta_0, \beta_1,\dots,\beta_p$, por lo que estos parámetros son de interés.

A continuación se presentan algunos ejemplo de los modelos lineales generalizados más usados en estadística.

??? example "Modelo de regresión lineal"
    El modelo de regresión lineal puede considerarse como un caso particular de un modelo lineal generalizado, ya que cumple con las 3 características descitas anteriormente.

    1) $Y_i \sim N(\mu_i,\sigma^2)$ (La distribución normal pertenece a la familia exponencial).
    
    2) $E(Y_i)=\mu_i=\beta_0+\beta_1X_{i1}+\dots+\beta_p X_{ip}$ (El valor esperado de $Y_i$ es el predictor lineal).

    3) $g(\mu_i)=\mu_i$ (función enlace identidad).

??? example "Modelo de regresión logística"
    El modelo de regresión logística tambien es considerado un caso particular de un modelo lineal generalizado, este modelo es usado para modelar probabilidades de éxito con variable respuesta binaria o de conteos.

    1) $Y_i \sim Ber(p_i)$ para datos con respuesta binaria o $Y_i \sim Bin(n_i,p_i)$ para datos agrupados.

    2) $\log \left(\frac{p_i}{1-p_i}\right)=\beta_0+\beta_1X_{i1}+\dots+\beta_p X_{ip}$

    3) La función _logit_ es monótona (es la inversa de la [función logística](https://es.wikipedia.org/wiki/Funci%C3%B3n_log%C3%ADstica)).

??? example "Modelo de regresión Poisson"
    Otro modelo que puede considerarse un caso particular de los modelos lineales generalizados es la regresión Poisson.

    1) $Y_i \sim Poi(\lambda_i)$.

    2) $\log \lambda_i = \beta_0+\beta_1X_{i1}+\dots+\beta_p X_{ip}$.

    3) $g$ es monótona (La inversa de la función logaritmo es la función exponencial).

## Estimación

Usando el supuesto de que las observaciones son independientes, es posible construir la función de verosimilitud

$$L(\theta_i|\mathbf{x},y)=e^{\sum_{i=1}^n y_i b(\theta_i)+c(\theta_i)+d(y_i)}$$

sin embargo en ocasiones es preferible trabajar con la función de log-verosimilitud.

$$l(\theta_i|\mathbf{x},y)=\sum_{i=1}^n y_i b(\theta_i)+\sum_{i=1}^n c(\theta_i)+\sum_{i=1}^n d(y_i)$$

Las estimaciones de los parámetros se obtienen maximizando esa función. En general, no es posible encontrar una solución analítica cerrada de la función de log-verosimilitud.

A continuación se muestran algunos métodos para la estimación de parámetros.

### Método de Scoring

Este método puede ser considerado como una variante del método de Newton-Raphson, en el cual los parámetros se estiman de forma iterativa

\(\theta^{(i+1)}=\theta^{(i)}+\mathbf{I}\left(\theta^{(i)}\right)^{-1}\mathbf{U}\left(\theta^{(i)}\right)\)

donde $\mathbf{U}=\frac{\partial l(\theta|\mathbf{x},y)}{\partial \theta}$ es conocido como vector _score_ o gradiente y $\mathbf{I}=-E\left(\frac{\partial^2 l(\theta|\mathbf{x},y)}{\partial \theta^2}\right)$ es la información.

Note que si no se tienen covariables, este método puede ser usado directamente para estimar a $\theta_i$ como se muestra en el siguiente ejemplo.

### Mínimos cuadrados ponderados iterativos

Para los modelos lineales generalizados, el vector _score_ puede escribirse como

\(
\mathbf{U}= \left(U_j\right), j=1,\dots,p
\)

donde $U_j=\sum_{i_1}^n\frac{(y_i-\mu_i)}{Var(Y_i)}x_{ij}\frac{\partial \mu_i}{\partial \eta_i}$ y la matriz de Información como

\(
\mathbf{I}=\lbrace I_{jk} \rbrace, j,k=1,\dots,p
\)

donde $I_{jk}=\frac{x_{ij}x_{ik}}{Var(Y_i)}\left(\frac{\partial \mu_i}{\partial \eta_i}\right)^2$. Vea el capítulo 4 de (Dobson & Barnett, 2008) para mayores detalles.

Usando las ecuaciones del método de Scoring se tiene que

\(
\begin{align*}
\mathbf{b}^{(i+1)}&=\mathbf{b}^{(i)} + \left(\mathbf{I}^{(i)}\right)^{-1}\mathbf{U}^{(i)}\\
\mathbf{I}^{(i)}\mathbf{b}^{(i+1)}&=\mathbf{I}^{(i)}\mathbf{b}^{(i)} + \mathbf{U}^{(i)}
\end{align*}
\)

donde $\mathbf{b}$ es un vector que contiene estimaciones de los parámetros de interés.

Note que la información puede expresarse de forma matricial como $\mathbf{I}=\mathbf{X}^t\mathbf{W}\mathbf{X}$, donde $\mathbf{W}$ es una matriz diagonal de dimensión $n \times n$ con elementos $w_i=\frac{1}{Var(Y_i)}\left(\frac{\partial \mu_i}{\partial \eta_i}\right)^2$, también se puede construir un vector $\mathbf{z}$ con elementos $z_i=\sum_{k=1}^{p}x_{ik}b_k^{(i)}+(y_i-\mu_i)\left(\frac{\partial \mu_i}{\partial \eta_i}\right)$, por lo que las ecuaciones se pueden representar como

\(
\mathbf{X}^t\mathbf{W}\mathbf{X}\mathbf{b}^{(i+1)}=\mathbf{X}^t\mathbf{W}\mathbf{z}
\)

Estas ecuaciones son similares a las ecuaciones normales, aunque deben ser resueltas de forma iterativa ya que $\mathbf{z}$ y $\mathbf{W}$ dependen del valor de $\mathbf{b}$ anterior.

La mayoría de los softwares estadísticos emplean este método cuando estiman los parámetros por máxima verosimilitud.

## Inferencia

En estadística no sólo es importante obtener estimaciones de parámetros, sino también es de interés hacer inferencia ya sea sobre valores futuros o realizar pruebas de hipótesis o de bondad de ajuste con el fin de verificar si el modelo propuesto es válido o no para un conjunto de datos.

Debido a que es complicado obtener las distribuciones exactas de muchas cantidades de interés, se suele recurrir a la teoría asintótica. A continuación se muestran algunos resultados de interés.

### Estadística Score

!!! note "Distribución muestral para la estadística Score"
    Sea $Y_1,Y_2,\dots,Y_n$ variables aleatorias independientes y sea $\mathbf{U}$ la estadística score y $\mathbf{I}$ la matriz de información, entonces __asintóticamente__

    - $\mathbf{U} \sim N_p \left(\mathbf{0},\mathbf{I}\right)$
    - $\mathbf{U}^T\mathbf{I}^{-1}\mathbf{U} \sim \chi_{p}^2$

### Estadística de Wald

!!! note "Estadística de Wald"
    Sea $\hat{\beta}=(\hat{\beta}_0,\hat{\beta}_1,\dots,\hat{\beta}_p)^t$ el estimador de máxima verosimilitud de $\beta=(\beta_0,\beta_1,\dots,\beta_p)^t$. Por las [propiedades del estimador de máxima verosimilitud](inferencia.md#estimadores-de-máxima-verosimilitud), la distribución asintótica es:

    - $(\hat{\beta}-\beta)^{T}\mathbf{I}^{-1}(\hat{\beta})(\hat{\beta}-\beta)\sim \chi_{p}^2$

### Estadística de razón de verosimilitudes

Una forma de medir la bondad de ajuste de un modelo, es compararlo con el _modelo saturado_, el cual tendrá $n$ parámetros y en teoría tendría el mejor ajuste posible. La idea es comparar si el modelo ajustado está cerca o lejos del modelo saturado.

Para ello se usa la _devianza_ definida como $D=2\left(l(\beta_m)-l(\hat{\beta})\right)$, donde $l(\beta_m)$ es la verosimilitud evaluada en los parámetros del modelo saturado y $l(\hat{\beta})$ es la verosimilitud evaluada en el estimador de máxima verosimilitud.

!!! note "Distribución muestral de la devianza"
    La distribución muestral de la devianza asintótica es:

    \(D\sim\chi_{n-p,v}^2\)

    donde $v$ es el parámetro de no centralidad y $p$ el número de parámetros del modelo.

A continuación se muestran algunos ejemplos del cálculo de la devianza para algunos modelos

??? example "Devianza en el modelo Poisson"
    Sea $Y_1,\dots,Y_n$ una muestra aleatoria con $Y_i\sim Poi(\lambda_i)$. Note que el modelo completo es aquel que tenga tantos parámetros como observaciones. Para encontrar un estimador de $\lambda_i$ se puede usar la primer derivada de la función de log-densidad e igualar a cero.

    \(
        \begin{align*}
        0&=\frac{\partial}{\partial \lambda_i}\log e^{y_i \log \lambda_i -\lambda_i -\log y_i!}\\
        &=\frac{\partial}{\partial \lambda_i} y_i \log \lambda_i -\lambda_i -\log y_i! \\
        &=\frac{y_i}{\lambda_i}-1\\
        &=y_i-\lambda_i
        \end{align*}
    \)

    Por lo que $l(\beta_m)=\sum_{i=1}^n y_i \log y_i -y_i -\log y_i!$.

    Por otro lado, $\hat{y}_i$ son los valores estimados con los estimadores de máxima verosimilitud $\hat{\beta}$, asumiendo $\hat{y}_i=\hat{\lambda}_i$, por lo que $l(\hat{\beta})=\sum_{i=1}^n y_i \log \hat{y}_i -\hat{y}_i -\log y_i!$.

    Por lo tanto la devianza puede ser calculada como $D=2\left[\sum_{i=1}^n y_i \log \frac{y_i}{\hat{y}_i}-(y_i-\hat{y}_i) \right]$.

??? example "Devianza en el modelo Binomial"
    Sea $Y_1,\dots,Y_n$ una muestra aleatoria con $Y_i\sim Bin(n_i,p_i)$. Asumiendo $n_i$ conocida, el estimador para $\pi$ puede obtenerse de la siguiente manera:

    \(
    \begin{align*}
    0&=\frac{\partial}{\partial \lambda_i}\log e^{y_i \log \left(\frac{p_i}{1-p_i}\right) + n_i\log (1-p_i)+\log \binom{n_i}{y_i}}\\
    &=\frac{\partial}{\partial p_i} y_i \log \left(\frac{p_i}{1-p_i}\right) + n_i\log (1-p_i)+\log \binom{n_i}{y_i}\\
    &=\frac{y_i}{p_i(1-p_i)}-\frac{n_i}{(1-p_i)}
    \end{align*}
    \)

    Por lo que $\hat{p}_i = \frac{y_i}{n_i}$ y la verosimilitud completa es $l(\beta_m)=\sum_{i=1}^n y_i\log \frac{y_i}{n_i}-y_i\log \frac{n_i-y_i}{n_i} +n_i\log \frac{n_i-y_i}{n_i}+\log \binom{n_i}{y_i}$.

    Los estimadores $\hat{\beta}$ pueden ser usados para estimar $\hat{p}_i$ y con ello es posible estimar $\hat{y}_i=n_i\hat{p}_i$, por lo que $l(\hat{\beta})=\sum_{i=1}^n y_i\log \frac{\hat{y}_i}{n_i}-y_i\log \frac{n_i-\hat{y}_i}{n_i}+n_i\log \frac{n_i-\hat{y}_i}{n_i}+\log \binom{n_i}{y_i}$.

    Por lo tanto, la devianza para el modelo binomial es $D=2\left[\sum_{i=1}^n y_i \log \frac{y_i}{\hat{y}_i}+(n_i-y_i)\log \frac{n_i-y_i}{n_i-\hat{y}_i} \right]$.

Tambien es posible hacer pruebas de hipótesis para verificar si algun coeficiente $\beta_j$ estadísticamente es cero con el fin de tener un modelo más parsimoniso. A estos modelos se les denominan _modelos anidados_.

Por ejemplo, sea $H_0:\beta = \beta_{M_0}=(\beta_0,\beta_1,\dots,\beta_q)$ contra la alternativa $H_a:\beta = \beta_{M_1}=(\beta_0,\beta_1,\dots,\beta_p)$ con $q<p$. Es posible usar la estadística de diferencia de devianzas de los modelos $\Delta D=2\left(l(\beta_{M_1})-l(\hat{\beta_{M_0}})\right)$ para probar dicha hipótesis.

!!! note "Prueba de modelos anidados"
    La distribución muestral de la diferencia de devianza de dos modelos anidados asintótica es:

    \(D\sim\chi_{p-q,v}^2\)

    donde $v$ es el parámetro de no centralidad, $p$ y $q$ el número de parámetros del modelo del modelo 1 y modelo 0 respectivamente.

## Bibliografía

Dobson, A., & Barnett, A. (2008). An Introduction to Generalized Linear Models (Third Edition). CRC Press.
