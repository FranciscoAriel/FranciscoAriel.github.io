---
title: Modelos Lineales Generalizados
summary: Introducción a modelos lineales cuya variable respuesta no es normal.
author: Francisco Vázquez
date: 2022-10-11
author_gh_user: FranciscoAriel
publish_date: 2022-10-11
read_time: 15 minutos
---

## Introducción

Los modelos lineales generalizados (MLG) son una poderosa herramienta para el análisis de datos, cuya característica principal es que la variable respuesta no necesariamente es normal, por lo que se extiende a varias distribuciones.

Un caso particular de estos modelos es el modelo de regresión lineal, aunque también lo son la regresión Poisson o regresión Logística.

A continuación se definirá a los modelos lineales generalizados.

!!! note "Definición"
    Sean $Y_1,Y_2,\dots,Y_n$ variables aleatorias independientes con distribución $f_{Y}(y_i;\theta_i)=e^{y_i b(\theta_i)+c(\theta_i)+d(y_i)}$. Entonces se tienen las siguientes características:

    1) $f_Y(y_i;\theta_i)$ pertenece a la familia exponencial.

    2) Si $E(Y_i)=\mu_i$, con $h(\theta_i)=\mu_i$, entonces $g(\mu_i)=\mathbf{X\beta}$.

    3) $g$ es una función monótona y diferenciable y se le conoce como _función enlace_.

Note que $g(\mu_i)$ es explicada de forma lineal por covariables $X_j,j=1,2,\dots,p<n$ a través de parámetros $\beta_0, \beta_1,\dots,\beta_p$, por lo que estos parámetros son de interés.

## Estimación

Usando el supuesto de que 
