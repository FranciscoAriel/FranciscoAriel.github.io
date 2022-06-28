---
title: Introducción a la Estadística Multivariada
summary: Una introducción a lo métodos multivariados con algunas aplicaciones.
author: Francisco Vázquez
date: 2022-05-31
author_gh_user: FranciscoAriel
publish_date: 2022-05-31
read_time: 45 minutos
---

La estadística multivariada es un área que estudia datos recolectados de individuos a los cuales se les mide una o más características.

Usualmente los datos, denotados por $\mathbf{X}$, son registrados en forma rectangular por medio de columnas y renglones. Esta forma permite representar los datos en forma *matricial*.

\(\mathbf{X} =\lbrace X_{i,j}\rbrace = 
\begin{bmatrix}
X_{1,1} & X_{1,2} & \dots & X_{1,p} \\
X_{2,1} & X_{2,2} & \dots & X_{2,p} \\
\vdots & \vdots &\ddots & \vdots \\
X_{n,1} & X_{n,2} & \dots & X_{n,p} \\
\end{bmatrix}
\)

Note que cada renglón representa una observación multivariada, mientras que cada columna denota una variable, se usarán letras minúsculas pára refereirse a *observaciones* o *realizaciones*.

## Muestras aleatorias

Debido a que en estadística es de interés hacer inferencias sobre el conjunto de datos, se requiere hacer ciertos supuestos sobre la información. En particular se supondrá que la información es una *muestra aleatoria multivariada* de una población específica.

En este sentido, la matriz de datos $\mathbf{X}$ será considerada como una *muestra aleatoria* de dimensión $n$.

\(\mathbf{X} =
\begin{bmatrix}
X_{1,1} & X_{1,2} & \dots & X_{1,p} \\
X_{2,1} & X_{2,2} & \dots & X_{2,p} \\
\vdots & \vdots &\ddots & \vdots \\
X_{n,1} & X_{n,2} & \dots & X_{n,p} \\
\end{bmatrix} =
\begin{bmatrix}
\mathbf{X}_{1}^t \\
\mathbf{X}_{2}^t \\
\vdots \\
\mathbf{X}_{n}^t \\
\end{bmatrix}
\)

!!! note "Muestra aleatoria"
    Se dice que los vectores renglón $\mathbf{X}_{1}^t,\mathbf{X}_{2}^t,\dots,\mathbf{X}_{n}^t$ son una muestra aleatoria de una función de distribución conjunta $f(X)$ con vector de medias $\mathbf{\mu}$ y covarianzas $\mathbf{\Sigma}$. La función de distribución conjunta está dada por $f(\mathbf{X}_{1})f(\mathbf{X}_{2})\dots f(\mathbf{X}_{n})$.

Note que generalmente en cada observación, $\mathbf{X}_i=(X_{i,1},X_{i,2},\dots,X_{i,p})$, proviene de una distribución *multivariada* de dimensión $p$, cuyo vector de medias es $E(\mathbf{X})=\mathbf{\mu}= \begin{pmatrix}\mu_1&\mu_2&\cdots&\mu_p\end{pmatrix}$ y matriz de covarianzas es $Cov(\mathbf{X})=\mathbf{\Sigma}=\lbrace \sigma_{j,j} \rbrace, j=1,2,\dots,p$. De hecho las $p$ variables pueden estar correlacionadas debido a que se mide a un mismo individuo; sin embargo, se asume que los individuos han de ser independientes unos de otros.

En muchas ocasiones, se prefiere trabajar con la matriz de covarianzas en lugar de la matriz de datos, ya que resume las relaciones que hay entre las variables.

Un resultado importante es que si la matriz de covarianzas $\mathbf{\Sigma}$ es positiva definida, existe su inversa $\mathbf{\Sigma}^{-1}$ y:

\(
\mathbf{\Sigma}\mathbf{e}=\lambda \mathbf{e} \rightarrow \mathbf{\Sigma}^{-1}\mathbf{e}=\frac{1}{\lambda} \mathbf{e}
\)

donde $\lambda$ es un eigenvalor y $\mathbf{e}$ es un eigenvector.

