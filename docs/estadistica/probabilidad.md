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
     El conjunto $S$ de todos los resultados posibles de un experimento se denomina **espacio muestral**.

!!! note "Punto muestral"
    Un elemento del espacio muestral $S$ se denomina **punto muestral**. Es un resultado particular.

!!! note "Evento"
    Un evento $A$ es un subconjunto del espacio muestral $S$. Es un conjunto de resultados. Cualquier colección de eventos y cada uno es un subconjunto de $S$ se denominará con $\mathbb{A}$.

!!! note "Evento particular"
    El evento $\lbrace a \rbrace$ constituido por un solo punto $a \in S$ se denomina **evento muestral**.

Considere el experimento de lanzar un dado de 6 caras.

![Representación espacio muestral dados](img/dados.jpg)
Imagen de [anncapictures](https://pixabay.com/es/users/anncapictures-1564471/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2031512) en [Pixabay](https://pixabay.com/es/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2031512).

El espacio muestral estaría formado por los seis números posibles, es decir:

$$ S = \lbrace 1,2,3,4,5,6 \rbrace $$

Sean el evento $A$ que el resultado sea par, el evento $B$ que el resultado sea impar y el evento $C$ que el resultado sea mayor a 3.

Entonces se tiene que 

$$A=\lbrace 2,4,6 \rbrace \\
B=\lbrace 1,3,5 \rbrace \\
C=\lbrace 4,5,6 \rbrace
$$

Observe que el evento $B \cup C = \lbrace 1,3,4,5,6\rbrace$ también es un evento en el espacio muestral $S$.

### Axiomas de probabilidad

Como se mencionó anteriormente, actualmente la probabilidad se estudia de manera formal partiendo de 3 axiomas.

!!! caution "Conocimiento avanzado"
    El estudio de la probabilidad requiere conocimientos avanzados de *Matemáticas* y *Teoría de Conjuntos* los cuales están fuera del alcance de esta página.

Sea $A$ un evento del espacio muestral $S$. Una función $P: \mathbb{A} \rightarrow [0,1]$ es llamada *función de probabilidad* si satisface estas 3 condiciones.

- **Axioma 1**: $0\le P(A) \le 1$ para $A \in \mathbb{A}$
- **Axioma 2**: $P(S) = 1$
- **Axioma 3**: Para cualquier secuencia de eventos $A_1,A_2,\dots$ mutuamente excluyentes, entonces

$$P\left( \bigcup_{i=1}^{\infty} A_i\right)=\sum_{i=1}^{\infty}A_i$$

Se dice que $P(A)$ es la *probabilidad de que ocurra el evento A*.

A partir de esos axiomas, se derivan otras propiedades.

* $P(\empty)=0$.
* Si $A_1,\dots,A_n$ son eventos mutuamente excluyentes, entonces $P\left( \bigcup_{i=1}^{n} A_i\right)=\sum_{i=1}^{n}A_i$.
* $P(A^c)=1-P(A)$.
* Para cualesquiera 2 eventos: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
* Si $A \subset B$, entonces $P(A) < P(B)$.
