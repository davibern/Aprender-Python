# Módulos

Un ```módulo``` es un conjunto de archivos (uno o varios) o bien un conjunto de funciones que pueden incluirse en una aplicación.

Es decir, un módulo podría ser un archivo, varios archivos, una función o varias funciones, que te servirán para poder incluir su código en otra aplicación.

La idea es tener un programa para incluirlo en otro programa, y que ésto pueda ahorrar trabajo en un futuro, o tener el código bien estructurado.

## Crear un módulo e importarlo

Para crear un módulo sólo es necesario un fichero que acabe en .py, y ponerle un nombre. Luego creamos otro fichero en nuestro proyecto y lo importamos con la palabra reservada ```import```.

Creamos un fichero que será importado en otro fichero.

```Python
# modulo_suma.py
def suma(a, b):
    return a + b
```

En otro fichero importamos ```modulo_suma.py```.

```Python
# main.py
import modulo_suma.py

resultado = modulo_suma.suma(2, 2)
print(resultado)
```

## Importar un fichero y varias funciones

Podemos tener un fichero de operaciones, e importar sólo los que nos hagan falta. Para ello hay que usar las palabras reservadas ```from``` e ```import```.

```Python
# operaciones.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b
```

Pero sólo necesitamos las funciones ```sumar``` y ```restar```.

```Python
# main.ph
form operaciones import sumar, restar
sumar(2, 2)
restar(2, 2)
```

## Cambiar el nombre de las funciones importadas

A parte de poder importas las funciones que más nos interesen, también podemos renombrarlas. Volvemos al ejemplo del código de ```operaciones.py```, pero esta vez en su importación, le vamos a cambiar el nombre.

```Python
# main.ph
form operaciones import sumar as s, restar as r
s(2, 2)
r(2, 2)
```

Como le hemos cambiado el nombre, también hay que hacerlo a la función.

## Existen multitud de módulos

Python contiene una cantidad inmensa de módulos a importar, desde controladores de comandos del sistema, a estadísticas, gráficos 2D, matemáticos, etc.

Puedes encontrar éstos módulos en la siguiente web: [https://pypi.org/](https://pypi.org/).

Para esta unidad lo mejor es que practiques importando tus propios paquetes, u otros básicos como os, pandas, etc.

***

⬅️ [Clase anterior](/15_Funciones/readme.md) | [Clase siguiente](/17_Clases/readme.md) ➡️