!!! abstract "Matriz definda positiva"
    Se dice que una matriz $\mathbf{A}$ es definida positiva si para todo $\mathbf{c}\ne \mathbf{0}$, entonces $\mathbf{c}^t\mathbf{A}\mathbf{c}>0$. Note que $\mathbf{c}^t\mathbf{A}\mathbf{c}$ es un escalar y se le conoce como *forma cuadrática*.

Una propiedad interesante es que la matriz $\mathbf{\Sigma}$ puede descomponerse por medio de sus eigen valores y eigen vectores.

!!! abstract "Descomposición espectral"
    Sea $A$ una matriz de dimensión $p \times p$, entonces

    \(
    A=\sum_{j=1}^{p}\lambda_j\mathbf{e}_j\mathbf{e}_j^t
    \)

Los eigenvectores tienen muchas aplicaciones en estadística multivariada ya que son ortonormales. Sea $\mathbf{P}=[\mathbf{e}_1,\mathbf{e}_2,\cdots,\mathbf{e}_k]$ de dimensión $p \times p$, entonces $\mathbf{P}\mathbf{P}^t = \mathbf{P}^t\mathbf{P}=\mathbf{I}$.

Una aplicación es que si se define la matriz:

\(
\mathbf{\Lambda}=\begin{bmatrix}
\lambda_1 & 0 & \dots & 0\\
0 & \lambda_2 & \dots & 0\\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \dots & \lambda_p\\
\end{bmatrix}
\)

entonces $\mathbf{A}=\mathbf{P}\mathbf{\Lambda}\mathbf{P}^t=\sum_{j=1}^{p}\lambda_j\mathbf{e}_j\mathbf{e}_j^t$ y $\mathbf{A}^{-1}=\mathbf{P}\mathbf{\Lambda}^{-1}\mathbf{P}^t=\sum_{j=1}^{p}\frac{1}{\lambda_j}\mathbf{e}_j\mathbf{e}_j^t$. 

Note que es posible definir la raiz de una matriz,denotada por $\mathbf{A}^{1/2}$, que cumple con la propiedad $\mathbf{A}^{1/2}\mathbf{A}^{1/2}=\mathbf{A}$ y $\mathbf{A}^{-1/2}\mathbf{A}^{-1/2}=\mathbf{A}^{-1}$, simplemente definiendo $\mathbf{A}^{1/2}=\mathbf{P}\mathbf{\Lambda}^{1/2}\mathbf{P}^t=\sum_{j=1}^{p}\sqrt{\lambda_j}\mathbf{e}_j\mathbf{e}_j^t$. Esta expresión es útil para encontrar la matriz de correlaciones a partir de la matriz de covarianzas o viceversa, es decir $\mathbf{R}=\mathbf{D}^{-1/2}\mathbf{S}\mathbf{D}^{-1/2}$ y $\mathbf{S}=\mathbf{D}^{1/2}\mathbf{R}\mathbf{D}^{1/2}$ donde

\(
\mathbf{D}=\begin{bmatrix}
\sqrt{s_{1,1}} & 0 & \dots & 0\\
0 & \sqrt{s_{2,2}} & \dots & 0\\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \dots & \sqrt{s_{p,p}}\\
\end{bmatrix}
\).




Debido a que se tiene una muesta aleatoria, es de interés conocer los momentos o características de dicha función de distribución, para ello se usan los estimadores insesgados para estimar el vector de medias. A continuación se mostrará cómo estimar dichos parámetros.

### Vector de medias y matriz de covarianzas muestrales

Para estimar a $\mathbf{\mu}$ de la matriz de datos se puede usar el *vector de medias muestrales* $\bar{\mathbf{X}}=\frac{1}{n}\mathbf{X}^t\mathbf{1}$, donde $\mathbf{1}^t=\begin{pmatrix}1&1&\dots&1\end{pmatrix}$ es de $1\times n$.

De manera similar, para estimar la matriz de covarianzas, se usa la *matriz de covarianzas muestrales* $\mathbf{S}=\frac{1}{n-1}\mathbf{X}^t\left(\mathbf{I}-\frac{1}{n}\mathbf{1}\mathbf{1}^t\right)\mathbf{X}$.

