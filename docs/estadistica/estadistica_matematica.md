---
title: Apuntes de Estadística Matemática
summary: Estudio formal de la estadística.
authors: Francisco Vázquez
date: 2022-02-04
---

La __Estadística Matemática__ estudia de forma más profunda y formal a la Teoría de la Probabilidad, que a la vez está basada en Teoría de la Medida. Este curso sirve como base para Teoría Estadística para un doctorado en Estadística.

En ocasiones se requiere una fuerte formación en _Teoría de la Medida_, pero en esta página se usarán los conceptos más indispensables para abordar su estudio.

## Conceptos básicos

Para el estudio de la estadística matemática, se requieren ciertas definiciones que nos permitirán abordar su estudio.

Una definición muy general es el espacio muestral $\Omega$.

!!! note "Espacio muestral"
    Sea $\Omega$ un conjunto de elementos de interés. $\Omega$ es llamado _Espacio Muestral_.

Usualmente nos referimos a $\Omega$ como el conjunto de todos los resultados posibles de un experimento, aunque de acuerdo con Shao (1999) tambíen podría ser un conjunto de números, un intervalo de la recta real, entre otros.

!!! note "Medida"
    Una _medida_ es una extensión matemática natural de longitud, área o volumen de subconjuntos en espacios Euclideanos de dimensión 1 2 o 3.

### Epacios medibles

Cuando se trabaja con un espacio muestral, una medida será una función definida para _ciertos_ subconjuntos de $\Omega$ que satisfagan ciertas propiedades.

!!! note "$\sigma$-álgrebra"
    Sea $\mathcal{F}$ una colección de subconjuntos de un espacio muestral $\Omega$. $\mathcal{F}$ es llamado una $\sigma$__-álgebra__ o $\sigma$__-campo__ si y solo si tiene las siguientes propiedades:

    1. $\emptyset \in \mathcal{F}$ (El conjunto vacío pertenece a la colección).
    2. $A \in \mathcal{F} \rightarrow A^C \in \mathcal{F}$ (Si el conjunto A pertenece a la colección, también su complemento).
    3. $A_i \in \mathcal{F},i=1,2,\dots, \rightarrow \cup A_i \in \mathcal{F}$ (La unión también pertenece a la colección).

!!! tip "Espacio medible"
    Un par $(\Omega,\mathcal{F})$ es llamado _espacio medible_. Los elementos de $\mathcal{F}$ son llamados _eventos_ en probabilidad y estadística.

El concepto de $\sigma$-campo se ilustra con los siguientes ejemplos.

??? example "El $\sigma$-campo más pequeño"
    Sea A un conjunto propio no vacío de $\Omega$, es decir $A \in \Omega, A \ne \Omega$. ¿Será $\lbrace \emptyset,A,A^C,\Omega \rbrace$ un $\sigma$-campo?

    Considere la siguiente imagen

    ![Ilustración de un sigma-campo](img/conjuntos.png)

    Observese que este conjunto $\lbrace \emptyset,A,A^C,\Omega \rbrace$ cumple con las 3 propiedades (está el conjunto vacío $\emptyset$,está su complemento $A^C$). De hecho este $\sigma$-campo es el más pequeño que contiene a $A$, ya que cualquier $\mathcal{F}$ podría contener a $A$.

    Este $\sigma$-campo se denota como $\sigma(\lbrace A \rbrace)$.

??? example "$\sigma$-campo Borel"
    Sea $\mathcal{C}$ el conjunto de todos los intervalos abiertos en los números reales $\mathbb{R}$. Entonces $\mathcal{B}=\sigma(\mathcal{C})$ es llamado $\sigma$__-campo Borel__ y los elementos de $\mathcal{B}$ son llamados _conjuntos Borel_.

    Considere un intervalo abierto arbitrario, por ejemplo el intervalo $A=(5,9)$, este intervalo pertenece a $\mathcal{C}$ y también su complemento, en este caso los intervalos abiertos $(-\infty,5) \cup (9,\infty)$.

    Finalmente $\cup A_i=(-\infty,\infty)$ también está en $\mathcal{C}$.

Aunque ya se había mencionado anteriormente una idea de _medida_, a continuación se definirá el concepto de manera formal.

!!! note "Medida"
    Sea $(\Omega,\mathcal{F})$ un espacio medible. Una función $v$ definida sobre $\mathcal{F}$ es llamada _medida_ si y solo si tiene las siguientes propiedades.

    1. $0 \le v(A) \le \infty, A \in \mathcal{F}$.
    2. $v(\emptyset) = 0$.
    3. Si $A_i \in \mathcal{F}$ y son disjuntos, entonces

    \(v \left( \bigcup_{i=1}^{\infty} A_i \right) = \sum_{i=1}^{\infty} v(A_i)\).

