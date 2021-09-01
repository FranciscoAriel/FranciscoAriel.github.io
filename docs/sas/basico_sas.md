---
title: SAS básico
summary: Conociendo SAS.
authors: Francisco Vázquez
date: 2020-09-26
---

En esta sección se presentan temas para comenzar con la lectura y procesamiento de datos, así como la creación de reportes y agregados que permitan tner una idea general de los datos que se están trabajando.

## Lectura de datos

Los dataset son el insumo principal para analisis de datos en SAS, por ello iniciaremos con una rápida exploración.

La creación de un dataset inicia con un bloque `DATA` y termina con un `RUN`.

### Introducción de valores de forma manual

La forma más fácil de crear un dataset, es con el uso de la sentencia `INPUT` y `DATALINES` con el fin de introducir valores manualmente. Estos datos fueron copiados y pegados directamente de una hoja de excel.

El siguiente ejemplo muestra como introducir datos manualmente.

````sas
DATA EMPLEADOS(LABEL = "Registro de empleados nuevos");
    ATTRIB
        NOMBRE LENGTH = $16 LABEL = "Nombre"
        APELLIDO LENGTH = $12 LABEL = "Apellido"
        ID LABEL = "ID empleado"
        GENERO LENGTH = $1. LABEL = "Género"
        FNAC INFORMAT = DDMMYY10. FORMAT = DATE10. LABEL = "Fecha de nacimiento"
    ;
    INPUT NOMBRE -- FNAC;
    DATALINES;
    Bill Cuddy 11171 M 16/10/1986
    Susan Krasowski 17023 F 09/07/1959
    Andreas Rennie 26148 M 18/07/1934
    Lauren Krasowski 46966 F 24/10/1986
    Lauren Marx 54655 F 18/08/1969
    Tommy Mcdonald 70046 M 20/01/1959
    Colin Byarley 70059 M 20/01/1934
    Lera Knott 70079 F 11/07/1986
    Wilma Yeargan 70100 F 23/06/1984
    Patrick Leach 70108 M 14/04/1939
    Portia Reynoso 70165 F 11/02/1964
    Soberina Berent 70187 F 27/09/1986
    Angel Borwick 70201 F 19/12/1969
    Alex Santinello 70210 M 22/04/1986
    Kenan Talarr 70221 M 10/02/1964
    ;
RUN;
````

La sentencia `DATA` especifica el nombre del dataset y entre parentesis están las opciones del dataset, en este caso el dataset *empleados* tendrá una etiqueta para identificarlo.

Es recomendable especificar las propiedades de las variables a crear mediante la sentencia `ATTRIB` en donde se especifican sus propiedades.

!!! info "Declaración de variables"
    Otra forma de declarar variables es mediante las sentencias `LENGTH` y `FORMAT`. Consulte la documentación para más información.

Nótese que para el caso de las variables de tipo caracter se hace uso de la opción `LENGTH =` seguido del signo de pesos para indicar que es de tipo caracter y la longitud deseada. Para el caso de variables numéricas, se debe especificar al menos un atributo, en este caso se recomienda especificar el atributo `LABEL =`. En el caso de la variable *fnac* los datos estan almacenados en formato de fecha (ddmmyyyy) por lo que se usa el informato `ddmmyy10.` para que lo reconozca como fehca de sas, pero se desea visualizar con el formato de fecha (ddmmmyyyy).

La sentencia `INPUT` sirve para indicar el nombre de las variables del dataset. Se puede poner el símbolo `$` para indicar que la variable es de tipo caracter. Sin embargo en este caso, como ya se han declarado las variables se puede usar una lista, es decir, solo poner el nombre de la primer variable declarada seguido de dos guiones `--` y el nombre de la última.

La sentencia `DATALINES` indica el inicio de los datos y finaliza con un punto y coma.

Con la sentencia `RUN` se cierra el bloque de instrucciones y comienza a ejecutar el proceso.

### Lectura de datos desde un archivo externo

SAS puede leer datos de archivos de texto almacenados en distintos formatos, por ejemplo de ancho fijo o delimitados. Para acceder a ellos es necesario usar la referencia para apuntar a ellos, algo similar a la declaración de las librerías.