Se usará la notación $\bar{\mathbf{x}}$ y $\mathbf{s}$ para referirse a realizaciones

??? example "Cálculo del vector de medias y matriz de covarianzas muestrales"
    En este ejemplo se mostrará cómo calcular el vector de medias muestrales. Supónga que se tiene la siguiente matriz de datos con $n=3$ y $p=2$.

    \(\mathbf{x} =
    \begin{bmatrix}
    9 & 1 \\
    5 & 3 \\
    1 & 2 \\
    \end{bmatrix} 
    \)

    Haciendo la sustitución se tiene que el vector de medias es:

    \(
    \bar{\mathbf{x}}= \frac{1}{3}\begin{bmatrix}
    9 & 5 & 1 \\
    1 & 3 & 2\\
    \end{bmatrix}
    \begin{bmatrix}
    1 \\
    1 \\
    1 \\
    \end{bmatrix} = \frac{1}{3}\begin{bmatrix}
    15\\
    6\\
    \end{bmatrix} =
    \begin{bmatrix}
    5\\
    2\\
    \end{bmatrix}
    \)

    y la matriz de covarianzas:

    \(
    \begin{align*}
    \mathbf{s}&=\frac{1}{2}\begin{bmatrix}
    9 & 5 & 1 \\
    1 & 3 & 2\\
    \end{bmatrix}\left( \begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0\\
    0 & 0 & 1\\
    \end{bmatrix} -\frac{1}{3}    \begin{bmatrix}
    1 \\
    1 \\
    1 \\
    \end{bmatrix}
    \begin{bmatrix}
    1 & 1 & 1 
    \end{bmatrix}\right)
    \begin{bmatrix}
    9 & 1 \\
    5 & 3 \\
    1 & 2 \\
    \end{bmatrix} \\
    & = \frac{1}{2}
    \begin{bmatrix}
    9 & 5 & 1 \\
    1 & 3 & 2\\
    \end{bmatrix}
    \begin{bmatrix}
    2/3 & -1/3 & -1/3 \\
    -1/3 & 2/3 & -1/3\\
    -1/3 & -1/3 & 2/3\\
    \end{bmatrix}
    \begin{bmatrix}
    9 & 1 \\
    5 & 3 \\
    1 & 2 \\
    \end{bmatrix}\\
    & =\frac{1}{2}
    \begin{bmatrix}
    4 & 0 & -4 \\
    -1 & 1 & 0\\
    \end{bmatrix}
    \begin{bmatrix}
    9 & 1 \\
    5 & 3 \\
    1 & 2 \\
    \end{bmatrix}\\
    & =\frac{1}{2}
    \begin{bmatrix}
    32 & -4 \\
    -4 & 2 \\
    \end{bmatrix}\\
    &=\begin{bmatrix}
    16 & -2 \\
    -2 & 1 \\
    \end{bmatrix}
    \end{align*}
    \)

### Matriz de Combinaciones lineales

En estadística multivariada es posible realizar combinaciones lineales de variables para formar una nueva variable. Las combinaciones lineales estudiadas tienen la forma:

\(
\mathbf{a}^t\mathbf{X}=a_1 \mathbf{X}_1 + a_2 \mathbf{X}_2 + \dots + a_p \mathbf{X}_p
\)

Note que el vector $\mathbf{a}^t$ es de dimensión $1 \times p$ y la matriz $\mathbf{X}=\begin{pmatrix}\mathbf{X}_1&\mathbf{X}_2&\dots&\mathbf{X}_p\end{pmatrix}$ es de dimensión $n\times p$, aunque solo nos interesa trabajar con las $p$ variables.

Es posible calcular la media, la varianza y las covarianzas muestrales de dichas combinaciones lineales sin la necesidad de calcular las nuevas variables.