En otras palabras, una medida nos permite asignar un número real a los elementos o subconjuntos del espacio muestral.

!!! note "Espacio de medida"
    A la tripleta $(\Omega,\mathcal{F},v)$ se le conoce como _espacio de medida_.

A continuación se definirán algunos ejemplos de medida de especial interés que son usados en estadística.

!!! example "Medida de probabilidad"
    Si $v(\Omega)=1$ entonces $v$ es llamada una _medida de probabilidad_ y usualmente se denota por $P$ en vez de $v$ y la tripleta $(\Omega,\mathcal{F},P)$ es llamada _espacio de probabilidad_. Note la similitud en la definición que se dió en la sección [axiomas de probabilidad](probabilidad.md#axiomas-de-probabilidad) (a $\mathcal{F}$ se le llamó $\mathbb{s}$).

??? example "Medida de conteo"
    Sea $\mathcal{F}$ una colección de subconjuntos de un espacio muestral $\Omega$. Sea $v(A)$ el número de elementos en el conjunto $A \in \mathcal{F}$. Entonces $v$ es una medida sobre $\mathcal{F}$ y es llamada __medida de conteo__.

    Esta medida es de utilidad en probabilidad cuando se usa la [función de propabilidad con probabilidades iguales](probabilidad.md#axiomas-de-probabilidad).

??? example "Medida de Lebesgue"
    Sea $(\mathbb{R},\mathcal{B})$ un espacio medible (El conjunto de todos los números reales sería el espacio muestral y $\mathcal{B}$ serían el conjunto de todos los intervalos abiertos en los reales). Se define

    \(m([a,b])=b-a\)

    para cada intervalo finito $[a,b] \in \mathcal{B},-\infty < a < b < \infty$. A esta medida se le conoce como __medida de Lebesgue__. Básicamente nos da la longitud del intervalo o distancia ente dos números reales. Note que si $m$ se restringe al espacio medible $([0,1],\mathcal{B}_{[0,1]})$, se obtiene una _medida de probabilidad_.

A continuación se definen algunas propiedades de las medidas.

!!! note "Propiedades de la medida"
    Sea $(\Omega,\mathcal{F},v)$ un espacio medible con $A \in \mathcal{F}$.

    a) Si $A \subset B$ entonces $v(A) \le v(B)$ (La medida es monótona).

    b) (Subaditividad) Para cualquier secuencia $A_1, A_2,\dots,$ se cumple

    \(v \left( \bigcup_{i=1}^{\infty}A_i\right) = \bigcup_{i=1}^{\infty}v(A_i)\)

    c) (Continuidad) Si $A_1 \supset A_2 \supset \dots$ y $v(A_1) \le \infty$, entonces 

    \(v\left( \lim_{n \to \infty} A_n \right) = \lim_{n \to \infty} v \left( A_n \right)\)

Estas propiedades se aplican en las propiedades de la probabilidad, vea la sección [axiomas de probabilidad](probabilidad.md#axiomas-de-probabilidad).

### Función de probabilidad

Ahora se puede definir la función de distribución acumulada a partir de la medida de probabilidad.

!!! note "Función de distribución acumulada"
    Sea $P$ una medida de probabilidad. La _función de distribución acumulada_ de $P$ se define como

    \( F(x) = P(-\infty,x), x \in \mathbb(R) \)

Note que esta definición está en términos de una medida de probabilidad, y no en términos de una variable aleatoria (no lleva el subíndice $X$) como en la sección [Función de distribución](probabilidad.md#función-de-distribución).

Las propiedeades de la función de distribución son las siguientes:

a) $F(-\infty) = \lim_{x \to -\infty} F(x) = 0$

b) $F(\infty) = \lim_{x \to \infty} F(x) = 1$

c) $F$ es no decreciente, es decir, para toda $x < y$ entonces $F(x) \le F(y)$.

d) Es continua por la derecha, esto es $\lim_{x < y \to x} F(y) = F(x)$

### Función medible y variable aleatoria

Hasta ahora se ha trabajado sobre el espacio muestral $\Omega$, pero este suele ser algo muy general. Ahora se definirá una forma para trabajar con números reales en lugar de conjuntos.

