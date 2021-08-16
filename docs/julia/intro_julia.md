---
title: Introducción a Julia
summary: Una guía rápida sobre Julia.
authors: Francisco Vázquez
date: 2021-08-13
---

## Inicio

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

## Operadores aritméticos

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

## Ciclos

Se puede realizar un ciclo usando el siguiente código

````julia
for x in 1:10
    println(x)
end
````

!!! Nota
    La función `print()` imprimiría los valores consecutivamente sin espacio, mientras que `println()` los imprime en una línea nueva.

Se debe tomar en cuenta que la palabra `for` debe cerrarse con un  `end` para delimitar el bloque.

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