Estadístico|Combinación lineal|Fórmula
-----------|------------------|-------
Media muestral|$\mathbf{a}^t\mathbf{X}$|$\mathbf{a}^t\bar{\mathbf{x}}$
Varianza muestral|$\mathbf{a}^t\mathbf{X}$|$\mathbf{a}^t\mathbf{s}\mathbf{a}$
Covarianzas muestrales|$\mathbf{a}^t\mathbf{X}$ y $\mathbf{b}^t\mathbf{X}$|$\mathbf{a}^t\mathbf{s}\mathbf{b}$

## Distribución normal multivariada

En estadística multivariada, el modelo de distribución normal juega un papel muy importante, debido a que cuando se tienen muchos datos, muchas estadísticas multivariadas tienen distribución normal, debido al *Teorema Central del Límite*. También muchos fenómenos se comportan de manera normal.

!!! note "Distribución normal multivariada"
    La distribución normal multivariada, de dimensión $p$ para el vector aleatorio $\mathbf{X}^t=\begin{pmatrix}X_1&X_2&\cdots&X_p\end{pmatrix}$ es:

    \(
    f_{\mathbf{X}}(\mathbf{x})=\frac{1}{(2\pi)^{p/2}|\mathbf{\Sigma}|^{1/2}}e^{\frac{-1}{2}(\mathbf{x}-\mathbf{\mu})^t\mathbf{\Sigma}^{-1}(\mathbf{x}-\mathbf{\mu})}
    \)

    donde $-\infty < x_j < \infty, i=1,2,\dots,p$; $;-\infty < \mu_j < \infty, i=1,2,\dots,p$ y $\mathbf{\Sigma}$ es positiva definida.

Es posible calcular contornos en los que la densidad es constante usando $\lbrace \mathbf{x} | (\mathbf{x}-\mathbf{\mu})^t\mathbf{\Sigma}^{-1}(\mathbf{x}-\mathbf{\mu}) = c^2 \rbrace$.

Note que los elipsoides están centrados en $\mathbf{\mu}$ y tiene ejes $c\sqrt{\lambda_j}\mathbf{e}_j$, para $j=1,2,\dots,p$.

Si se usa $c^2=\chi_{p}(\alpha)$, donde $\chi_{p}(\alpha)$ se obtienen contornos que contienen $(1-\alpha) \times 100 \%$ de la probabilidad, donde $\chi_{p}(\alpha)$ es el persentil superior de una distribución chic cuadrada con $p$ grados de libertad.

### Propiedades de la distribución normal multivariada

La distribución normal multivariada tiene muchas propiedades y resultados análagos a la distribución normal univariada, los cuales se estudiarán a continuación.

!!! note "Distribución de una combinación lineal"
    Si $\mathbf{X}\sim N_p(\mathbf{\mu},\mathbf{\Sigma})$, entonces cualquier combinación lineal de sus variables $\mathbf{a}^t\mathbf{X}=a_1\mathbf{X}_1+a_2\mathbf{X}_2+\dots+a_n\mathbf{X}_n$ se distribuye normal univariada, es decir $\mathbf{a}^t\mathbf{X}\sim N(\mathbf{a}^t\mathbf{\mu},\mathbf{a}^t\mathbf{\Sigma}\mathbf{a})$.

!!! note "Distribución de varias combinaciones lineal"
     Si $\mathbf{X}\sim N_p(\mathbf{\mu},\mathbf{\Sigma})$, entonces las $q$ combinaciones lineales

    \(
    \mathbf{A}\mathbf{X}=
    \begin{pmatrix}
    a_{1,1}\mathbf{X}_1+a_{1,2}\mathbf{X}_2+\dots+a_{1,p}\mathbf{X}_p\\
    \vdots\\
    a_{q,1}\mathbf{X}_1+a_{q,2}\mathbf{X}_2+\dots+a_{q,p}\mathbf{X}_p\\
    \end{pmatrix}
    \)

    tiene distribución normal $q$ variada, es decir: $\mathbf{A}\mathbf{X}\sim N_q(\mathbf{A}\mathbf{\mu},\mathbf{A}\mathbf{\Sigma}\mathbf{A}^{t})$.

