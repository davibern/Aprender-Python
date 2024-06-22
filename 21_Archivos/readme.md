# Archivos (ficheros)

Lo siguiente en programación una vez que sabemos de tipos, condiciones, estructuras de control, bucles, listas, diccionarios, tuplas, conjuntos, módulos, paquetes, clases, funciones, etc., es poder almacenar nuestros datos en archivos. Trabajar con una fuente de datos y que nuestro programa pueda abrir, leer, escribir y cerrar un fichero.

Poder tratar con ficheros es una parte fundamental de la programación y veremos en Python lo fácil e intuitivo que es.

## Función open()

En Python para poder tratar con un fichero, lo primero es saber qué función tenemos para poder hacerlo, y luego qué opciones tiene.

```Python
# Síntasis
open('fichero', modo)
```

Bien, como vemos, es simple, hay que usar ```open()```, pero este toma dos argumentos:

* El fichero que hay que abrir.
* El modo en el que lo hacemos.

Esta última parte es la que le indicará al sistema cómo vamos a operar, algo indispensable para no crear problemas:

* **r** -> Modo lectura (read). Abre el fichero para su lectura. Devuelve un error si el fichero no existe.
* **a** -> Modo añadir (append). Abre un fichero para agregar datos o crearlo si éste no existe.
* **w** -> Modo escritura (write). Abre un fichero para escritura o crearlo si éste no existe.
* **x** -> Modo creación (create). Crea el fichero especificado, devuelve un error si el fichero ya existiera.
* **t** -> Modo texto (text). Es el valor por defecto si no se especifica ninguno.
* **b** -> Modo binario (binary). Fichero para imágenes, por ejemplo.

Por último, cuando terminamos de trabajar con un fichero hay que cerrarlo con el método ```close()```.

## Abrir fichero de lectura

Si no se especifica nada, el fichero se abrirá siempre en modo lectura, es decir, podemos usar ```open(filename)``` y no es necesario que indimos ni "r" ni "rt".

```open()``` tiene varios métodos interesantes, pero si sólo abrimos el fichero y lo mostramos por pantalla, obtendremos información básica. Y con el método __close__  lo cerramos. Podemos comprobar si un fichero está cerrado además con el método __closed__, que devolverá verdadero o faslo según el caso.

```Python
file = open('data.txt')
print(file)
file.close()
# <_io.TextIOWrapper name='data.txt' mode='r' encoding='cp1252'>
```

Tenemos también la opción de __abrir__ y __cerrar__ el fichero de forma asegurada con el bloque __with__, que nos asegura que el fichero se cerrará al terminar el bloque, incluso si se produce un error. Esto es muy útil para evitar errores de memoria y para asegurarnos de que el fichero se cerrará correctamente.

```Python
with open('data.txt') as file:
    content = file.read()
    print(content)
# Mostrará el contenido del archivo
```

He creado el fichero [data.txt](/21_Archivos/data.txt) por si quieres ir paso a paso conmigo.

Ahora vamos a leer el contenido del fichero, para eso vamos a usar el método ```read()```. Aunque antes, si te fichas en mi ejemplo, he abierto un fichero y su contenido lo he guardado en una variable llamada ```file```. Tiene sentido, porque si no lo guardamos en memoria, no podremos trabajar luego con el 🤯.

Vamos a leerlo.

```Python
file = open('data.txt')
content = file.read()
print(content)
file.close()
# Mostrará el contenido del archivo
```

En este ejemplo puedes ver que he creado un objeto en memoria para poder leer el fichero, otro objeto para poder leer su contenido, y por último lo muestro por pantalla.

Nuestro fichero de ejemplo tiene muy poquitas filas, pero imagina que tienes un csv de miles de registros, ¿podemos ver sólo una parte? Sí, en el método ```read()``` indicamos cuántos caracteres leemos (esto incluye espacios y saltos de línea).

