# Bienvenido a Estadística desde Cero

En este sitio web conocerás conceptos básicos de estadística así como fundamentos de diversos programas de software estadístico con el fin de iniciarse en el mundo de la ciencia de datos.

![Ilustración de una laptop](img/laptop.png)
Imagen de [Sara Torda](https://pixabay.com/es/users/sara_torda-888816/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2298286) en [Pixabay](https://pixabay.com/es/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2298286)

## Conceptos básicos

En esta sección encontrarás una breve introducción a la estadística, abarcando desde los conceptos y definiciones básicos hasta modelos más complejos.

Haz click [aquí](estadistica/inferencia/index.html) para ir al blog de Estadística.

![Interfaz gráfica](img/interface.png)
Imagen de [janjf93](https://pixabay.com/es/users/janjf93-3084263/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3614766) en [Pixabay](https://pixabay.com/es/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3614766)

## Software estadístico

Presentamos una guía básica para aprender los comandos básicos de distintos lenguajes de programación más usados en estadística y ciencias de datos.

![Ilustración de programador](img/programmer.png)
Imagen de [200 Degrees](https://pixabay.com/es/users/200degrees-2051452/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1653351") en [Pixabay](https://pixabay.com/es/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1653351)

### SAS &reg; Software

En este blog conoceras todo lo relacionado a:

* **SAS &reg; software** - Contiene todo lo esencial para leer, manipular datos así como otras funciones básicas de SAS.
* **SAS/STAT &reg; software** - Tiene muchos métodos estadísticos y otros análisis de datos.
* **SAS/IML &reg; software** - Es un lenguaje específico para trabajar con vectores, matrices, funciones matemáticas y estadísticas avanzadas.
* **OTROS** - Conexión de SAS con otros lenguajes de programación y sus configuraciones.

Para ir al blog de SAS haz click [aquí](sas/intro_sas/index.html).

![Mujer joven trabajando](img/young-woman.jpg)

Imagen de [Karolina Grabowska](https://pixabay.com/es/users/kaboompics-1013994/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=791849) en [Pixabay](https://pixabay.com/es/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=791849)

### R

Visita mi [blog sobre R](r/intro_r/index.html).

En este blog encontrarás todo lo relacionada al lenguaje R.

* Variables
* Funciones
* Matrices
* Gráficas
* Data sets

Entre otras cosas más.

![Trabajo en computadora](img/work.jpg)

Imagen de [Free-Photos](https://pixabay.com/photos/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=731198) en [Pixabay](https://pixabay.com/es/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=731198)

### Python

[Click aquí](python/intro_python/index.html) para ir a mi blog de Python.

Aquí encontrarás todo lo relacionado con librerías que se usan en ciencia de datos.

### Julia *¡NUEVO!*

Julia es un nuevo lenguaje de programación enfocado en la velocidad y está optimizado para trabajar con todos los recursos de la computadora.

[Click aquí](julia/intro_julia/index.html) para ir a mi blog de Julia.

### Jupyter Notebooks

PROXIMAMENTE ... :clock1:

## Sobre el sitio

Este sitio es una guía para iniciarse en el mundo de la programación en diversos lengajes estadísticos y bajo ningún motivo el autor es responsable de los daños ocasionados por resultados inesperados.

Los softwares usados son

* SAS
* R
* Python
* Julia

Los programas son mostrados con fines educativos.

Síguenos en nuestras redes sociales

[Github](https://github.com/FranciscoAriel)

[LinkedIn](https://www.linkedin.com/in/fcoavc/)

No te pierdas las últimas noticias en nuestro canal de [Telegram](https://t.me/estad_camp_0)

<div>
<script async src="https://telegram.org/js/telegram-widget.js?15" data-telegram-post="estad_camp_0/9" data-width="100%"></script>
</div>

## Tú puedes contribuir

¡Todos aprendemos de todos!

Si deseas aportar nuevos conocimientos puedes apoyarnos con sugerencias o comentarios.

También puedes hacer aportaciones a mi código fuente, es muy fácil todo está escrito en formato markdown.

Puedes clonar este repositorio.

````bash
git clone https://github.com/FranciscoAriel/FranciscoAriel.github.io.git
````

o simplemente descarga el zip en tu computadora.

### Organización del sitio

El archivo *mkdoc.yml* es el archivo principal que contiene la configuración para construir el sitio web con MKDOCS.

Este archivo contiene el menú de navegación para organizar por los distntos lenguajes de programación. Dentro de cada menú se despliegan temas según su nivel de dificultad. Cada tema está ligado a un archivo markdown.

La carpeta **docs** contiene de forma organizada los diversos archivos markdown por lenguaje y una carpeta llamada **src** donde se contienen archivos auxiliares, como ejemplos de códigos, dataset u otros recursos. Finalmente la carpeta **img** contiene contiene imágenes para ilustrar algunos resultados.

El proyecto está basado en el tema [material](https://squidfunk.github.io/mkdocs-material).

### Archivos markdown

Los archivos markdown están en formato `utf-8`.

Cada archivo inicia con un encabezado en donde se especifica los metadatos.

````yaml
title: Título
summary: Resumen
authors: Nombre del autor
date: yyyy-mm-dd
````

Se pueden usar encabezados de nivel dos para temas principales y de nivel 3 para subtemas

````md
## Tema

Párrafo

### Subtema

Párrafo
````

### Extras

Para agregar fragmentos de código, consulte la sección [code blocks](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#code-blocks) para conocer sobre como resaltar los códigos o lenguajes soportados.

Se pueden agregar cuadros que resaltan la información consulte [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#admonitions) para una referencia completa.

----

> SAS and all other SAS Institute Inc. product or service names are registered trademarks or trademarks of SAS Institute Inc. in the USA and other countries. &reg; indicates USA registration.