!!! note "Distribución de subconjuntos de una normal multivariada"
    Si se tiene un vector aleatorio $\mathbf{X}$ de dimensión $p \times 1$, se puede partir dicho vector como se muestra a continuación:

    \(
    \begin{align*}
    \mathbf{X} ({p \times 1})&=
    \begin{bmatrix}
    \mathbf{X}_1 ({q \times 1})\\
    \mathbf{X}_2 ({(p-q) \times 1})\\
    \end{bmatrix}\\
    \mathbf{\mu} ({p \times 1})&=
    \begin{bmatrix}
    \mathbf{\mu}_1 ({q \times 1})\\
    \mathbf{\mu}_2 ({(p-q) \times 1})\\
    \end{bmatrix}\\
    \mathbf{\Sigma} ({p \times p})&=
    \begin{bmatrix}
    \mathbf{\Sigma}_{11} ({q \times q}) & \mathbf{\Sigma}_{12} ({q \times (p-q)})\\
    \mathbf{\Sigma}_{21} ({(p-q) \times q}) & \mathbf{\Sigma}_{22} ({(p-q) \times (p-q)})\\
    \end{bmatrix}\\
    \end{align*}
    \)

    entonces $\mathbf{X}_1 \sim N_q(\mathbf{\mu}_1,\Sigma_{11})$.

!!! note "Variables independientes de una normal multivariada"
    a) Si $\mathbf{X}_1$ y $\mathbf{X}_2$ de dimensión $q_1 \times 1$ y $q_2 \times 1$ son independientes, entonces $Cov(\mathbf{X}_1,\mathbf{X}_2)=\mathbf{0}$.

    b) Si

    \(
    \begin{bmatrix}
    \mathbf{X}_1 \\
    \mathbf{X}_2 \\
    \end{bmatrix} \sim N_p\left(\begin{bmatrix}
    \mathbf{\mu}_1 \\
    \mathbf{\mu}_2 \\
    \end{bmatrix}, \begin{bmatrix}
    \mathbf{\Sigma}_{11} & \mathbf{\Sigma}_{12}\\
    \mathbf{\Sigma}_{21} & \mathbf{\Sigma}_{22}\\
    \end{bmatrix}\right)
    \)

    entonces $\mathbf{X}_1$ y $\mathbf{X}_2$ son independientes si y solo si $\mathbf{\Sigma}_{12}=\mathbf{0}$.

    c) Si $\mathbf{X}_1 \sim N_{q_1}(\mathbf{\mu}_1,\mathbf{\Sigma}_{11})$ y $\mathbf{X}_2 \sim N_{q_1}(\mathbf{\mu}_2,\mathbf{\Sigma}_{22})$ son independientes, entonces

    \(
    \begin{bmatrix}
    \mathbf{X}_{q_1}\\
    \mathbf{X}_{q_2}\\
    \end{bmatrix} \sim N_{q_1+q_2}\left( \begin{bmatrix}
    \mathbf{\mu}_1 \\
    \mathbf{\mu}_2 \\
    \end{bmatrix}, \begin{bmatrix}
    \mathbf{\Sigma}_{11} & \mathbf{0}\\
    \mathbf{0}^t & \mathbf{\Sigma}_{22}\\
    \end{bmatrix} \right)
    \)

!!! note "Distribución condicional normal multivariada"
    Sea

    \(
    \begin{bmatrix}
    \mathbf{X}_{1}\\
    \mathbf{X}_{2}\\
    \end{bmatrix} \sim N_{p}\left( \begin{bmatrix}
    \mathbf{\mu}_1 \\
    \mathbf{\mu}_2 \\
    \end{bmatrix}, \begin{bmatrix}
    \mathbf{\Sigma}_{11} & \mathbf{\Sigma}_{12}\\
    \mathbf{\Sigma}_{21} & \mathbf{\Sigma}_{22}\\
    \end{bmatrix} \right)
    \)
    
    con $|\mathbf{\Sigma}_{22}|>0$. Entonces la distribución condicional de $\mathbf{X}_{1}$ dado que $\mathbf{X}_{2}=\mathbf{x}_{2}$, es normal y tiene media $\mathbf{\mu}_1+\mathbf{\Sigma}_{12}\mathbf{\Sigma}_{22}^{-1}(\mathbf{x}_{2}-\mathbf{\mu}_2)$ y covarianza $\mathbf{\Sigma}_{11}-\mathbf{\Sigma}_{12}\mathbf{\Sigma}_{22}^{-1}\mathbf{\Sigma}_{21}$. 

