---
title: Inferencia estadística
summary: Introducción a la teoría estadística en donde se abarcan temas de propiedades de los estimadores puntuales y por intervalos.
authors: Francisco Vázquez
date: 2021-09-10
---

# Introducción

En la vida real quisiéramos estimar valores aproximados de características de interés de una población, por ejemplo la temperatura promedio de cierto lugar.

Sería conveniente tener _fórmulas generales_ para poder estimar algo desconocido únicamente utilizando información obtenida a partir de la observación de fenómenos; quisiéramos que esas _fórmulas generales_ sean buenas y que se pudieran utilizar con otros datos. Por ello en este documento se detalla la forma en obtener estimadores de los parámetros poblacionales que son de interés.

## Propiedades deseables de los estimadores

Supóngase que \(\mathbf{X}=( X_1,X_2,\ldots,X_n )\) es una muestra aleatoria de una densidad \(f_X(x;\theta)\) conocida, la cual depende de un parámetro desconocido [^1] \(\theta\), aunque sabemos que \(\theta\) pertenece a un espacio de parámetros \(\Theta\). Si únicamente conocemos la muestra aleatoria (observaciones), \(\mathbf{x}\) que representan una realización de \(\mathbf{X}\), ¿Cuál es el valor aproximado de \(\theta\)?.

[^1]: Por ahora se considerará que \(\theta\) es de dimensión uno, aunque podría ser un vector de parámetros.
