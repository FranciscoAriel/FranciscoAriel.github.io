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

Aunque es común estudiar variables aleatorias relacionadas al _tiempo entre eventos_, es posible estudiar otras variables relacionadas, por ejemplo distancia o cualquier variable que tome valores positivos.

## Modelos de tiempo de vida

En análisis de supervivencia se usan conceptos que hasta ahora no habían sido descritos, aunque son similares a los que se usan en probabilidad. A continuación se dará una breve definición de ellos.



