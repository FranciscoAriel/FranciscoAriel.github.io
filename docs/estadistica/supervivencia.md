---
title: Análisis de supervivencia
summary: Estudio de variables de vida, incluyendo información censurada.
author: Francisco Vázquez
date: 2022-09-09
author_gh_user: FranciscoAriel
publish_date: 2022-09-09
read_time: 15 minutos
---

El análisis de supervivencia se basa en el estudio de variables de vida, por lo que se utilizan variables aleatorias con valores positivos. El nombre se debe a que en Medicina, se llevan a cabo estudios con pacientes en los cuales es de interés estimar el tiempo de _supervivencia_ a una enfermedad.

El análisis de superivencia es usado en otras disciplinas aunque tiene otros objetivos, tales como:

- **Entomología:** Modela el tiempo en que fallecen insectos al aplicárseles un insecticida.
- **Meteorología:** Tiempo en que aparecen los huracanes.
- **Actuaría:** Tiempo entre incidentes.
- **Ingeniería:** (conocido como _confiabilidad_) Tiempo en que aparece una falla.

Aunque es común estudiar variables aleatorias relacionadas al _tiempo entre eventos_, es posible estudiar otras variables relacionadas, por ejemplo distancia o cualquier variable que tome valores positivos. A la ocurrencia de los eventos de interes se les llama también como _fallos_ (failures).

Un problema común en datos de tiempo de vida es la presencia de _censura_ y/o _truncamiento_. Debido a esta problemática, es necesario desarrollar teoría y métodos que puedan lidiar con este problema, en la [sección 3](#inferencia-paramétrica-con-datos-censurados) se estudiará este problema de forma detallada.

## Modelos de tiempo de vida

En análisis de supervivencia se usan conceptos que hasta ahora no habían sido descritos, aunque son similares a los que se usan en probabilidad. A continuación se dará una breve definición de ellos.

!!! note "Función de Supervivencia"
    Sea $T$ una variable aleatoria con soporte en los reales positivos.

    \(S(t) = P(T > t) = 1 - F_T(t)\)

    La función de supervivencia se interpreta como la probabilidad de que un individuo sobreviva más que tiempo que $t$.

Esta definición es muy importante y frecuentemente el objetivo será estimarla.

!!! note "Función de riesgo"
    Sea $T$ una variable aleatoria positiva. La función de riesgo $h(t)$ se define como la probabilidad de un individuo muera en un intervalo de tiempo pequeño _dado_ que ha sobrevivido al tiempo $t$.

    Si $T$ es continua, entonces $h(t) = \frac{f(t)}{S(t)}=-\frac{\partial}{\partial t}\log S(t)$.

En diversas aplicaciones, por ejemplo para determinar la garantía de un producto, es de interés conocer la función de riesgo,

!!! note "Función de riesgo acumulado"
    La función de riesgo acumulado $H(t)$ se define como:

    \(H(t)=\int_{0}^{t}h(s)ds=-\log S(t) \)

    Por lo que $S(t) = e^{-H(t)}$

!!! note "Relación entre la función de supervivencia y de riesgo acumulado"
    Si $T$ es una variable aleatoria discreta, entonces

    \(
    \begin{align}
    S(t) &= P(T > t)\\
    & = P(T > a_1) \times P(T>a_2|T>a_1)\times \dots \times P(T>a_k|T>a_{k-1})\\
    & = (1-h_1)\times \dots \times (1-h_k)\\
    & = \prod_{a_i \le t} (1-h_i)
    \end{align}
    \)

## Inferencia paramétrica con datos censurados

## Estimación no paramétrica

## Comparación de curvas de supervivencia

## Modelo de riesgos proporcionales

## Extensiones