!!! note "Distribución de una forma cuadrática"
    Sea $\mathbf{X}\sim N_p(\mathbf{\mu},\mathbf{\Sigma})$ con $|\mathbf{\sigma}|> 0$. Entonces
    $(\mathbf{X}-\mathbf{\mu})^{t}\mathbf{\Sigma}^{-1}(\mathbf{X}-\mathbf{\mu}) \sim \chi_p^2$.

### Inferencia en la distribución normal multivariada

En esta sección se estudiarán la forma de hacer inferencia con una muestra aleatoria multivariada.

!!! note "Distribución conjunta multivariada"
    Suponga que $\mathbf{X}_1,\mathbf{X}_2,\dots,\mathbf{X}_n$, cada uno es un vector de dimensión $1\times p$, es una *muestra aleatroria* de tamaño $n$ que proviene de una población normal multivariada con vector de medias $\mathbf{\mu}$ y matriz de covarianzas $\mathbf{\Sigma}$. La función de densidad conjunta es el producto de todas las densidades marginales:

    \(
    \begin{align*}
    f_{\mathbf{X}_1,\mathbf{X}_2,\dots,\mathbf{X}_n}(\mathbf{x}_1,\mathbf{x}_2,\dots,\mathbf{x}_n) & =\prod_{i=1}^{n}\frac{1}{(2\pi)^{p/2}|\mathbf{\Sigma}|^{1/2}}e^{\frac{-1}{2}(\mathbf{x}_i-\mathbf{\mu})^t\mathbf{\Sigma}^{-1}(\mathbf{x}_i-\mathbf{\mu})}\\
    & = \frac{1}{(2\pi)^{np/2}|\mathbf{\Sigma}|^{n/2}}e^{\frac{-1}{2}\sum_{i=1}^{n}(\mathbf{x}_i-\mathbf{\mu})^t\mathbf{\Sigma}^{-1}(\mathbf{x}_i-\mathbf{\mu})}
    \end{align*}
    \)

Note que, una vez observados los datos, dicha función es ahora función de $\mathbf{\mu}$ y $\mathbf{\Sigma}$, a esta función se le conoce como *función de verosimilitud*. Es de interés encontrar los valores $\hat{\mathbf{\mu}}$ y $\hat{\mathbf{\Sigma}}$ que maximicen dicha verosimilitud dados los datos.

!!! note "Estimadores de máxima verosimilitud"
    Sea $\mathbf{X}_1,\mathbf{X}_2,\dots,\mathbf{X}_n$ una muestra aleatoria de una población normal con media $\mathbf{\mu}$ y covarianza $\mathbf{\Sigma}$. Entonces 

    \(
    \hat{\mathbf{\mu}} = \bar{\mathbf{X}};
    \hat{\mathbf{\Sigma}} = \frac{n-1}{n}\mathbf{S}
    \)

    son los *estimadores de máxima verosimilitud* de $\mathbf{\mu}$ y $\mathbf{\Sigma}$. Las realizaciones $\bar{\mathbf{x}}$ y $\frac{n-1}{n}\mathbf{s}$ son llamadas *estimaciones de máxima verosimilitud*.

Note que los estimadores de máxima verosimilitud son *aleatorios*, mientras que las *estimaciones* son fijos. Por esta razón, es de interés estudiar las distribuciones de los estimadores de máxima verosimilitud.

Los estimadores de Máxima Verosimilitud tambien tienen propiedades deseables, por ejemplo son invariantes, es decir si $\hat{\mathbf{\theta}}$ es un estimador de máxima verosimilitud, entonces un estimador de $h(\mathbf{\theta})$ es $h(\hat{\mathbf{\theta}})$.

