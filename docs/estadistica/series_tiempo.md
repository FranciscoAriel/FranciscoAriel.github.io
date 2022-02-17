---
title: Introducción a las Series de Tiempo
summary: Introducción a las series de tiempo, definiciones y ejemplos.
authors: Francisco Vázquez
date: 2022-01-26
---

Las series de tiempo es una de la metodologías estadísticas más aplicada debido a que usualmente se tiene información histórica que se desea estudiar y se usan en diversos campos del conocimiento, por ejemplo en economía. Sin embargo actualmente es común encontrar aplicaciones en prácticamente cualquier área.

Uno de los principales usos de las series de tiempo, es hacer *pronósticos de valores futuros* de la variable de interés, usando la información disponible.

![Representación de una serie en los negocios](img/stock.jpg)
Imagen de [geralt](https://pixabay.com/es/users/geralt-9301/) en [pixabay](https://pixabay.com/).

## Introducción y definición

!!! note "Definición"
    Una serie de tiempo $X_t$, es una secuencia de valores numéricos indexados por una variable, generalmente tiempo $t$.

Las series de tiempo pueden ser continuas o discretas. Comunmente en ciencias sociales o economía, las series de tiempo estan medidas en intervalos de tiempo regulares, ya sea de manera anual, trimestral, mensual o diaria.

Las series de tiempo pueden ser consideradas un caso particular de los procesos estocásticos en donde el parámetro o índice $t$ es discreto. Para una revisión más completa de las series de tiempo visite la sección [Procesos estocásticos](procesos_estocasticos.md).

## Herramientas de exploración

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
