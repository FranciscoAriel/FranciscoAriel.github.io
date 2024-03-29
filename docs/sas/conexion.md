---
title: Conectando SAS con otros softwares
summary: Cómo conectar SAS con otros lenguajes de programación.
authors: Francisco Vázquez
date: 2020-11-02
---

# Conexión con SAS

Existen muchas formas de conectar SAS con otros lenguajes de programación.

En esta sección se mostrarán algunas maneras de conectarse a con otros programas, ya sea de manera local o remota.

## Conexión con Python y Jupyter Notebooks

Es posible usar [SAS &reg; OnDemand for Academics](https://www.sas.com/en_us/software/on-demand-for-academics.html) y conectarlo con los cuadernos de Jupyter. Para ello se requiere lo siguiente:

1. Crear una cuenta en [SAS &reg; OnDemand for Academics](https://www.sas.com/en_us/software/on-demand-for-academics.html) para obtener un nombre de usuario y establecer una contraseña.
2. Tener instalada la versión más reciente de [Anaconda](https://www.anaconda.com). También se requiere tener instalado [Java](https://www.java.com/es/download/) versión **1.8.0_162** o mayor.
3. Instalar el paquete [saspy](https://sassoftware.github.io/saspy/index.html). También se recomienda instalar el [sas kernel](https://sassoftware.github.io/sas_kernel/overview.html) para los cuadernos de python.
4. Realizar las [configuraciones necesarias](https://support.sas.com/ondemand/saspy.html#one).

Consulte la [ayuda de SAS OnDemand](https://support.sas.com/ondemand/saspy.html) para una referencia completa y detallada.

!!! note "Actualización de Java"
    Debido a actualizaciones recientes, es posible que existan problemas con Java y no permitan conectarse correctamente. Se recomeida leer este [post](https://github.com/sassoftware/saspy/issues/470#issuecomment-1178996639) con el fin de actualizar algunos archivos de java.

### Configuración de saspy

Se puede instalar el paquete `saspy` desde la consola (cmd o powershell) escribiendo el siguiente comando:

````cmd
pip install saspy
````

!!! tip "Incluye pip"
    La distribución de Anaconda ya incluye pip, por lo que solo basta escribir el nombre del paquete en la consola.

Para comprobar que se ha instalado correctamente, se debe escribir en la consola

````cmd
python
````

Debe de aparecer algo similar a esto:

````cmd
Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32

Warning:
This Python interpreter is in a conda environment, but the environment has
not been activated.  Libraries may fail to load.  To activate this environment
please see https://conda.io/activation

Type "help", "copyright", "credits" or "license" for more information.
>>>
````

Para comprobar la correcta instalación de la librería, se puede escribir en la consola el siguiente comando:

````python
import saspy
saspy
````

El resultado nos arrojaría el directorio donde está el archivo de configuración `sascfg.py`, por ejemplo:

````python
<module 'saspy' from 'C:\\Users\\Usuario\\anaconda3\\lib\\site-packages\\saspy\\__init__.py'>
````

En dicho directorio se debe crear una copia del archivo `sascfg.py` nombrándolo **sascfg_personal.py**. A continuación se debe borrar el contenido y pegar esto en **sascfg_personal.py**:

````python
SAS_config_names=['oda']
oda = {'java' : 'C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath\\java.exe',
#US Home Region
'iomhost' : ['odaws01-usw2.oda.sas.com','odaws02-usw2.oda.sas.com','odaws03-usw2.oda.sas.com','odaws04-usw2.oda.sas.com'],
#European Home Region
#'iomhost' : ['odaws01-euw1.oda.sas.com','odaws02-euw1.oda.sas.com'],
#Asia Pacific Home Region
#'iomhost' : ['odaws01-apse1.oda.sas.com','odaws02-apse1.oda.sas.com'],
'iomport' : 8591,
'authkey' : 'oda',
'encoding' : 'utf-8'
}
````

!!! tip "Java"
    Verifique que el directorio de Java realmente existe, de otra forma no funcionará correctamente.

Posteriormente se debe crear en la carpeta personal (usualmente `C:\Users\Usuario`) el archivo `_authinfo` que contenga la información de las credenciales de SAS &reg; OnDemand de la siguiente forma, sustituyendo por los valores que correspondan:

````txt
oda user usuario password contraseña
````

!!! caution "Archivo sin extensión"
    El archivo `_authinfo` no tiene extensión y debe ser guardado en formato `UTF-8`. Si la contraseña contiene espacios, se debe poner entre comillas.

Una vez realizados estos pasos, puede escribir nuevamente en la consola esta instrucción para comprobar que se puede acceder a SAS OnDemand:

````python
sas = saspy.SASsession()
sas
````

El resultado que se mostraría en la pantalla es el siguiente:

````python
Using SAS Config named: oda
SAS Connection established. Subprocess id is 3500
````

Adicionalmente se puede instalar el  [sas kernel](https://sassoftware.github.io/sas_kernel/index.html) para los cuadernos de python usando la consola CMD o Powershell.

````cmd
pip install sas_kernel
````

Para comprobar que se ha instalado exitosamente, se puede ejecutar el siguiente comando:

````cmd
jupyter kernelspec list
````

### Usando SAS en un cuaderno Jupyter

En esta sección se muestra cómo usar un cuaderno de Jupyter y conectarlo con SAS. Se usará [Visual Studio Code](https://code.visualstudio.com) versión 1.62 usando la [extensión Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) para la generación del archivo _ipynb_.

Para hacer uso de esta funcionalidad, se debe crear un cuaderno de jupyter con un kernel de SAS. Revise la [configuración de saspy](conexion.md#configuracion-de-saspy) para tener lsito tanto el kernel como el paquete saspy.

!!! tip "Nuevo archivo"
    Puede crearse un nuevo cuaderno de jupyter desde el menu *Archivo*, Seleccionar la opción *Nuevo Archivo ...*, aparecerá la opción de crear opción de crear un nuevo archivo de jupyter.

Para pode usarlo, se debe elegir el kernel de SAS y se puede escribir tanto código de SAS como Markdown el el cuaderno. Los resultados estarán dentro del cuaderno de Jupyter y dependiendo de los procedimientos, los resultados serán mostrados en formato HTML.

La siguiente imagen muestra el funcionamiento de SAS en un cuaderno de Jupyter.

![SAS notebook](img/sas_nb.png)

Consulte la [documentación de sas kernel](https://sassoftware.github.io/sas_kernel/overview.html) para más información.

### Usando el paquete saspy en un cuaderno Jupyter

Las librería y datasets de SAS pueden usarse dentro de Python a través del paquete saspy.

Para hacer uso de la librería, se debe crear un cuaderno de jupyter con un kernel de python. Revise la [configuración de saspy](conexion.md#configuracion-de-saspy) para tener todo listo y evitar algún error.

El primer paso es cargar el paquete saspy escribiendo el siguiente código en una celda de código python:

````python
import saspy
sas = saspy.SASsession()
sas
````

Se desplegará información acerca de la conexión a SAS &reg; OnDemand y sus configuraciones.

````python
Using SAS Config named: oda
SAS Connection established. Subprocess id is 2816

Access Method         = IOM
SAS Config name       = oda
SAS Config file       = C:\Users\Usuario\anaconda3\lib\site-packages\saspy\sascfg_personal.py
WORK Path             = /saswork/SAS_work32430000E59D_odaws01-usw2.oda.sas.com/SAS_work6D2A0000E59D_odaws01-usw2.oda.sas.com/
SAS Version           = 9.04.01M6P11072018
SASPy Version         = 3.7.5
Teach me SAS          = False
Batch                 = False
Results               = Pandas
SAS Session Encoding  = utf-8
Python Encoding value = utf-8
SAS process Pid value = 58781
````

La siguiente imagen muestra algunas funcionalidades del paquete saspy. Consulte la [documentación de saspy](https://sassoftware.github.io/saspy/api.html) para una referencia completa de los métodos del paquete.

![Usando saspy](img/sas_nb2.png)            

### Usando código SAS usando cualquier kernel de Jupyter

Es posible usar código SAS en un cuaderno de Jupyter directamente, aunque el kernel no sea de SAS.

Para hacer esto, se hace uso de los _SAS MAGICS_, que son trozos de código de otro lenguaje que se ejecutan. Simplemente en una celda nueva se debe colocar al inicio `%%SAS` y debajo el código SAS que se desea realizar.

La siguiente muestra su uso.

![SAS magic](img/sas_magic.png)

Nótese que a pesar de estar en un cuaderno con kernel python, se ha realizado una conexión con SAS y se ha ejecutado el código de la celda.

!!! caution "Activar el paquete"
    No olvide activar el paquete saspy antes de usar el _sas magic_ para evitar errores.
