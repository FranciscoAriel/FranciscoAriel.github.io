---
title: Conectando SAS con otros softwares
summary: Cómo conectar SAS con otros lenguajes de programación.
authors: Francisco Vázquez
date: 2020-11-02
---

# Conexión con SAS

Existen muchas formas de conectar SAS con otros lenguajes de programación.

En esta sección se mostrarán algunas maneras de conectarse a con otros programas, ya sea de manera local o remota.

## Conexión con Jupyter Notebooks

Es posible usar [SAS &reg; OnDemand for Academics](https://www.sas.com/en_us/software/on-demand-for-academics.html) y conectarlo con los cuadernos de Jupyter. Para ello se requiere lo siguiente:

1. Crear una cuenta en [SAS &reg; OnDemand for Academics](https://www.sas.com/en_us/software/on-demand-for-academics.html) para obtener un nombre de usuario y establecer una contraseña.
2. Tener instalada la versión más reciente de [Anaconda](https://www.anaconda.com). También se requiere tener instalado [Java](https://www.java.com/es/download/) versión **1.8.0_162** o mayor.
3. Instalar el paquete [saspy](https://sassoftware.github.io/saspy/index.html). También se recomienda instalar el [sas kernel](https://sassoftware.github.io/sas_kernel/overview.html) para los cuadernos de python.
4. Realizar las [configuraciones necesarias](https://support.sas.com/ondemand/saspy.html#one).

Consulte la [ayuda de SAS OnDemand](https://support.sas.com/ondemand/saspy.html) para una referencia completa y detallada.

### Configuración

Se puede instalar el paquete `saspy` desde la consola (cmd o powershell) escribiendo el siguiente comando:

````cmd
pip install saspy
````

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
oda user "usuario" password "contraseña"
````

!!! caution "Archivo sin extensión"
    El archivo `_authinfo` no tiene extensión y debe ser guardado en formato `UTF-8`.

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

Para comprobar que se ha instalado exitoamente, se puede ejecutar el siguiente comando:

````cmd
jupyter kernelspec list
````

La siguiente imagen muestra el funcionamiento de SAS en un cuaderno de Jupyter.

