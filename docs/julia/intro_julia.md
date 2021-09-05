---
title: Introducción a Julia
summary: Una guía rápida sobre Julia.
authors: Francisco Vázquez
date: 2021-08-13
---

# Inicio

Julia es un poderoso lenguaje de programación enfocado en la potencia y velocidad.

Al iniciar Julia se muestra una pantalla en que es la consola de Julia.

## Variables

Julia tiene varios tipos de variables, por ejemplo tipo numérico (entero y flotante) booleano o caracter. Para conocer todos los tipos de variables que existen, consulte la [documentación](https://docs.julialang.org/en/v1/manual/integers-and-floating-point-numbers/).

Se puede definir una variable usando el operador de asignación `=` como se muestra en el siguiente ejemplo.

````julia
x = 1
y = 1.25
z = x + y
a = "abc"
si = true
````

Para saber de que tipo es, se puede usar la función `typeof()`, el resultado se muestra

````julia
typeof(x)
````

> Int64

## Vectores

La forma de definir vectores es mediante el uso de corchetes cuadrados `[]`, por ejemplo:

````julia
a = [1,2,3]
b = [2,4,5]
````

!!! danger "No confundir con tuplas"
    La forma de definir una tupla es mediante un paréntesis `()`.

Al igual que otros lenguajes de programación, la forma de acceder a sus elementos es mediante el operador `[]` y también con `:` se puede definir una secuencia.

````julia
a[2]
b[1:2]
````

### Operadores aritméticos

Julia soporta diversos operadores aritméticos, la siguiente tabla muestra los principales operadores.

Expresión|Nombre|Descripción
----|------|------
`x + y`|suma|realiza adición
`x - y`|resta|realiza substracción
`x * y`|producto|realiza multiplicación
`x / y`|división|realiza división
`x ÷ y`|división entera|similar a `x/y`, pero truncado a un entero
`x \ y`|división inversa|equivalente a `y/x`
`x ^ y`|potencia|eleva `x` a la potencia `y`
`x % y`|resto|equivalente to `rem(x,y)`

Para una mayor referencia visita la sección[operadores aritméticos](https://docs.julialang.org/en/v1/manual/mathematical-operations/#Arithmetic-Operators).

## Control de flujo

Julia posee estructuras para control de flujo. Se puede realizar un ciclo usando el siguiente código

````julia
for x in 1:10
    println(x)
end
````

!!! Nota
    La función `print()` imprimiría los valores consecutivamente sin espacio, mientras que `println()` los imprime en una línea nueva.

Se debe tomar en cuenta que la palabra `for` debe cerrarse con un  `end` para delimitar el bloque.

Para usar el ciclo while, se usa el siguiente código

````julia
x = 0
while x <= 5 
    println(x)
    x = x + 1
end
````

!!! danger "Ciclo infinito"
    No olvides aumentar el contador con el fin de que se cumpla la condición, de otro modo se entraría en un ciclo infinito.

## Funciones

Para definir una función, se usa la palabra `function` seguido del nombre de la función y entre paréntesis los argumentos.

Se debe especificar la paabra clave `return`, de otro modo retornaría el último valor calculado.

La función termina con un `end` e inmediatamente se compila.

````julia
function signo(x)
    if x < 0 resp = "Negativo"
    elseif x > 0 resp = "Positivo"
        else resp = "Es Cero"
    end
    return resp
end
````

una vez compilada, se puede usar.

````julia
signo(-5)
````

El resultado sería el siguiente

> "Negativo"
