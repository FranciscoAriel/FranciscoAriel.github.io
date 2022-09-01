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
    La función de verosimilitud de $n$ variables aleatorias $X_1, X_2,\dots,X_n$, denotada como $L(\theta|x)$, se define como la *densidad conjunta* de $n$ variables aleatorias $f_{X_1,\dots,X_n}(x_1,\dots,x_n; \theta)$ como *función* de $\theta$. En particular si $X1, X_2,\dots,X_n$ es una muestra aleatoria de $f(x; \theta)$, entonces la función de verosimilitud es $f(x_1; \theta)f(x_2; \theta)\dots f(x_n; \theta)$.

??? example "Función de verosimilitud de lanzamiento de monedas"
    Suponga que se lanza una moneda 5 veces y resulta que sólo cae un águila. Se sospecha que la moneda está cargada ($p = 0.2$), pero el dueño de la moneda asegura que la moneda es legal ($p = 0.5$). De acuerdo a los datos, ¿cúal de los dos afirmaciones es más plausible?

    Note que la función de distribución conjunta puede expresarse como:

    \(f_{\mathbf{X}}(\mathbf{x},p)=\prod_{i=1}^5 p^{x_i}\left(1-p\right)^{1-x_i}=p^{y}\left(1-p\right)^{5-y}
     \)

     donde $y=\sum_{i=1}^5$. Debido a que se observó sólo un águila, $y=1$ y la función de verosimiltud únicamente depende de $p$. Haciendo los cálculos, se tiene que 
     
     \(
     L(p|y=1) = 
     \begin{cases}
     0.08192 & \text{ si } p = 0.2 \\
     0.03125 & \text{ si } p = 0.5
     \end{cases}
     \)

     Por lo tanto se concluye que, *dada la muestra* $p=0.2$ es más plausible que la moneda esté cargada, ya que la función de verosimiltud es mayor.

A continuación se dará una definición para obtener un estimador de máxima verosimilitud.

!!! note "Estimador de máxima verosimilitud"
    Sea $L(\theta|x_1, x_2,\dots, x_n)$ la función de verosimilitud para las variables $X_1, X_2,\dots, X_n$. Si $\hat{\theta}$ es un valor de $\theta \in \Theta$ que *maximiza la función de verosimilitud* $L(\theta|x_1, x_2,\dots, x_n)$, entonces $\hat{\theta}$ es una **estimación** de $\theta$ de la muestra observada $x_1, x_2,\dots, x_n$ **específicamente**.
    
    Si fuera posible encontrar una función que dependa sólo de la muestra aleatoria y que siempre maximizara $L(\theta|x_1, x_2,\dots, x_n)$, para cualquier muestra $X_1, X_2,\dots, X_n$, entonces $\hat{\theta}_X$ es el **estimador de máxima verosimilitud**.

Se mostrarán algunos ejemplos en los cuales es posible encontrar el estimador de máxima verosimilitud.

??? example "Estimador de Máxima Verosimilitud del lanzamiento de una moneda"
    Suponga que se lanza una moneda $n$ veces. Encontrar el estimador de máxima verosimilitud para $\theta$.

    Note que $n$ lanzamienton de moneda $X_1, X_2,\dots, X_n$ pueden considerarse como una muestra aleatoria de la distribución $Ber(\theta)$ con $\theta \in (0, 1) = \Theta$. Usando la función de densidad conjunta del ejemplo anterior:

    \(f_{\mathbf{X}}(\theta,\mathbf{x}) = \theta^{\sum_{i=1}^n x_i}\left(1-\theta\right)^{n-\sum_{i=1}^n x_i}\)

    Una vez observada la muestra, la función de verosimilitud puede expresarse como únicamente como función de $\theta$, por lo que basta con encontrar $\hat{\theta}$ que maximice $L(\theta|x_1, x_2,\dots, x_n)$. Note que $L(\theta|x_1, x_2,\dots, x_n)$ es continua en el intervalo (0,1), por lo que es posible encontrar la derivada de $L(\theta|x_1, x_2,\dots, x_n)$ y hallar su solución.

    \(
     \frac{\partial L(\theta|x_1, x_2,\dots, x_n)}{\partial \theta} = \frac{\sum_{i=1}^n x_i}{\theta}-\frac{n-\sum_{i=1}^n x_i}{1-\theta}=0
     \)
     
     Cuya solución es $\hat{\theta} = \frac{\sum_{i=1}^n x_i}{n}$. Para comprobar que este valor crítico en un punto máximo, se usa el criterio de la segunda derivada.

     \(
     \frac{\partial ^2 L(\theta|x_1, x_2,\dots, x_n)}{\partial \theta^2} = \frac{-2\sum_{i=1}^n x_i}{\theta}-\frac{n-\sum_{i=1}^n x_i}{1-\theta}<0
     \)

     Lo cual implica que $\frac{\sum_{i=1}^n x_i}{n}$ maximiza la función de verosimilitud.

     Por lo tanto $\hat{\theta}=\frac{\sum_{i=1}^n x_i}{n}=\bar{x}$ es la *estimación de máxima verosimilitud* de $\theta$ cuando observamos $x_1,x_2,\dots,x_n$.

     Como esto ocurrirá en cada muestra $\mathbf{X}$, entonces el **estimador de máxima verosimilitud** será:

     \(\hat{\theta}=\bar{X}=\frac{\sum_{i=1}^n X_i}{n}\)

!!! note "Función Score"
    A la derivada de la función de verosimilitud, se le conoce como función Score.

[^1]: Por ahora se considerará que \(\theta\) es de dimensión uno, aunque podría ser un vector de parámetros.
[^2]: Note que podrían existir infinidad de estimadores con esta característica.

> Muchas de las ideas fueron tomadas del curso _Inferencia Estadística_ impartido por el Dr. José Villaseñor en el cuatrimestre Otoño de 2014 en el Colegio de Postgraduados, Campus Montecillo.
