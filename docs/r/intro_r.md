---
title: Introducción a R
summary: Una guía rápida sobre R.
authors: Francisco Vázquez
date: 2020-02-05

---

Este es un tutorial básico sobre el programa. Visite la página de [R](https://www.r-project.org/) para más información.

## Conceptos básicos

R es un lenguaje de programación que usa objetos. Estos objetos tienen identidad, atributos y propiedades.

Tambien puede considerarse como un intérprete, es decir que espera acciones del usuario. Cuando el usuario ejecuta comandos, R los ejecuta línea por línea.

Los **comandos** o **expresiones** más comunes son las asignaciones, es decir se asigna un valor a una variables. Cada comando suele escribirse en una sola línea o terminar con punto y coma.

R es un lenguaje sensible a mayúsculas y minúsculas, esto es un factor a tomar en cuenta para evitar errores.

!!! tip "Interaz gráfica"
    R tiene una interfaz gráfica para crear código de forma más amigable. Visite [R Studio](https://rstudio.com/) para más información.

Cuando se inicia una sesión, se asigna un espacio de trabajo (workspace) en memoria y un directorio de trabajo (working directory).

El espacio de trabajo sirve para almacenar objetos creados, tales como vectores, funciones entre otros.

Para conocer el directorio de trabajo puede escribir en consola:

````r
getwd()
````

Para cambiar use la función `setwd("dir")`, donde *dir* es el nuevo directorio.

!!! caution "Barras verticales"
    R no reconoce una sola barra `/` en los directorios de windows. Use doble barra  `//` o una barra invertida `\`.

### Escalares

Un escalar es un vector con un solo elemento.

Se pueden crear escalares con el símbolo de asignación `<-` o `=`.

````r
n <- 5
m = n + 1
a = "Hola mundo!"
````

Los escalares son útiles para guardar algún valor. Pueden ser considerados como una variable.

También puede haber escalares lógicos o booleanos, por ejemplo si se construye `nm = n>m` su valor sería:

> [1] FALSE

### Vectores

Un vector es un objeto con uno o más elementos. Puede contener elementos numéricos o caracteres.

Se pueden crear vectores con la función `c()`, por ejemplo:

````r
x = c(2,1,5)
z = c("ABC","AEI","XYZ")
````

Los vectores permiten algunas operaciones, las más comunes son la suma `+`, resta `-`,  multiplicación `*`, división. `/` y potencia `^`.

````r
y = m*x+n
````

!!! Note "Operación entre vectores"
    Las operaciones entre vectores son elemento a elemento. Si los elementos no tuvieran el mismo tamaño, el de menor tamaño se recicla (repite sus elementos) hasta tener el mismo número de elementos.

Por ejemplo, la operación `nx = n + x` dará como resultado:

> [1]  7  6 10

Los vectores tienen una dimensión y para conocerla se puede usar la función `length()`. Por ejemplo `length(x)` nos daría como resultado:

> [1] 3

ya que sus elementos son:

> [1] 2 1 5

También se puede acceder a sus elementos mediante el operador `[]`, por ejemplo para conocer el segundo elemento de _x_ se puede usar `x[2]` y el resultado es:

> [1] 1

Para acceder a más de un elemento, es posible apuntar a la posición del elemento, por ejemplo `x[c(1,2)]` o `x[1:2]`.

En ambos, el resultado sería:

> [1] 2 1

El operador `:` sirve para indicar una secuencia consecutiva. Por ejemplo `i = 1:10` crearía un vector de 10 elementos del 1 al 10, esto es útil para crear sucesiones o índices.

Para crear secuencias más complejas se puede usar la función `seq()`.

Por ejemplo con `seq(from = 1,to = 10,by = 1)` se crea una secuencia del 1 al 10 incrementando el valor en 1 y se obtiene el mismo resultado que con `1:10`.

Otra forma de crear un vector es mediante la función `rep()`. Por ejemplo la siguiente expresion:

````r
u = rep(x = x,each = 2,times = 3)
````

Crea un el vector _u_ que contiene cada elemento del vector _x_ 2 veces y esta secuencia se recrea 3 veces.

> [1] 2 2 1 1 5 5 2 2 1 1 5 5 2 2 1 1 5 5

### Matrices

Una matriz es una arreglo de dos dimensiones (renglones y columnas) que contiene valores, especialmente numéricos. Tiene _n_ renglones y _p_ columnas, es decir tiene _np_ elementos.

Para crea una matriz, se usa la función `matrix()` cuya sintaxis es la siguiente:

> matrix(**data** = objeto, **nrow** = valor, **ncol** = valor _<, **byrow** = FALSE>_)

donde **data** representa un vector o una expresión, **nrow** el número de renglones que se desean, **ncol** el número de columnas y el argumento opcional **byrow** indica si se deberían llenar por columnas.

Si se ejecuta el siguiente comando:

````r
A1 = matrix(data = u)
````

el resultado sería una matriz de 18 renglones y una columna.

Si se desea una matriz de otra dimensión se puede usar este código.

````r
A1 = matrix(data = u,nrow = 6,byrow = TRUE)
````

### Factores

### Data Frames

### Listas