Se puede hacer mediante la sentencia `FILENAME`:

> **FILENAME** *fileref* '*nombre-archivo*';

donde *fileref* es un nombre sas que hará referencia a un archivo y *nombre-archivo* es el nombre de un archivo físico externo que incluye tanto la ruta como el nombre con su extensión.

Por ejemplo la siguiente sentencia asigna con el nombre *archivo* al archivo "datos" almacenados en formato .dat que están en la carpeta proyectos.

````sas
FILENAME archivo "C:\Users\Usuario\Documents\Proyectos\datos.dat";
````

También será necesario usar la sentencia `INFILE`. Esta sentencia le da las espeficicaciones a SAS sobre cómo leer archivos externos. Para una mayor referencia consulte la [sentencia INPUT](https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/lestmtsref/n1rill4udj0tfun1fvce3j401plo.htm).

#### Lectura de un archivo de ancho fijo

En ocasiones se tienen los datos almacenados en formato de texto pero los datos estan alineados de tal forma que es posible saber en que posición inicia cada variable.

![Ejemplo de un archivo en formato de texto de ancho fijo](img/fijo.png)

El ejemplo anterior muestra un ejemplo de un archivo de texto de ancho fijo, obsérvese que el id comienza en la columna 1 mientras que el nombre inicia en la columna 8.

El siguiente código muestra cómo leer datos de un archivo de ancho fijo.

````sas
DATA VENTAS;
INFILE ARCHIVO;
INPUT ID 1 - 7 NOMBRE $ 8 - 18 APELLIDO $ 19-33 POSICION $ 34 - 53 VOLUMEN 54 - 60 PAIS $ 61-62;
RUN;
````

La diferencia con ejemplos anteriores es la sentencia `INFILE`. Esta sentencia especifica que se va leer un archivo externo y se usa junto con la sentencia `INPUT`.

En la sentencia `INPUT` se declaran las variables que va a contener el dataset **VENTAS**. SAS leerá el archivo línea por línea y almacenará los valores que encuentre en la variable declarada según la posición indicada, por ejemplo los valores que encuentre de la línea 1 a la 7 se guardarán en la variable *ID*, mientras que los valores de la columna 8 a la 18 se almacenarán en la variable *NOMBRE*, nótese que después de *NOMBRE* hay un signo de pesos, esto es para indicar que la variable es de tipo caracter.

!!! danger "Cuidado con las posiciones de columna"
    Se debe ser muy cuidadoso al especificar la posición de las columnas para no mezclar los valores.
    En el ejemplo anterior, si se hubiera declarado `VOLUMEN 54 - 61`, SAS hubiera considerado la columna 61 y nos mostraría un mensaje en el log:
    ![Error en la lectura de datos](img/error1.png)
    Debido a que la columna 61 contiene a la letra A, SAS estaría almacenando una cadena en una variable numérica, por lo que lo que nos mostraría el error y finalmente le asignaría un valor missing a *volumen*.

Una forma alternativa de declarar las variables en la sentencia sería usar el siguiente código:

````sas
DATA VENTAS;
INFILE ARCHIVO;
INPUT ID NOMBRE $10. APELLIDO $ 19-33 POSICION $ 34 - 53 VOLUMEN PAIS $3.;
RUN;
````

Note que en la sentencia `INPUT` se declaran a las variables de tipo caracter de dos formas: por posición (ejemplo `APELLIDO $ 19-33`) y por formato (ejemplo `NOMBRE $10.`).

