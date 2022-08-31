---
title: Inferencia estadística
summary: Introducción a la teoría estadística en donde se abarcan temas de propiedades de los estimadores puntuales y por intervalos.
author: Francisco Vázquez
date: 2021-09-10
author_gh_user: FranciscoAriel
publish_date: 2021-09-10
read_time: 25 minutos
---

En la vida real quisiéramos estimar valores aproximados de características de interés de una población, por ejemplo la temperatura promedio de cierto lugar.

![lluvia](img/rain.jpg)
Imagen de [Bianca van Dijk](https://pixabay.com/es/users/biancavandijk-9606149/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5960262) en [Pixabay](https://pixabay.com/es/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5960262)

Sería conveniente tener _fórmulas generales_ para poder estimar algo desconocido únicamente utilizando información obtenida a partir de la observación de fenómenos; quisiéramos que esas _fórmulas generales_ sean buenas y que se pudieran utilizar con otros datos. Por ello en este documento se detalla la forma en obtener estimadores de los parámetros poblacionales que son de interés.

## Propiedades deseables de los estimadores

Supóngase que $\mathbf{X}=( X_1,X_2,\ldots,X_n )$ es una muestra aleatoria de una densidad \(f_X(x;\theta)\) conocida, la cual depende de un parámetro desconocido[^1] \(\theta\), aunque sabemos que \(\theta\) pertenece a un espacio de parámetros \(\Theta\). Si únicamente conocemos la muestra aleatoria (observaciones), \(\mathbf{x}\) que representan una realización de \(\mathbf{X}\), ¿Cuál es el valor aproximado de \(\theta\)?.

!!! note "Definición Estadística"
     Una estadística es una _función de la muestra aleatoria_ solamente. Note que es una _variable aleatoria_.

!!! note "Definición Estimador"
     Un estimador del parámetro \(\theta\) es una estadística \(T=v(\mathbf{X})\), función de la muestra aleatoria, tal que la estimación \(t=v(\mathbf{x}) \in \Theta\).

!!! note "Definición Estimación" 
     Una estimación es una _realización de un estimador_, es decir, es un número real.

En otras palabras, para que \(T\) sea un estimador[^2], es necesario que al evaluar el estimador en cualquier muestra, \(T\) caiga dentro del espacio de parámetros \(\Theta\). Se desea que los estimadores tengan ciertas propiedades deseables:

### Suficiencia

!!! note "Principio de suficiencia" 
     Si \(Y_1=u( X_1,X_2,\ldots,X_n )\) es una estadística suficiente para \(\theta\), entonces cualquier inferencia sobre \(\theta\) va a depender de la muestra \(X_1,X_2,\ldots,X_n\) _únicamente a través de la estadística suficiente_ \(Y_1\).

     Es decir si tenemos dos muestras observadas \(x_1,x_2,\ldots,x_n\) y \(y_1,y_2,\ldots,y_n\), entonces la inferencia sobre \(\theta\) será la misma sin importar que se use la muestra uno \(\mathbf{x}=x_1,x_2,\ldots,x_n\) o la muestra dos \(\mathbf{y}=y_1,y_2,\ldots,y_n\); en otras palabras \(u( x_1,\ldots,x_n ) =u( y_1,\ldots,y_n ) \).

La propiedad de suficiencia se refiere a que una estadística \(Y_1\) *concentra* toda la información acerca del parámetro de la muestra aleatoria en *una sola variable aleatoria*. Es decir debe tomar en cuenta a *toda la muestra*.

La estadística suficiente es un tipo especial de estadística, ya que condensa la información de la muestra de tal forma que no se pierda ninguna información acerca del parámetro \(\theta\).

!!! note "Definición Estadística suficiente"
     Sea \(\mathbf{X}\) una muestra aleatoria con densidad conjunta \(f_{\mathbf{X}}(\mathbf{x} ;\theta)\). Una estadística \(Y_1=u(\mathbf{X}) \) es suficiente si y sólo si \(f_{\mathbf{X}|Y_1 } (\mathbf{x}|y_1)\) no depende de \(\theta\).

??? example "Ilustración de una estadística suficiente"
    Sea $X_1, X_2,\dots, X_n$ una muestra aleatoria con densidad $f_X(x; \theta) = \theta e^{−\theta x}I_{(0,\infty)}(x)$, se demostrara que

    \(Y_1 = \sum_{i=1}^{n} Xi\)

    es una estadística suficiente para $\theta$, la cual al ser suma de exponenciales, tiene densidad $Gamma(n, \theta)$, donde $\theta = 1/\beta$.

En la práctica, esta definición no es muy útil ya que implica calcular la densidad condicional y conocer la distribución de la estadística suficiente. Para ello se tiene el siguiente teorema.

!!! note "Teorema de Neyman-Fisher"
    Sea $X_1, X_2,\dots, X_n$ una muestra aleatoria con densidad $f_X(x; \theta), \theta \in (a, b) \subset \mathbb{R}$. Sea $Y_1 = u(X)$ una estadística con densidad $f_{Y_1}(y_1)$. $Y_1$ es una estadística suficiente para $\theta$ si y solo si 
    
    \(f_X(x) = \varphi_1(Y_1, \theta)\varphi_2(x)\)

    la densidad conjunta de las observaciones se puede factorizar de la forma anterior.

### Estimadores insesgados de varianza uniformemente mínima

### Consistencia

### Mejor asintótoticamente normal

### Completez

## Estimación puntual

### Dos teoremas importantes

### Método de momentos

### Estimadores de máxima verosimilitud

Antes de conocer el método, se discutirá que se entiende por verosimilitud. Esta idea fue
desarrollada por Fisher en la década de 1920 y es uno de los conceptos más usados en estadística.

La idea de verosimilitud se basa en la probabilidad de observar lo más creible dada una muestra, por lo tanto estos estimadores tratarán de maximizar la probabilidad de que haya ocurrido el evento más probable dada cierta información.

Por ejemplo, si en una carrera de caballos participan 8 caballos en igualdad de condiciones,  pero se sabe que hay un caballo favorito (el cual ya ha ganado varias carreras anteriormente) y éste gana la carrera, entonces el caballo ganador seguramente tenía las mejores condiciones sobre los demás y por lógica ganó la carrera. De hecho pudo haber ganado cualquier otro caballo, ya que es un evento posble pero con poca probabilidad.

!!! abstract "Función de distribución"
    La función de verosimilitud de $n$ variables aleatorias $X_1, X_2,\dots,X_n$, se define como la *densidad conjunta* de $n$ variables aleatorias $f_{X_1,\dots,X_n}(x_1,\dots,x_n; \theta)$ como *función* de $\theta$. En particular si $X1, X_2,\dots,X_n$ es una muestra aleatoria de $f(x; \theta)$, entonces la función de verosimilitud es $f(x_1; \theta)f(x_2; \theta)\dots f(x_n; \theta)$.

[^1]: Por ahora se considerará que \(\theta\) es de dimensión uno, aunque podría ser un vector de parámetros.
[^2]: Note que podrían existir infinidad de estimadores con esta característica.

> Muchas de las ideas fueron tomadas del curso _Inferencia Estadística_ impartido por el Dr. José Villaseñor en el cuatrimestre Otoño de 2014 en el Colegio de Postgraduados, Campus Montecillo.
