# Github de Francisco

## Visita mi blog

Este repositorio sirve para almacenar el código fuente de mi sitio de cursos básicos.

Si quieres visitar mi blog de conceptos básicos de softwares estadísticos de [click aquí](https://franciscoariel.github.io/site). Este sitio fue escrito in markdown con [mkdocs](https://www.mkdocs.org).

También tengo un curso básico de sql en gitbook. Puedes consultarlo en este [enlace](https://vazquez-chavez-francisco-ariel.gitbook.io/notas/).

## Tú puedes contribuir

¡Todos aprendemos de todos!

Si deseas aportar nuevos conocimientos puedes apoyarnos con sugerencias o comentarios.

También puedes hacer aportaciones a mi código fuente, es muy fácil todo está escrito en formato merkdown.

Puedes clonar este repositorio.

````bash
git clone https://github.com/FranciscoAriel/FranciscoAriel.github.io.git
````

o simplemente descarga el zip en tu computadora.

### Organización del sitio

El archivo *mkdoc.yml* es el archivo principal que contiene la configuración para construir el sitio web con MKDOCS.

Este archivo contiene el menú de navegación para organizar por los distntos lenguajes de programación. Dentro de cada menú se despliegan temas según su nivel de dificultad. Cada tema está ligado a un archivo markdown.

La carpeta **docs** contiene de forma organizada los diversos archivos markdown por lenguaje y una carpeta llamada **src** donde se contienen archivos auxiliares, como ejemplos de códigos, dataset u otros recursos.
Finalmente la carpeta **img** contiene contiene imágenes para ilustrar algunos resultados.

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

## Extras

Para agregar fragmentos de código, consulte la sección [code blocks](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#code-blocks) para conocer sobre como resaltar los códigos o lenguajes soportados.

Se pueden agregar cuadros que resaltan la información consulte [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#admonitions) para una referencia completa.

----

This is a **readme page**.

If you want to visit my blog, [click here](https://franciscoariel.github.io/site).

This site was written in markdown with [mkdocs](https://www.mkdocs.org).
