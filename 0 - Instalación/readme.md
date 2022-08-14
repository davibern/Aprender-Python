# Instalación de Python

La versión que recomiendan instalar desde la fuente oficial es la **3.10.x**. A continuación indico cómo hacerlo de forma genérica para:

* Windows 10/11
* Linux
* Mac

## Python en Windows 11/10

De base Python no se encuentra instalado en Windows, por lo que tenemos varias formas, desde la web o usando winget.

### Descargar los binarios desde la web

Accede a [Descargar Python] y pulsa en "Download Python 3.10.x", esto desde Windows descargará los binarios que mejor le vengan a tu sistema operativo según arquitectura y versión.

[Descargar Python]: https://www.python.org/downloads/

Pero si estás interesado en descargar otras versiones tienes disponible este otro enlace: [Descargar Python Windows].

[Descargar Python Windows]: https://www.python.org/downloads/windows/

### Instalar binarios

Una vez decidida la versión y descargada, en Windows no hay misterio alguno, doble clic, y siguiente hasta terminar la instalación.

Por defecto la instalación añadirá al PATH de tu sistema la dirección del ejecutable, para comprobar que tenemos instalado Python abrimos la terminal de windows y escribimos:

```python --version```
> Python 3.10.5

Si saliera algún error es que o bien no se ha instalado el PATH o bien es necesario reiniciar.

### Instalar Python usando WinGet

Si te atreves puedes instalar Python usando el paquete de descargas de Windows 10/11 llamado [WinGet].

Este sistema emula el distribuidor de paquetes de Unix, tales como Linux o Mac, y desde la línea de comandos de PowerShell puedes instalar infinidad de programas.

Primero, consultamos los paquetes que tengamos disponibles de Python:

```winget list --name Python```

Esto nos devolverá esta posible lista:

* Python Launcher
* Python 3

Más o menos os debería de salir esta lista genérica, lo siguiente es actualizar la lista de winget:

1. ```winget upgrade --all```
2. ```winget install Python```

Se iniciará la instalación desde la terminal y veremos aparecer las ventanas de configuración de la instalación, siguiente, siguiente, y listo.

[WinGet]: https://docs.microsoft.com/es-es/windows/package-manager/winget/

## Python en Linux

Por defecto Linux tendrá instalado, en cualquier versión, Python. Y lo normal es que tenga instalada la versión **2.9.x.**

Tienes dos opciones, trabajar con la que viene por defecto o instalar la versión 3.

Si decides instalar la versión 3, haz lo siguiente, para sistemas Debian (Ubuntu, etc.)

```sudo apt-get install python3.10```

Una vez instalado tendrás dos versiones, la 2.9 y la 3.10, podrás comprobar su instalación en la terminal escribiendo:

```python --version```
> Python 2.9

```python 3.10 --version```
> Python 3.10

## Python en Mac

Para Mac la instalación es similar que en Windows, puedes descargarte los binarios desde la web y elegir versión o usar homebrew.

# Shell de Python

Una vez instalado ya podríamos trabajar directamente con Python usando nuestro Terminal, con sólo ejecutar ```python```.

![Shell de Python](/99%20-%20Imagenes/shell_python_1.png)

Recuerda que desde el terminal sólo tienes que ejecutar **python** y automáticamente se mostrará la Shell de Python.

Una vez dentro ya puedes realizar operaciones, como por ejemplo una suma.

> 255 + 300

![Sumar en la shell de python](/99%20-%20Imagenes/shell_python_2.png)

También podemos mostrar texto.

> "hola python"

![Mostrar texto en la shell de python](/99%20-%20Imagenes/shell_python_3.png)

También podemos mostrar una comparativa y su salida, por ejemplo:

> 2 > 1

![Mostrar compartiva de operadores en la shell de python](/99%20-%20Imagenes/shell_python_4.png)

Para salir de la shell de Pyton basta con escribir ```quit()```.

![Salir de la shell de python](/99%20-%20Imagenes/shell_python_5.png)