Otra propiedad interesante es la suficiencia, en pocas palabras, toda la información acerca de $\mathbf{\mu}$ y $\mathbf{\Sigma}$ está contenida en $\hat{\mathbf{\mu}}$ y $\hat{\mathbf{\Sigma}}$.

### Distribuciones muestrales multivariada

Las distribuciones de $\bar{\mathbf{X}}$ y $\mathbf{S}$ son análogas al caso univariado, aunque hay ciertas generalizaciones.

!!! note "Distribución del vector de medias muestral"
    La distribución de $\bar{\mathbf{X}}$ es normal con vector de medias $\mathbf{\mu}$ y covarianza $\frac{1}{n}\mathbf{\Sigma}$.

!!! note "Distribución de la matriz de covarianza muestral"
    La distribución de $(n-1)\mathbf{S}=\sum_{i=1}^{n}\mathbf{V}_i\mathbf{V}_i^t$ es Wishart $p$ variada con parámetros $n-1$ y $\mathbf{\Sigma}$, donde cada $\mathbf{V}_i = (\mathbf{X}-\bar{\mathbf{X}}) \sim N_p(\mathbf{0},\mathbf{\Sigma})$.

!!! note "Independencia del vector de medias y matriz de covarianzas muestrales"
    $\bar{\mathbf{X}}$ y $\mathbf{\Sigma}$ son independientes.

### Distribución para tamaños de muestras grandes del vector de medias y matriz de covarianzas muestrales

Las distribuciones de $\bar{\mathbf{X}}$ y $\mathbf{\Sigma}$ son similares al caso univariado cuando el tamaño de muestra aumenta, es decir se cumple la *Ley de los grandes números* y el *Teorema Central del Límite*.

!!! note "Ley de los grandes números"
    $\bar{\mathbf{X}}$ converge en probabilidad a $\mathbf{\mu}$ y $\mathbf{S}$ converge en probabilidad a $\mathbf{\Sigma}$.

!!! note "Teorema central del límite"
    Sea $\mathbf{X}_1,\mathbf{X}_2,\dots,\mathbf{X}_n$ una muestra aleatoria de una población normal con media $\mathbf{\mu}$ y covarianza $\mathbf{\Sigma}$ finita. Entonces $\sqrt{n}(\mathbf{X}-\mathbf{\mu})$ tiene distribución aproximadamente $N_p(\mathbf{0},\mathbf{\Sigma})$ para $n - p$ grande.

!!! note "Distribuciones aproximadas"
    Sea $\mathbf{X}_1,\mathbf{X}_2,\dots,\mathbf{X}_n$ una muestra aleatoria de una población normal con media $\mathbf{\mu}$ y covarianza $\mathbf{\Sigma}$ finita. Entonces $n(\mathbf{X}-\mathbf{\mu})^t\mathbf{S}^{-1}(\mathbf{X}-\mathbf{\mu})$ es aproximadamente $\chi_p^2$ para $n-p$ grande.

## Inferencias sobre el vector de medias

Es de interés hacer inferencias sobre el vector de medias. En particular se requiere saber si el vector de medias es igual a cierto vector de valores.

Puede establecerse una pruaba de hipótesis de la forma:

\(
H_0: \mathbf{\mu} = \mathbf{\mu}_0 \text{ vs } H_a: \mathbf{\mu} \ne \mathbf{\mu}_0
\)

De manera análoga al caso univariado, se puede realizar un contraste de hipótesis similar a la prueba F llamado T cuadrada de Hotelling, es decir.

\(
T^2=n(\bar{\mathbf{X}}-\mathbf{\mu}_0)^t\mathbf{S}^{-1}(\bar{\mathbf{X}}-\mathbf{\mu}_0)
\)

donde $T^2 \sim \frac{(n-1)p}{n-p}F_{p,n-p}$. Por lo que se rechaza $H_0$ si $T^2 > \frac{(n-1)p}{n-p}F_{p,n-p}(\aplha)$.

## Bibliografía

Johnson, R., & Wichern, D. (2007). *Applied Multivariate Statistical Analysis* (6th edition). Pearson Education.