!!! note "Función medible"
    Sean $(\Omega,\mathcal{F})$ y $(\Lambda,\mathcal{G})$ espacios medibles y $f$ una función de $\Omega$ a $\Lambda$. La función $f$ es llamada _función medible_ de $(\Omega,\mathcal{F})$ a $(\Lambda,\mathcal{G})$ si y solo si $f^{-1}(\mathcal{G}) \subset \mathcal{F}$.

!!! tip "Variable aleatoria"
    Si $(\Lambda,\mathcal{G})$ es un espacio Borel, es decir $(\mathbb{R},\mathcal{B})$, a $f$ se le conoce como _función Borel_ o _Borel medible_. En probabilidad se le conoce como _variable aleatoria_.

Para saber un poco más de las variables aleatorias vea la sección [variable aleatoria](probabilidad.md#variables-aleatorias).

Si $P$ es una medida de probabilidad y $X$ es una variable aleatoria, entonces a $P_X=P(X^{-1})$ se le conoce como _distribución de X_.

## Integración

!!! note "Integral"
    La integral de una función no negativa de una función $\varphi$ con respectoa $v$ se define como

    \(\int \varphi dv = \sum_{i=1}^{k}a_i v(A_i)\)

Note que este concepto de integración es complejo, ya que involucra funciones Borel $f$ con respecto a una medida $v$ y podría considerarse una especie de promedio ponderado de las medidas por unos pesos $a_i$. A continuación se tratará de ilustrar este concepto mediante unos ejemplos.

??? example "Integral de un conjunto contable"
    Sea $\Omega$ un conjunto contable, $\mathcal{F}$ todos los subconjuntos de $\Omega$ y $v$ la medida de conteo. Para cualquier función Borel $f$ la integral con respecto a $v$ es

    \(\int f d v = \sum_{\omega \in \Omega} f(\omega)\)

    Básicamente esta integral sumará el número de elementos en el conjunto $\omega$.

??? example "Integral de Riemann"
    Si $\Omega = \mathbb{R}$ y $v$ es la medida de Lebesgue, entonces la integral de $f$ sobre el intervalo $[a,b]$ coincide con la integral de Riemann de cálculo (la de los rectángulos) y usualmente se denota como

    \(\int_{a}^{b}f(x) d x= \int_{a}^{b} f(x) dx\)

    Esta integral de Riemman es muy utilizada en Probabilidad y Estadística y es con la que comunmente se trabaja.

La notación de la integral de $f$ puede ser escrita de varias forma, dependiendo si se requiere indicar los límites de integración o las variables de integración. De hecho en Probabilidad y Estadística, la función de distribución acumulada $F$ de $P$ puede expresarse como $\int f(x) d P$ o $\int f(x) d F(x)$ o simplemente $\int f dF$; tambien la esperanza de una variable aleatoria $X$ podría expresarse como $E(X)=\int X d P$.

### Propiedades de la integral

A continuación se presentan las propiedades de la integral, estas propiedades resultarán muy familiares a las que se estudian en Cálculo.

!!! note "Propiedades de la integral"
    Sea $(\Omega,\mathcal{F},v)$ un espacio de medida y $f$ y $g$ funciones Borel.

    i) $\int a f d v = a \int f d v, a \in \mathbb(R)$ (Linealidad de la integral)

    ii) $\int (f + g) d v =  \int f d v + \int g d v$ (Linealidad de la integral)
    
    iii) Si $f \le g$ entonces $\int f d v \le \int g d v$

    iv) Si $f \ge 0$ y $\int f d v = 0$ entonces $f = 0$.

A continuación se enuncian algunos teoremas que se ocupan mucho en Estadística y Probabilidad.

!!! note "Cambio de variable"
    Sea $f$ una función medible de $(\Omega,\mathcal{F},v)$ a $(\Lambda,\mathcal{G})$ y $g$ una función Borel en $(\Lambda,\mathcal{G})$. Entonces

    \(\int_{\Omega}g(f)dv=\int_{\Lambda}g d(v(f^{-1}))\)

    Esta definición es una generalización del cambio de variable de la integral de Riemann $\int g(y) dy = \int g(f(x))f´(x) dx,y=f(x)$

??? example "Una propiedad de la esperanza de X"

!!! note "Teorema de Fubini"

??? example "Intercambio de límites de integración"

!!! note "Derivada Radon-Nikodym"

??? example "Función de densidad"

??? example "Otra forma de definir la esperanza de X"

## Referencias

Shao, J. (1999). _Mathematical statistics_. Springer-Verlag.
