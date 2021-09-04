---
title: Manipulación de variables
summary: Creación de variables, selección de observaciones, estructuras condicionales
authors: Francisco Vázquez
date: 2021-09-03
---

# Manejo de bases

En esta sección se presentan temas más profundos acerca del procesamiento de datos.
Se explorarán distintas formas de manejar variables, seleccionar observaciones así como el uso de cliclos y arreglos que nos permitan tener un mayor control de la información que se tenga.

Primero se verá la forma de crear variables con el fin de realizar cálculos posteriores, estas variables pueden ser usadas incluso para crear varios datasets, crear contadores o acumuladores, entre otras. También se conocerán técnicas de selección de observaciones con el fin de manipular mejor las bases.

Después se explorará un poco el tema del ordenamiento con el fin de crear ya sea grupos o realizar otras operciones como uniones, tranposiciones entre otras.

Antes de continuar con temas mas complejos, es importante comprender de forma general el funcionamiento del paso DATA.

Para una explicación más detallada consulte [Cómo funciona el paso DATA](https://support.sas.com/documentation/cdl/en/basess/58133/HTML/default/viewer.htm#a001290590.htm).

El paso DATA tiene dos fases:

- Fase de compilación
- Fase de ejecución

A continuación se describir´n de forma breve estas fases.

Durante la fase de compilación, SAS revisa la sintaxis y si es correcta, se manda a código máquina en dondese procesa el código y se generan los siguientes objetos:

- **Memoria de entrada**. Es un lugar en la memoria donde SAS lee registros de un archivo de texto cuando el programa se ejecute.
- **Vector de datos del programa**. Es un lugar en la memoria donde SAS construye un conjunto de datos, una observación a la vez.
- **Porción descriptora**. Es la información general del dataset como el nombre de la base y los atributos de las variables a crear.

La memoria de entrada solo aplica en el caso en que se lean archivos externos. En este caso, los datos se leen de la memoria de entrada al vector de datos del programa.

El vector de datos del programa (VDP) es importante porque en éste se realizarían los cálculos de las sentencias de SAS o funciones. Contiene el nombre de todas las variables declaradas o inicializadas. Es como un paso intermedio entre lo que se lee y calcula con lo que se se escribe al dataset. Al inicio de cada iteración los valores en el VDP son iniciados con valor missing y son llenados según lea o ejecuten sentencias.

Durante la fase de compilación tambien se crean dos variables auxiliares en el VDP que no se escribirán en el dataset: `_N_` y `_ERROR_`. La primera cuenta el número de veces que el paso DATA itera y la segunda registra si hubo algún problema en la fase de ejecución.

Una vez concluída esta etapa, se procede a la siguiente fase.

En la fase de ejecución se realizan las siguientes acciones:

1. Se leen las observaciones del VDP.
2. Se ejecutan las sentencias (cálculo de variables).
3. Se escriben al dataset.
4. La variables en el VDP son reiniciadas y se colocan valores missing.

Debido a que es un procesos repetitivo, SAS realiza los pasos mencionados tantas veces como observaciones haya en el archivo externo o dataset leído.

El proceso termina cuando ya no hay registros que leer y en ese momento el dataset es cerrado y se concluye el paso DATA.

## Creando variables

Hasta ahora solo conocíamos las sentencias `ATTRIB`, `LENGTH` y `FORMAT` para declarar o iniciar variables. Otra forma de crearlas es mediante la asignación de variables de la siguiente forma:

> variable = *expresión sas*;

Esta sentencia se conoce como *sentencias de asignación*. Su función es evaluar y almacenar el resultado en alguna variable que está al lado izquierdo del signo `=`.

Una forma muy común de crear variables es mediante el uso de operadores matemáticos. La siguiente tabla muestra algunos de los operadores aritméticos en SAS. Para una referencia consulte [Operadores SAS en expresiones](https://documentation.sas.com/doc/en/lrcon/9.4/p00iah2thp63bmn1lt20esag14lh.htm#n1feyypdf6czp4n15pthf5lafmlf) y [Funciones SAS en expresiones](https://documentation.sas.com/doc/en/lrcon/9.4/p1fjvn4giid9e0n1v0wcn4ibwbzi.htm).

Símbolo|Descripción|Ejemplo|
-------|-----------|-------|
`+`    |Adición    |`fecha + 1`
`-`    |Sustracción|`fecha - 7`
`*`    |Multiplicación|`height * 2.54`
`/`    |División   |`suma / total`
`**`   |Exponenciación|`metros ** 2`

Considere las siguientes sentencias:

````sas
fecha = '10Jun20'd;
version = 1;
status = "ok";
altura = height * 2.54;
nombre2 = SUBSTR(name,1,3);
````

En esas sentencias se han creado las variables simplemente asignando un valor o una expresión SAS. Las primeras tres sentencias crearían variables de tipo numérico; la expresión `'10Jun20'd` es interpretada por sas como un valor numérico. La cuarta sentencia realiza una multiplicación de una variable por una constante. Finalmente, la quinta aplica una función a una variable de tipo caracter que extraerá los 3 primeros caracteres de una cadena.

A continuación se presentan algunas variables que serán muy útiles 

### Variables acumuladoras y contadoras

En SAS es posible crear una variable que sume o vaya acumulando.

Considere la siguiente tabla donde se representan la información de los empleados de una compañía. Se desea obtener un acumulado de las ventas de los empleados y un contador para tener en cuenta el número de empleados.

![Datos del ejemplo](img/ejemplo1.png)

El siguiente código muestra la forma de crear el acumulador y el contador de forma muy básica.

````sas
DATA ventas_au2;
    SET ventas_au;
    contador = _N_;
    salario_acum + salary;
RUN;
````

La tercer línea guarda el número de veces que se ha iterado, es decir el número de registros leídos. Debido a que la variable `_N_` es temporal y no se escribe en el dataset, se guarda en la variable _contador_.

En la cuarta se muestra cómo acumular en la variable *salario_acum*, en cada iteración se le suma la variable *salary* a la variable *salario_acum*. Esta sentencia es conocida como [sentencia SUM](https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/lestmtsref/n1dfiqj146yi2cn1maeju9wo7ijs.htm).

!!! error "Cuidado con el operador +"
    Se debe tener cuidado al usar el operador `+` debido a que si alguno de los operandos tiene un valor _missing_, el resultado sería _missing_. Se recomienda usar la [función SUM](https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/lefunctionsref/n0zxive1z1ctqin12w06c85jfigd.htm) para evitar esos imprevistos.

Si se hubiese definido `salario_acum = salario_acum + salary`en la línea 4, el resultado en cada observacion nos resultaría un valor _missing_. Como se mencionó previamente, durante la fase de compilación los valores en el VDP se reinician a valor _missing_ causando que el resultado en dicha expresión sea _missing_.

Para evitar que eso ocurra, se puede usar la sentencia `RETAIN` con el fin de que SAS conserve el valor en cada iteración.

````sas
DATA ventas_au2;
    SET ventas_au;
    RETAIN salario_acum2 0;
    salario_acum2 = salario_acum2 + salary; 
RUN;
````

En la línea 3 se pide que SAS retenga la variable _salario_acum2_ en cada iteración y que su valor inicial sea 0. De esta manera se podría sumar de manera normal. Consulte la [sentencia RETAIN](https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/lestmtsref/p0t2ac0tfzcgbjn112mu96hkgg9o.htm) para más información.

### Funciones

### Formatos

## Filtrado de datos

En ocasiones, se tiene una basta cantidad de datos y solo nos interesa un subconjunto de estos. Para eso se pueden elegir observaciones de un dataset con la sentencia `WHERE`.

!!! caution "WHERE vs IF"
    No debe confundirse la sentencia `WHERE` con `IF`. La sentencia `IF` trabaja con observaciones _después_ de ser leídas en el VDP, mietras que `WHERE` selecciona las observaciones _antes_ de pasar al VDP.

La sintaxis es la siguiente:

> WHERE _expresión_;

donde _expresión_ es una condición a evaluar, vea la sección [selección de observaciones](#seleccion-de-observaciones) para una referencia de los operadores lógicos y booleanos. La siguiente tabla muestra expresiones válidas para la sentencia `WHERE`

Operador|Descripción|Ejemplo
--------|-----------|-------
`BETWEEN - AND`|Un rango inclusivo| `WHERE age BETWEEN 12 AND 15;`
`?` o `CONTAINS`|Una cadena de caracteres|`WHERE name ? "Ja";`
`IS NULL` o `IS MISSING`|Valores faltantes|`WHERE volumen IS NULL;`
`LIKE`|Combinación de patrones|`WHERE name LIKE "J%";`
`=*`|Suena como (Sólo palabras en inglés)|`WHERE name =* "jeims";`
`SAME - AND`|Agrega cláusulas a una sentencia `WHERE` existente|`WHERE sex = "F"; WHERE SAME AND age >= 13;`

En el siguiente ejemplo se muestra el filtrado usando la sentencia `WHERE` usando los datos de [covid](#leyendo-archivos-desde-web) para tener sólo la información de México.

````sas
DATA mexico;
    SET covid;
    WHERE iso_code EQ "MEX";
RUN;
````

El log muestra el siguiente mensaje:

> NOTE: There were 609 observations read from the data set WORK.COVID.
>      
> WHERE iso_code='MEX'

Si se hubiese usado la sentencia `IF` en lugar de `WHERE` el resultado hubiera sido el siguiente:

> NOTE: There were 113406 observations read from the data set WORK.COVID.
>    
> NOTE: The data set WORK.MEXICO has 609 observations and 60 variables.

El ejemplo anterior muestra las diferencias entre las sentencias `IF` y `WHERE`.

!!! tip "`WHERE` como opción de dataset"
     Es posible usar la opción `WHERE =` para filtrar observaciones para un dataset especificado, esto es útil cuando se leen más de un dataset. Vea la [documentación](https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/ledsoptsref/p0ny9o8t8hc5zen1qn3ft9dhtsxx.htm) para más información.

### Sentencias condicionales

Anteriormente se había usado la sentencia `IF` para seleccionar variables, ahora se usará en conjunto con la palabra `THEN` con el fin de que realice una acción. Esta sentencia se conoce como sentencia **IF-ELSE**.

La sintaxis es la siguiente:

> IF _expresión_ THEN _acción1_; ELSE _acción2_;

El siguiente ejemplo muestra cómo crear una variable a partir de ciertos valores.

````sas
DATA clase;
    SET SASHELP.CLASS;
    LENGTH sexo $8;
    IF sex = "F" THEN sexo = "Mujer";
    ELSE sexo = "Hombre";
RUN;
````

Note que la sentencia `IF-ELSE` solo permite una acción a la vez. Para realizar más de una acción se debe usar el bloque `DO`. Consulte la [documentación](https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/lestmtsref/n0el0y2a02ab1ln1pks3gbac1en3.htm) para más información.

````sas
DATA clase;
    SET SASHELP.CLASS;
    sexo = "Hombre";
    genero = "Masculino";
    IF sex = "F" THEN DO;
        sexo = "Mujer";
        genero = "Femenino";
    END;
RUN;
````

Estas sentencias pueden anidarse para formar sentencias más complejas, por ejemplo.

````sas
DATA clase;
   SET SASHELP.CLASS;
   LENGTH escuela $12.;
   IF age LE 12 THEN escuela = "Primaria";
      ELSE IF age GE 16 THEN escuela = "Preparatoria";
   ELSE escuela = "Secundaria";
RUN;
````

!!! caution "Cuidado con las estructuras anidadas"
    Se debe tener cuidado al usar sentencias anidadas ya que deben ser cerradas correctamente. De no ser así, se pueden cometer errores.

Otra forma de crear sentencias condicionales es mediante el uso de la sentencia `SELECT`. Consulte la [ayuda](https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/lestmtsref/p09213s9jc2t99n1vx0omk2rh9ps.htm) para más información.

````sas
DATA clase;
   SET SASHELP.CLASS;
   LENGTH escuela $12.;
   SELECT;
      WHEN (age LE 12) escuela = "Primaria";
      WHEN (age GE 16) escuela = "Preparatoria";
      OTHERWISE escuela = "Secundaria";
   END;
RUN;
````

!!! note "No confundirse"
    Esta sentencia no debe confundirse con la sentencia [SELECT de SQL](https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/sqlproc/p0hwg3z33gllron184mzdoqwpe3j.htm). Para hacer algo similar en SQL, revise este [ejemplo](https://vazquez-chavez-francisco-ariel.gitbook.io/notas/consultas-basicas#creacion-de-nuevas-columnas).

## Ciclos

## Arreglos

## Manipulación y transformación de bases