```Python
file = open('data.txt')
content = file.read(5)
print(content)
file.close()
# Mostrará el contenido del archivo pero limitando el número de caracteres
```

Pero podemos leer sólo la primera línea con ```readline()```.

```Python
file = open('data.txt')
content = file.readline()
print(content)
file.close()
# ['0\n', '1\n', '2\n', '3\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9'] 
```

O todas las líneas con ```readlines()```. Esto nos devolverá una lista con el contenido de todo el fichero.

```Python
file = open('data.txt')
content = file.readlines()
print(content)
file.close()
```

Pero este sistema, cuando lo veas, devolverá una lista, como decía antes, pero con ```\n``` al final porque está leyendo varias líneas, ¿cómo podemos limpiar nuestra lista? con ```splitlines()```.

```Python
file = open('data.txt')
content = file.read().splitlines()
print(content)
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```

Como eres observador, te habrás dado cuenta que el fichero de nuestro ejemplo tienen los números del 0 al 9, cuando lo leyemos y obtenemos el resultado en una lista, su contenido es de tipo string.

Cuando vayas trabajando con datos, es importante ir comprobando si lo que estamos importando está en el tipo correcto según nuestros intereses.

Si quisieras cambiar el tipo de ```str``` a ```int``` de tu lista tendrías luego que convertirlo, como en el siguiente ejemplo.

```Python
file = open('data.txt')
content = file.read().splitlines()
print(content)

for i in range(0, len(content)):
    content[i] = int(content[i])

print(content)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Modificar o crear un fichero

Si en vez de leer el fichero lo que queremos es crearlo o actualizarlo, recuerda que tenemos las opciones "a" o "w", que sería "append" o "write".

Vamos a añadir el valor 10 al final del fichero data.txt de nuestro ejemplo.

```Python
file = open('data.txt', 'a')
file.write('\n10')
file.close()
```

Usamos la opción "a", para añadir al final del fichero el valor 10, pero le he indicado que antes incluya un salto de línea.

Para crear un fichero usamos "w", ¡vamos a ello!

```Python
file = open('data_temp.txt', 'w')
file.write('Soy un fichero nuevo')
file.close()
```

## Eliminar un fichero

Para eliminar un fichero en Python no tenemos un ```file.delete()```, sino que tendremos que recurrir a la biblioteca ```os``` y usar el método ```remove()```.

```Python
import os
os.remove('data_temp.txt')
```

Aunque si intentamos borrar un fichero que no existe, nos dará un error de tipo ```FileNotFoundError```. Por lo que es muy muy importante controlar los errores cuando trabajamos con fichero, y para eso tenemos las [excepciones](/19_Excepciones/readme.md).

## Control de errores

En el ejemplo anterior hemos eliminado un fichero, pero no hemos comprobado que existe o no hemos incluido ningún control de errores.

Veamos primero si podemos comprobar que antes exista.

```Python
import os
if os.path.exists('data_temp.txt'):
    os.remove('data_temp.txt')
    print('Fichero eliminado correctamente.')
else:
    print('Error: el fichero no existe.')
# Error: el fichero no existe
```

Y ahora vamos a hacer lo mismo con el ```try-except```.

```Python
import os

try:
    os.remove('data_temp.txt')
    print('Archivo eliminado correctamente.')
except FileNotFoundError:
    print('Error: el archivo no existe.')
# Error: el fichero no existe
```

¿Cuál os gusta más? Particularmente con el control de excepciones puedes comprobar por ejemplo, que el fichero que quieres leer existe. Es mucho más cómodo y verstátil.

```Python
try:
    file = open('data_temp.txt')
    content = file.read().splitlines()
    print(content)
except FileNotFoundError:
    print('Error: el fichero no existe')
# Error: el fichero no existe
```

Como digo, siempre es mejor usar el ```try-except``` para comprobar errores, por ejemplo, que el fichero exista, se pueda modificar, tengamos permisos, etc.