Para una mayor referencia consulte [leyendo datos en bruto](https://support.sas.com/documentation/cdl/en/lrcon/62955/HTML/default/viewer.htm#a003209907.htm#:~:text=The%20INPUT%20statement%20reads%20raw%20data%20from%20instream,styles%20of%20input%20in%20a%20single%20INPUT%20statement.) en la documentación de SAS.

#### Lectura de un archivo de texto delimitado

El delimitador predeterminado es un espacio en blanco. Sin embargo, los archivos de texto delimitados por otros caracteres (por ejemplo una coma, tabulador, o símbolos especiales) tambien pueden ser leídos por SAS. Para especificar el tipo de delimitador, se utiliza la opción `DLM =` en la sentencia `INFILE`.

Considere el siguiente archivo de texto. Puede notarse que está delimitado por el caracter "/" y además tiene datos perdidos (resaltados en amarillo). De hecho, los valores perdidos al final de la línea podrían hacer que SAS terminara antes de leer los datos.

![Archivo de texto delimitado](img/dat1.png)

El siguiente código puede ser usado para leer esos datos.

````sas
DATA gerentes;
    INFILE ARCHIVO DLM = "/" DSD TRUNCOVER;
    ATTRIB
        id label = "ID gerente"
        nombre LENGTH = $12 LABEL = "Nombre"
        apellido LENGTH = $18 LABEL = "Apellido"
        genero LENGTH = $2 LABEL = "Género"
        ventas LABEL = "Ventas totales"
        posicion LENGTH = $18 LABEL = "Posición"
        pais LENGTH = $2 LABEL = "País" 
        fnac INFORMAT = date12. FORMAT = ddmmyy10. LABEL = "Fecha de nacimiento"
        fingreso INFORMAT = anydtdte12. FORMAT = ddmmyy10. LABEL = "Fecha de ingreso"
    ;
    INPUT id -- fingreso;
RUN;
````

La opción `DSD` es útil cuando hay un valor faltante en datos delimitados, de otra forma SAS no reconocería dos delimitadores juntos y no leería los datos correctamente.

La opción `MISSOVER` evita que SAS salte a una nueva linea cuando no encuentra valores válidos y asigna valores faltantes a las variables que no encuentre. `TRUNCOVER` funciona de manera similar a `MISSOVER` pero la diferencia radica en que asignaría los valores que encuentre pasando el fin de línea.

#### Leyendo archivos desde web

Para leer datos desde internet (usualmente en formato csv) se debe especificar el nombre del archivo con la sentencia FILENAME con la opción `URL`.

> **FILENAME** *fileref* URL '*nombre-archivo*' *< opciones-url >*;

Un ejemplo para descargar datos de covid se encuentran en el siguiente programa de sas: [datos_covid_web.sas](src/datos_covid_web.sas).

Consulte la documentación de la sentencia `FILENAME` con el [método de acceso URL](https://documentation.sas.com/doc/es/pgmsascdc/9.4_3.5/lestmtsglobal/p103pi2vrzn6qhn1e8alrs01jrb7.htm) para más información.

### Selección de observaciones

Es posible seleccionar las observaciones que se quieren escribir en un dataset, sobre todo aquellas que _cumplan ciertas condiciones_. Al igual que otros lenguajes de programación SAS tiene expresiones lógicas que evalúan cierta condición.

La sintaxis es la siguiente:

> IF _expresión_;

Esta sentencia nos permite continuar procesando aquellas observaciones que cumplen la condición, generalmente de comparación.

Una expresión puede ser el nombre de una varible y puede contener algún operador lógico y un operando. Pueden conectarse mediante conectores lógicos, comunmente llamados booleanos.

La siguiente tabla resume algunos operadores lógicos y conectores.

Símbolo                   |Descripción|Ejemplo|
--------------------------|-----------|-------|
`=` o `EQ`                |IGUAL A    |`sex EQ "F"`
`^=` o `¬=` o `~=` o `NE` |NO IGUAL A |`sex NE "F"`
`>` o `GT`                |MAYOR QUE  |`age GT 13`
`<` o `LT`                |MENOR QUE  |`age LT 13`
`>=` o `GE`               |MAYOR O IGUAL A|`age GE 14`
`<=` o `LE`               |MENOR QUE O IGUAL A|`age LE 14`
`IN`                      |(ESTÁ) EN   |`age in (12 14 15)` o `sex in ("F" "M")`
`&` o `AND`               |Y          | `sex EQ "F" AND age GT 13`
`!` o `OR` o              |O          |`sex EQ "F" OR age GT 13`
`~` o `^` o `¬` o `NOT`   |NO         |`NOT(sex EQ "F" OR age GT 13)`

Por ejemplo el siguiente código solo contendría a empleados de Australia.

````sas
DATA VENTAS_AU;
    INFILE ARCHIVO;
    IF PAIS EQ "AU";
    INPUT ID 1 - 7 NOMBRE $ 8 - 18 APELLIDO $ 19-33 POSICION $ 34 - 53 VOLUMEN 54 - 60 PAIS $ 61-62;
RUN;
````

Para elegir observaciones que no sean nulas, se puede usar la siguiente sentencia.

````sas
DATA VENTAS_AU;
    INFILE ARCHIVO;
    IF VOLUMEN;
    INPUT ID 1 - 7 NOMBRE $ 8 - 18 APELLIDO $ 19-33 POSICION $ 34 - 53 VOLUMEN 54 - 60 PAIS $ 61-62;
RUN;
````

### Usando un procedimiento para leer datos externos

La forma más fácil de leer archivos externos es mediante el procedimiento **IMPORT**.

> **PROC IMPORT** DATAFILE = "filename" OUT = dataset;

Este procedimiento no solo lee archivos de texto, sino tambien de Excel, SPSS, Stata e incluso tablas de Access. Para una mayor referencia vea el [procedimiento IMPORT](https://documentation.sas.com/doc/es/pgmsascdc/9.4_3.5/proc/n1qn5sclnu2l9dn1w61ifw8wqhts.htm).

El siguiente código leerá un archivo en formato excel.

````sas
PROC IMPORT OUT = WORK.censo 
            DATAFILE = "C:\Users\Usuario\census.xlsx" 
            DBMS = XLSX REPLACE;
RUN;
````

Nótese que se ha especificado la opción `DBMS = XLSX` para que sas utilice los parámetros correspondientes para leer un archivo de excel. La opción `REPLACE` reemplazaría el dataset que tuviera el mismo nombre, de otro modo SAS mostraría un error y no crearía el dataset.

El siguiente código muestra cómo leer un archivo en formato csv.

````sas
PROC IMPORT OUT = WORK.census 
            DATAFILE = "C:\Users\Usuario\census.csv" 
            DBMS = CSV REPLACE;
     GETNAMES = YES;
     DATAROW = 2; 
RUN;
````

En el caso de archivos csv, hay dos sentencias adicionales, la sentencia `GETNAMES = YES` indica si los nombres de las variables se encuentran al inicio del archivo de texto, mientras que la sentencia `DATAROW = 2` indica que los valores incian en el renglón 2.

## Escritura a un archivo externo

SAS tambien puede ser utlizado para escribir archivos externos. En esta sección se mostrará como crear archivos de texto, asi como escribir mensaje del log a archivos externos.

### Escritura de un archivo delimitado

El siguiente código muestra como crear un archivo de texto.

````sas
FILENAME archivo "C:\Users\Usuario\alumnos.dat";
    DATA _NULL_;
    FILE archivo;
    SET sashelp.class;
    PUT name age sex;
RUN;
````

Como se puede ver, se ha referenciado con la sentencia `FILENAME` el archivo con el nombre que en el que se desea escribir.

Nótese que en la sentencia `DATA` se ha especificado `_NULL_`, una palabra reservada para pedir que no cree ningún dataset.

La sentencia `FILE` da las especificaciones para escribir los archivos de texto. Es muy similar a la sentencia `INFILE`, para mayor referencia consulte la [sentencia FILE](https://documentation.sas.com/doc/es/pgmsascdc/9.4_3.5/lestmtsref/n15o12lpyoe4gfn1y1vcp6xs6966.htm).

Finalmente, la sentencia `PUT` indica lo que se va a escribir en el archivo externo, en este caso se especifican la variables de interés. Para una mayor referencia consulte la [sentencia PUT](https://documentation.sas.com/doc/es/pgmsascdc/9.4_3.5/lestmtsref/n1spe7nmkmi7ywn175002rof97fv.htm).

!!! tip "Archivos delimitados por un caracter"
    SAS crea archivos delimitados por un espacio en blanco. Para crear un archivo delimitado por otro caracter (por ejemplo una coma) se puede usar la opción `DLM =`. Tambien se puede modificar la extensión del archivo con la sentencia `FILENAME`.

El resultado sería el siguiente.

![Ejemplo de un archivo de texto delimitado por espacios en blanco](img/dat2.png)

### Escritura de un archivo de texto de ancho fijo

Para crear un archivo de texto de ancho fijo, se puede especificar las posiciones en las que se escribiran las observaciones.

````sas
FILENAME archivo "C:\Users\Usuario\alumnos.txt";
DATA _NULL_;
    FILE archivo;
    SET sashelp.class;
    PUT name $8. sex 10-12 age 2. height 16-20 weight 22-25;
RUN;
````

Nótese que se han especificado los formatos de las variables y las columnas en las que se desea escribir el archivo, es algo muy similar cuando se leían los archivos con la sentencia `INPUT`.

### Crear archivos con encabezados

Debido a que sas escribe directamente al archivo, es un poco complicado especificarle que en el renglón 1 escriba el nombre de las variables.

Sin embargo, el siguiente código logra especificar el nombre de los archivos en la primer línea.

````sas
FILENAME archivo "C:\Users\Usuario\alumnos.txt";
DATA _NULL_;
    FILE archivo;
    IF _n_ EQ 1 THEN PUT "name " "sex " "age " "height " "weight ";
    SET sashelp.class;
    PUT name -- weight;
RUN;
````

Esto se logra escribiendo la sentencia `PUT` justo al inicio e inmediatamente despues se carga el dataset que se quiere escribir.

Las sentencias de la línea 4 se estudiarán en la siguente [sección](#creacion-y-manipulacion-de-datos)

### Leer y modificar archivos de texto

Es posible manipular archivos de texto mediante SAS. para ellos es necesario leerlos y volver a escribir sobre ellos.

![Arcivo de ancho fijo](img/txt1.png)

El siguiente código muestra como actualizar ciertas variables.

````sas
FILENAME ARCHIVO "C:\Users\Usuario\alumnos.txt";
DATA _NULL_;
   INFILE archivo SHAREBUFFERS  FIRSTOBS = 2 TRUNCOVER;
   ATTRIB
    sex LENGTH = $1
    sex2 LENGTH = $1;
   INPUT sex $ 9; 
   IF sex = "F" THEN sex2 = "M";
   IF sex = "M" THEN sex2 = "H";
   FILE archivo TRUNCOVER PAD;
   PUT sex2 9 ;
RUN;
````

Note que se la sentencia `LIBNAME` apunta al mismo archivo que se está usando en las sentencias `INFILE` y `FILE`.

La opción `SHAREBUFFERS` es útil para actualizar un archivo externo y solo actualiza ciertos campos. Esta opción se usa junto con las sentencias `INFILE`, `FILE` y `PUT`.

La variable *sex2* se usa para guardar el valor que se va a escribir en el archivo cuando *sex* toma cierto valor.

!!! error "Cuidado con las longitudes"
    Se debe tener cuidado cuando se actualiza un archivo de texto. Se debe procurar que la variable que se lee como la que se escribe tengan la misma longitud, de otro modo pueden haber resultados inesperados.

El resultado se muestra a continuación

![Archivo de ancho fijo resultante](img/txt2.png)

### Escritura de datos con el procedimiento EXPORT

Así como es posible leer datos de forma externa con un procedimiento, tambien hay uno para escribir datos a archivos externos. La sintaxis es muy similar.

> **PROC EXPORT** OUTFILE = “filename” DATA = dataset;

El siguiente código muestra la forma de escribir un dataset a un archivo csv.

````sas
PROC EXPORT DATA= SASHELP.Class 
            OUTFILE= "C:\Users\Usuario\alumnos.csv" 
            DBMS = CSV REPLACE;
RUN;
````

Para mayores referencias consulte el [procedimiento EXPORT](https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/proc/n045uxf7ll2p5on1ly4at3vpd47e.htm).

## Creación de variables y manipulación de datos

En esta sección conoceremos la forma de crear variables con el fin de crear variables o variables auxiliares para cálculos posteriores. También se conocerán técnicas de selección de observaciones con el fin de manipular mejor las bases.

### Funcionamiento del paso DATA

Antes de continnuar con temas mas complejos, es importante comprender de forma general el funcionamiento del paso DATA.

Para una explicación más detallada consulte [Cómo funciona el paso DATA](https://support.sas.com/documentation/cdl/en/basess/58133/HTML/default/viewer.htm#a001290590.htm).

El paso DATA tiene dos fases:

- Fase de compilación
- Fase de ejecución

A continuación se describir´n de forma breve estas fases.

#### Fase de compilación

Durante la fase de compilación, SAS revisa la sintaxis y si es correcta, se manda a código máquina en dondese procesa el código y se generan los siguientes objetos:

- **Memoria de entrada**. Es un lugar en la memoria donde SAS lee registros de un archivo de texto cuando el programa se ejecute.
- **Vector de datos del programa**. Es un lugar en la memoria donde SAS construye un conjunto de datos, una observación a la vez.
- **Porción descriptora**. Es la información general del dataset como el nombre de la base y los atributos de las variables a crear.

La memoria de entrada solo aplica en el caso en que se lean archivos externos. En este caso, los datos se leen de la memoria de entrada al vector de datos del programa.

El vector de datos del programa (VDP) es importante porque en éste se realizarían los cálculos de las sentencias de SAS o funciones. Contiene el nombre de todas las variables declaradas o inicializadas. Es como un paso intermedio entre lo que se lee y calcula con lo que se se escribe al dataset. Al inicio de cada iteración los valores en el VDP son iniciados con valor missing y son llenados según lea o ejecuten sentencias.

Durante la fase de compilación tambien se crean dos variables auxiliares en el VDP que no se escribirán en el dataset: `_N_` y `_ERROR_`. La primera cuenta el número de veces que el paso DATA itera y la segunda registra si hubo algún problema en la fase de ejecución.

Una vez concluída esta etapa, se procede a la siguiente fase.

#### Fase de ejecución

En esta fase se realizan las siguientes acciones:

1. Se leen las observaciones del VDP.
2. Se ejecutan las sentencias (cálculo de variables).
3. Se escriben al dataset.
4. La variables en el VDP son reiniciadas y se colocan valores missing.

Debido a que es un procesos repetitivo, SAS realiza los pasos mencionados tantas veces como observaciones haya en el archivo externo o dataset leído.

El proceso termina cuando ya no hay registros que leer y en ese momento el dataset es cerrado y se concluye el paso DATA.

### Creación de variables

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

### Filtrado de datos

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
     Es posible usar la opción `WHERE =` para filtrar observaciones para un dataset especificado, esto es útil cuando se leen más de un dataset. Vea la [documentación](https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/ledsoptsref/p0ny9o8t8hc5zen1qn3ft9dhtsxx.htm) para mayor información

## Creación de reportes

SAS es una herramienta muy útil para crear reportes de datos, algunos de ellos se pueden personalizar o adaptarlos a distintas necesidades.

### Reportes básicos

El reporte más simple que se puede crear, es mostrar el conjunto de datos usando el procedimiento `PROC PRINT`.

Sin embargo, para datasets muy grandes, esto no sería una buena opción debido a que SAS gastaría muchos recursos en imprimir toda la tabla. Se pueden usar ciertas configuraciones para que SAS solo procece cierta cantidad de observaciones de un dataset.

La primera de ellas es mediante las *opciones generales*, la cual afectaría a todos los procedimientos durante la sesión o mediante las *opciones de dataset* la cual solo aplica durante ese procedimiento. Para una referencia completa sobre las opciones generales, visite el [diccionario de opciones del sistema](https://documentation.sas.com/doc/es/pgmsascdc/9.4_3.5/lesysoptsref/p1tmgku1vq7pwqn1iqioeflxgec1.htm) y para las opciones de dataset vea el [diccionario de opciones de datasets](https://documentation.sas.com/doc/es/pgmsascdc/9.4_3.5/ledsoptsref/p1pczmnhbq4axpn1l15s9mk6mobp.htm).

El siguiente ejemplo muestra las primeras diez observaciones del conjunto de datos de baseball, pero solo pedimos que muestre ciertas variables.

````sas
PROC PRINT DATA = SASHELP.BASEBALL(OBS=10);
    VAR NAME TEAM NHOME SALARY;
RUN;
````

Produce el siguiente resultado

![Mostrando 10 observaciones](img/print1.png)

### Un reporte con seleccionando casos con total

**PROC PRINT** tambien tiene diversas sentencias para hacer reportes más completos o específicos.

````sas
TITLE "Reporte del equipo San Francisco";
PROC PRINT DATA = SASHELP.BASEBALL NOOBS;
    VAR NAME NHOME SALARY;
    WHERE TEAM EQ "San Francisco";
    FORMAT SALARY DOLLAR12.;
    LABEL 
        NAME = "Nombre del jugador"
        NHOME = "Número de Home Runs en 1986"
        SALARY = "Salario en 1987 (Miles de dólares)"
    ;
    SUM NHOME SALARY;
RUN;
TITLE;
````

El anterior ejemplo muestra un reporte que incluye el nombre de todos los jugadores del equipo *San Francisco*, número de home run ysu salario; al final del reporte se presenta el gran total de estas variables. En este ejemplo se modificaron las etiquetas y los formatos, pero sólo para el reporte mediante las sentencias `LABEL` y `FORMAT` y se seleccionaron las observaciones que cumplieran cierto criterio.

La opción `NOOBS` en la sentencia `DATA` pide no imprimir el número de observación del dataset y con la opción `LABEL` se mostrarán las etiquetas de las variables.

La sentencia `VAR` especifica las variables a mostrar.

La sentencia `WHERE` selecciona las observaciones que cumplan la condición de que el equipo sea igual a *San Francisco*.

La sentencia `FORMAT` le asigna a la variable **SALARY** el formato `DOLLAR12.`.

`LABEL` especifica las etiquetas de las variables en el reporte. En caso de que las variables del dataset ya tengan etiquetas, estas etiquetas definidas prevalecen en el reporte.

La sentencia `SUM` es la que especifica las variables que mostrarán el gran total. Finalmente se agrega la opción `TITLE` para que se le ponga un título al reporte y se vuelve a llamar al final para que vuelva a su valor inicial.

![Reporte gran total](img/print2.png)

### Reporte con subtotales

Es posible mostrar los reportes con subtotales por grupos de variables.

!!! warning "Datos agrupados"
    Los datos se deberían ordenar por la variables que se desee hacer el agrupamiento para evitar posibles errores en los cálculos. SAS considera valores iguales de la variable de agrupamiento como un bloque. Si SAS encontrara una observación con un valor que ya procesó, se generará un error.

Se puede usar el procedimiento SORT para ordenar una dataset por las variables que se deseen y posteriormente realizar el reporte.

````sas
PROC SORT DATA = SASHELP.BASEBALL OUT = BASEBALL;
    BY DIVISION TEAM;
RUN;

PROC PRINT DATA = BASEBALL NOOBS LABEL;
    VAR NAME POSITION NHOME SALARY;
    FORMAT SALARY DOLLAR12.;
    LABEL DIVISION = "División"
    NAME = "Nombre del jugador"
    TEAM = "Equipo"
    POSITION = "Posición"
    NHOME = "Número de Home Runs en 1986"
    SALARY = "Salario en 1987 (Miles de dólares)"
    ;
    SUM NHOME SALARY;
    BY DIVISION TEAM;
RUN;
````

El procedimiento SORT especifica que se ordene por las variables *division* y luego por *team* y se pide que se guarde una copia temporal, con el fin de no modificar el dataset original.

En el procedimiento **PRINT** se usa la sentencia `BY` para que crear el reporte por combinaciones de valores de *division* y *team*.

![Reporte gran total](img/print3.png)

La imagen anterior muestra el ultimo grupo de variables (División = West y Equipo = Texas). Nótese que este grupo contiene los subtotales tanto de las variables *team* y *division* así como el gran total. Cada grupo contiene como título el valor de las variables *division* y *team*.

!!! tip "Personalizar etiquetas"
    Se pueden agregar en la sentencia `PROC PRINT` las opciones `SUMLABEL =` y `GRANDTOTAL_LABEL =` para personalizar las etiquetas de subtotales y el gran total.

Si se desea mostrar un reporte con otro estilo resaltando las variables de agrupamiento, se puede agregar la sentencia.

`ID DIVISION TEAM;`

El resultado es el siguente.

![Reporte gran total](img/print4.png)
