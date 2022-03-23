---
title: Introducción a las Series de Tiempo
summary: Introducción a las series de tiempo, definiciones y ejemplos.
author: Francisco Vázquez
date: 2022-01-26
author_gh_user: FranciscoAriel
publish_date: 2022-01-26
read_time: 15 minutos
---

Las series de tiempo es una de la metodologías estadísticas más aplicada debido a que usualmente se tiene información histórica que se desea estudiar y se usan en diversos campos del conocimiento, por ejemplo en economía. Sin embargo actualmente es común encontrar aplicaciones en prácticamente cualquier área.

Uno de los principales usos de las series de tiempo, es hacer *pronósticos de valores futuros* de la variable de interés, usando la información disponible.

![Representación de una serie en los negocios](img/stock.jpg)
Imagen de [geralt](https://pixabay.com/es/users/geralt-9301/) en [pixabay](https://pixabay.com/).

## Herramientas de exploración de series de tiempo

En series de tiempo, es muy importante conocer el tipo de información que se está utilizando, debido a que los datos suelen tener comportamientos complejos, por lo que conviene tener la mayor información del fenómeno que se está estudiando.

A continucación se describirán algunos métodos que describen el problema.

### Gráfica de series de tiempo

La principal herramienta que se usará será una gráfica de series de tiempo.

Esta consiste en graficar en el eje $X$ el tiempo y en el eje $Y$ las observaciones de la serie.

Esta gráfica nos permitirá ver el comportamiento del fenómeno a través del tiempo e identificar visualmente algunos de sus componentes con el fin de elegir el método más adecuado.

### Estadísticas descriptivas

Las estadísticas descriptivas son de gran autilidad para conocer la distribución de la serie. Valores como la media, mediana, desviación estándar, mínimo o máximo, nos ayudarían a tener una idea del comportamiento de la serie.

Tambíen es recomendable realizar algunos gráficos que nos permitan visualizar su distribución tales como histogramas o diagrama de caja y bigotes (boxplot). En algunos casos, estos gráficos incluso podrían identificar si hay o no dos poblaciones.

### Descomposición de una serie de tiempo

### Métodos de suavizamiento

### Identificación de puntos de quiebre

## Introducción y definición

En esta sección se dará una introducción más formal que nos permitirá estudiar más a fondo las series de tiempo.

!!! note "Definición"
    Una serie de tiempo $X_t$, es una secuencia de valores numéricos indexados por una variable, generalmente tiempo $t$.

Las series de tiempo pueden ser continuas o discretas. Comunmente en ciencias sociales o economía, las series de tiempo estan medidas en intervalos de tiempo regulares, ya sea de manera anual, trimestral, mensual o diaria.

Las series de tiempo pueden ser consideradas un caso particular de los procesos estocásticos en donde el parámetro o índice $t$ es discreto. Para una revisión más completa de estos conceptos, visite la sección [Procesos estocásticos](procesos_estocasticos.md).

Un concepto muy importante en el estudio de las series de tiempo es la _estacionariedad_ (tambien puede revisarse la sección [introducción a los procesos estocásticos](procesos_estocasticos.md#definiciones)).

!!! note "Serie de tiempo estacionaria"
    Se dice que una serie de tiempo, denotada $X_t$ es _estrictamente estacionaria_ si la distribución conjunta de $(X_{t_1},X_{t_2},\dots,X_{t_k})$ tiene la misma distribución que $(X_{t_1+h},X_{t_2+h},\dots,X_{t_k+h})$ para $t_1,t_2,\dots,t_k,h \in \mathbb{N}$.

Un ejemplo de una serie de tiempo estacionaria estrictamente estacionaria sería una muestra aleatoria. Obsérvese que esta definición implica que la distribución es invariante en el tiempo. De acuerdo con (Tsay, 2010), esta es una condición muy fuerte y es dificil de verificarla empíricamente, por lo que a menudo se asume una condición más débil.

!!! note "Serie de tiempo débilmente estacionaria"
    Se dice que una serie de tiempo $X_t$ es _débilmente estacionaria_ si sus primeros dos momentos son finitos y la media $E{X}_t=\mu$ es constante y $Cov(X_t,X_{t+h})=\gamma (h)$ solo depende de $h$, para $h \in \mathbb{N}$.

En términos prácticos, la gráfica de series de tiempo debería fluctuar alrededor de una constante y su variabilidad debería mantenerse más o menos estable a través del tiempo.

A continuación se presenta un tipo de proceso que cumple con esta característica.

!!! note "Proceso de ruido blanco"
    Sean $\lbrace a_t \rbrace$ una sucesión de variables aleatorias independientes e idénticamente distribuidas con media 0 y varianza $\sigma^2$ finita. Si la distribución de $\lbrace a_t \rbrace$ es normal, entonces la serie se llama _ruido blanco gaussiano_.

## Bibliografía

Box, G., Jenkins, G., Reinsel, G., & Ljung, G. (2016). Time Series Analysis: Forecasting and Control. John Wiley & Sons.

Tsay, R. (2010). Analysis of Financial Time Series (Third Edition). John Wiley & Sons.

> Muchas de las ideas fueron tomadas del curso _Series de tiempo_ impartido por la Dra. Martha Elva Ramírez en Primavera del 2022 en el Colegio de Postgraduados, Campus Montecillo.
