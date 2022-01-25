---
title: Introducción a la probabilidad
summary: Introducción a la teoría de la probabilidad, definiciones y ejemplos.
authors: Francisco Vázquez
date: 2021-12-20
---

## Introducción

![Juegos de azar](img/poker.jpg)
Imagen de [ToNic-Pics](https://pixabay.com/es/users/tonic-pics-3001971/) en [Pixabay](https://pixabay.com/images/id-1564042/)

La probabilidad es una rama de las matemáticas que estudia el **azar o aleatoriedad**. En palabras simples, trata de medir la incertidumbre de que ocurra un suceso o evento $E$. El resultado de dicho experimento  $E$ **no** puede ser determinado con antelación.

Para darnos una idea de lo que es la probabilidad, tienen dos definiciones:

!!! note "Definición clásica (A priori)"
     Suponiendo que un evento $E$ puede ocurrir de $s$ formas de un total de $n$ formas igualmente posibles. Entonces $p=s/n$.

!!! note "Definición frecuentista (A posteriori)"
     Suponiendo que después de $n$ repeticiones, para valores muy grandes de $n$, un evento $E$ ocurre $s$ veces. Entonces $p=s/n$.

Estas definiciones a pesar de ser muy intuitivas, tienen grandes fallos. Por ejemplo, la primer definición es una definición circular, por que la frase _igualmente posible_ es un sinónimo de _igualmente probable_, justo lo que se quiere definir. En la segunda definición no se especifican los valores de $n$. Estas definiciones son muy antiguas, pero pueden ayudar a entender de forma muy general el concepto de **probabilidad**.

Actualmente el estudio de la probabilidad se realiza mediante el uso de la teoría de conjuntos, a partir de ciertos axiomas.

A continuación se presentarán algunas definiciones que serán de gran utilidad para conocer más de la probabilidad.

### Espacio muestral y eventos

!!! note "Espacio muestral"
     El conjunto $\Omega$ de todos los resultados posibles de un experimento se denomina **espacio muestral**.

!!! note "Punto muestral"
    Un elemento del espacio muestral $\Omega$ se denomina **punto muestral**. Es un resultado particular.

!!! note "Evento"
    Un evento $A$ es un subconjunto del espacio muestral $\Omega$, es decir,  es un conjunto de resultados. Cualquier colección de eventos y cada uno es un subconjunto de $\Omega$ se denominará con $\mathbb{s}$.

!!! note "Evento particular"
    El evento $\lbrace a \rbrace$ constituido por un solo punto $a \in \Omega$ se denomina **evento muestral**.

Considere el experimento de lanzar un dado de 6 caras.

![Representación espacio muestral dados](img/dados.jpg)
Imagen de [anncapictures](https://pixabay.com/es/users/anncapictures-1564471/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2031512) en [Pixabay](https://pixabay.com/es/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2031512).

El espacio muestral estaría formado por los seis números posibles, es decir:

$$ \Omega = \lbrace 1,2,3,4,5,6 \rbrace $$

Un *evento particular* podría ser un resultado en específico, por ejemplo $\lbrace 1 \rbrace$. Todos los subconjuntos posibles de resultados consitituirían $\mathbb{s}$.

Sean el evento $A$ que el resultado sea par, el evento $B$ que el resultado sea impar y el evento $C$ que el resultado sea mayor a 3.

Entonces se tiene que 

$$A=\lbrace 2,4,6 \rbrace, \\
B=\lbrace 1,3,5 \rbrace, \\
C=\lbrace 4,5,6 \rbrace
$$

Observe que el evento $B \cup C = \lbrace 1,3,4,5,6\rbrace$ también es un evento en el espacio muestral $S$.

### Axiomas de probabilidad

Como se mencionó anteriormente, actualmente la probabilidad se estudia de manera formal partiendo de 3 axiomas.

!!! caution "Conocimiento avanzado"
    El estudio de la probabilidad requiere conocimientos avanzados de *Matemáticas* y *Teoría de Conjuntos* los cuales están fuera del alcance de esta página.

Sea $A$ un evento del espacio muestral $S$. Una función $P: \mathbb{s} \rightarrow [0,1]$ es llamada *función de probabilidad* si satisface estas 3 condiciones.

- **Axioma 1**: $0\le P(A) \le 1$ para $A \in \mathbb{s}$
- **Axioma 2**: $P(\Omega) = 1$
- **Axioma 3**: Para cualquier secuencia de eventos $A_1,A_2,\dots$ mutuamente excluyentes, entonces

$$P\left( \bigcup_{i=1}^{\infty} A_i\right)=\sum_{i=1}^{\infty}A_i$$

Se dice que $P(A)$ es la *probabilidad de que ocurra el evento A*.

A partir de esos axiomas, se derivan otras propiedades.

- $P(\emptyset)=0$.
- Si $A_1,\dots,A_n$ son eventos mutuamente excluyentes, entonces $P\left( \bigcup_{i=1}^{n} A_i\right)=\sum_{i=1}^{n}P(A_i)$.
- $P(A^c)=1-P(A)$.
- Para cualesquiera 2 eventos: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
- Si $A \subset B$, entonces $P(A) < P(B)$.

En ciertos problemas con espacios muestrales finitos $N$, es posible asignarle a cada uno de los puntos una probabilidad igual a $1/n$.

En el ejemplo de los dados, se puede asumir que la probabilidad de que se obtenga un resultado en particular es $1/6$, por lo que P(A) = 1/2.

### Probabilidad condicional e independencia

En ocasiones, es de interés conocer la probabilidad de un evento, dado que haya ocurrido otro. En este sentido, se define la probabilidad condicional.

!!! note "Probabilidad condicional"
     Sean $A$ y $B$ dos eventos en $\mathbb{s}$. La *probabilidad condicional* del evento $A$ dado el evento $B$, denotada por $P\left( A|B \right)$, se define como 
     $P \left( A|B\right) =\frac{P\left(A\cap B\right)}{P\left( B\right)}$ con $P(B) \ne 0$.

Note que la probabilidad anterior no está definida cuando $P(B) = 0$. También se desprende la fórmula $P(A \cap B )= P(A|B)P(B) = P(B|A)P(A)$ si $P(A) \ne 0$.

De la definición anterior, se desprenden las siguientes propiedades de la función de probabilidad condicional

- $P(\emptyset|B)=0$.
- Si $A_1,A_2,\dots,A_n$ son eventos mutuamente excluyentes en $\mathbb{s}$, entonces $P(A_1 \cup A_2 \cup \dots \cup A_n|B) = \sum_{i=1}^{n}P(A_i|B)$.
- $P(A^c|B)=1 - P(A|B)$.
- Si $A_1$ y $A_2 \in \mathbb{s}$, entonces $P(A_1|B)=P(A_1 \cap A_2|B)+P(A_1 \cap A^c_2|B)$.
- Para cualesquiera 2 eventos $A_1$ y $A_2 \in \mathbb{s}$, $P(A_1 \cup A_2 |B) = P(A_1|B)+P(A_2|B)-P(A_1 \cap A_2|B)$.
- Si $A_1$ y $A_2 \in \mathbb{s}$ y $A_1 \subset A_2$, entonces $P(A_1|B) \le P(A_2|B)$.
- Si $A_1,A_2,\dots,A_n \in \mathbb{s}$, entonces $P(A_1 \cup A_2 \cup \dots \cup A_n|B) \le \sum_{i=1}^{n}P(A_i|B)$.

A continuación se mencionan unos teoremas de gran importancia

!!! note "Teorema de probabilidades totales"
    Si $B_1, B_2, \dots,B_n$ es una colección de eventos mutuamente disjuntos en $\mathbb{s}$ y satisfacen $\Omega = \cup^{n}_{j=1} B_j$ y $P(B_j)>0$ para $j = 1,\dots,n$, entonces para toda $A \in \mathbb{s}$ se tiene $P\left(A\right)=\sum^{n}_{j=1}P(A|B_j)P(B_j)$.

![Probabilidad total](img/prob_total.png)

!!! note "Teorema de Bayes"
    Si $B_1, B_2, \dots,B_n$ es una colección de eventos mutuamente disjuntos en $\mathbb{s}$ y satisfacen $\Omega = \cup^{n}_{j=1} B_j$ y $P(B_j)>0$ para $j = 1,\dots,n$, entonces para toda $A \in \mathbb{s}$ con $P(A)>0$ se tiene $P\left(B_k|A\right)=\frac{P(A|B_k)P(B_k)}{\sum^{n}_{j=1}P(A|B_j)P(B_j)}$.

### Independencia de eventos

!!! note "Eventos independientes"
    Sean $A$ y $B$ dos eventos en $\mathbb{s}$ Los eventos $A$ y $B$ se dice que son independientes i y solo si una de las siguientes condiciones es satisfecha.

    - $P(A \cap B) = P(A)P(B)$
    - $P(A|B) = P(A)$ si $P(B) > 0$
    - $P(B|A) = P(B)$ si $P(A) > 0$

De la definición anterior, se desprenden las siguientes propiedades:

!!! note "Eventos independientes y sus complementos"
    Si los eventos $A$ y $B$ son independientes, entonces los siguientes eventos también son independientes: $A$ y $B^c$, $A^c$ y $B$ y $A^c$ y $B^c$.

!!! danger "Independencia y eventos disjuntos"
    No debe confundirse los términos **eventos independientes** y **eventos disjuntos**. De hecho, los eventos disjuntos suelen ser muy dependientes por que la ocurrencia de uno implica la no ocurrencia del otro. El único evento que es independiente y ajeno es el vacío $\emptyset$.

