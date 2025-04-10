# Listas (Lists)

Como ya habrás visto en la [clase de tipos de datos](/04_Tipos_de_datos/readme.md), existen varios tipos de colecciones, este recordatorio lo voy a incluir en cada una de ellas, porque machacar información es también la mejor manera de que entre en la cabezita 🤯

Pero primero, ¿qué es una Lista?

> Es una colección de datos ordenada, modificable y que permite duplicados.

Y ahora el resto:

* **Tupla**: es una colección de datos ordenada, pero que no permite modificar los datos. Y permite duplicados.
* **Set**: es una colección de datos desordenada, pero indexada, que no permite modificaciones y tampoco duplicados.
* **Diccionario**: es una colección de datos desordenada, modificable e idenxada, que funciona por par clave-valor, y que no permite duplicados.

## Crear una Lista

Para crear una lista tenemos que crear un objeto tipo ```List()```.

```Python
lista = list() # Creamos un objeto vacío de tipo List en la variable lista
```

O bien podemos usar directamente los corchetes ```[]```

```Python
lista = []
```

Una lista, cuando se crea y está vacía, tendrá cero elementos dentro, sé que es una perogruyada, pero es bueno recordarlo.

```Python
lista = list()
print(len(lista))
# Devuelve 0
```

Pero, ¿y si quiero crear una lista con datos? Pues es exactamente igual, pero añadiendo datos dentro de los corchetes.

A esto se le llama inicializar un objeto, y por consiguiente la variable.

```Python
letras = ['A', 'B', 'C', 'D', 'E', 'F']
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]
lenguajes = ['Python', 'Java', 'R', 'C#', 'Visual Basic', 'JavaScript']
```

Y para imprimir el contenido, todo el contenido, basta con invocarlo.

```Python
print(letras)
print(numeros)
print(lenguajes)
```

¿Y si comprueba los elementos? ¿Habrán cambiado? Efectivamente...

```Python
print(len(letras))
# Indicará 5
```

Puedes probar en tu script lo siguiente:

```Python
lista = ['Sun', 'Venus', 'Mercurio', 'Marte', 'Tierra']
print(f'Planetas en la lista {len(lista)}')
print(f'Planetas: {lista}')
```

## Datos de una Lista

Los datos que se pueden guardar en una lista no tienen porqué ser los mismos. A diferencia de otros lenguajes, cuando se crea un array, éste debe contener siempre el mismo tipo de dato, como en Java.

Pero en Python, las listas permiten que los datos puedan ser diferentes, incluso que contengan otra matriz de datos.

```Python
lista_rara = [1, 2, 'Tres', 'Cuatro', [1, 3, 4]]
```

## Accediendo a las posiciones de una Lista

Podemos acceder a la lista, para entendernos, desde la izquierda (posición 0) o desde la derecha (última posición), pero para acceder a su última posición se usan los negativos.

Vamos a verlo mejor con un ejemplo.

```Python
mi_lista = ['Red', 'Orange', 'Blue', 'Black']
#           0       1        2       3
```

En este fragmento de código vemos que la lista empieza en 0 y acaba en 3, siendo 0 'Red' y 3 'Black'. Por lo que sabemos siempre que la primera posición será cero, 3 la última.

Si escribimos ```mi_lista[1]``` sabemos que accederemos al valor 'Orange'.

Y ahora veremos el índice contrario.

```Python
mi_lista = ['Red', 'Orange', 'Blue', 'Black']
#           -4      -3       -2       -1
```

Ahora, si queremos acceder al último valor, pero no sabemos cuántos elementos tiene la lista (aunque se puede calcular), bastaría con acceder a la posición -1.

Te puedes estar preguntando si por la izquierda se usa el 0, porque en la derecha no. La respuesta es que hay que diferenciarlo de algún modo, podría haberse usado el -0, pero como 0 es un número que no tiene signo negativo ni positivo, porque es neutro, se decidió el -1.

Y tiene sentido.

Ahora, si accedemos a ```mi_lista[-3]``` estaremos accediendo a 'Orange'.

## Desempaquetando todos los items

Al igual que con los Strings, podemos desempaquetar una lista en sus respectivas variables.

```Python
mi_lista = ['A', 'B', 'C', 'D', 'E', 'F']
a, b, c, d, e, f  = mi_lista
print(a) # Imprime 'A'
print(b) # Imprime 'B'
print(c) # Imprime 'C'
print(e) # Imprime 'E'
print(f) # Imprime 'F'
```

También podemos desempaquetar parcialmente una lista usando ```*``` seguido del nombre de la variable.

```Python
mi_lista = ['A', 'B', 'C', 'D', 'E', 'F']
a, b, c, *resto  = mi_lista
print(a) # Imprime 'A'
print(b) # Imprime 'B'
print(c) # Imprime 'C'
print(resto) # Imprime ['D', 'E', 'F']
```

También podemos desempaquetar parcialmente una lista especificando un intervalo de posición.

```Python
mi_lista = ['A', 'B', 'C', 'D', 'E', 'F']
lista_troceada = mi_lista[0:3] # Guarda sólo de la posición 0 a la 3
lista_completa = mi_lista[0:] # Guarda todos los elementos de la lista, empezando por el 0.
lista_pares = mi_lista[::2] # Guardará los elementos pares: 'B', 'D', 'F'.
```

Esto es aplicable también usando el índice negativo que hemos visto anteriormente.

## Modificar una lista

Como hemos dicho al principio, las lista son modificables, o mutables. Eso quiere decir, que una vez que las creamos, podemos editarlas, añadiendo o eliminando valores, o sustituyendo.

Vamos a ver a continuación las opciones que tenemos.

### Sustituir un valor

Se sustituye un valor accediendo a su posición y almacenando el nuevo valor.

```Python
mi_lista = ['A', 'B', 'C', 'D', 'E', 'F']
mi_lista[0] = 'Z'
print(mi_lista) # 'Z', 'B', 'C', 'D', 'E', 'F'
```

### Añadiendo un valor

Se añade un nuevo elemento en la última posición usando ```append()```.

```Python
mi_lista = ['A', 'B', 'C', 'D', 'E', 'F']
mi_lista.append('Z')
print(mi_lista) # 'A', 'B', 'C', 'D', 'E', 'F', 'Z'
```

### Insertar un elemento

Se inserta un elemento en un lugar específico de la lista. Es necesario añadir la posición de entrada y el valor.

```Python
mi_lista = ['A', 'B', 'C', 'D', 'E', 'F']
mi_lista.insert(2, 'Z')
print(mi_lista) # 'A', 'B', 'Z', 'C', 'D', 'E', 'F'
```

### Eliminando valores usando remove()

Se puede eliminar un item indicando su valor como atributo del método ```remove()```.

```Python
mi_lista = ['A', 'B', 'C', 'D', 'E', 'F']
mi_lista.remove('F')
print(mi_lista) # 'A', 'B', 'C', 'D', 'E',
```

### Eliminando valores usando pop()

Como el anterior, pero en este caso se usa una posición, no el valor. Si no se especifica el valor, se elimina la última posición.

```Python
mi_lista = ['A', 'B', 'C', 'D', 'E', 'F']
mi_lista.pop()
print(mi_lista) # 'A', 'B', 'C', 'D', 'E',
```

```Python
mi_lista = ['A', 'B', 'C', 'D', 'E', 'F']
mi_lista.pop(1)
print(mi_lista) # 'A', 'C', 'D', 'E', 'F'
```

### Eliminando usando del()

Como el anterior, pero en este caso ```del()``` también nos puede valer para eliminar todos los valores.

```Python
mi_lista = ['A', 'B', 'C', 'D', 'E', 'F']
del mi_lista
print(mi_lista) # []
```

```Python
mi_lista = ['A', 'B', 'C', 'D', 'E', 'F']
del mi_lista[0]
print(mi_lista)  # 'B', 'C', 'D', 'E', 'F'
```

### Limpiando la lista con clear()

El método ```clear()``` lo que hace es eliminar todos los valores, pero no la lista en sí.

```Python
mi_lista = ['A', 'B', 'C', 'D', 'E', 'F']
mi_lista.clear()
print(mi_lista) # []
```

## Comprobar si un elemento se encuentra en una lista

Podemos comprobar si un elemento existe en una lista usando la palabra reservada ```in```.

```Python
mi_lista = ['A', 'B', 'C', 'D', 'E', 'F']
a_exist = 'A' in mi_lista
print(a_exist) # True
```

Si no estuviera, devolvería *False*.

## Accediendo a elementos de una lista

### Elementos fijos de una lista

Podemos obtener una serie de elementos de una lista usando el _slice_, tal y como veremos a continuación. Este acceso se hace con ```:```.

```Python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista[1, 5] # Devolverá desde el 2 al 4
```

### Todos los elementos

Con __::__  podemos obtener todos los elementos de una lista. También podemos usarlo para obtener los elementos de una lista de dos en dos, o de tres en tres, etc. Para ello, usaremos __::2__, __::3__, etc.

```Python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista[::] # Devolverá todos los elementos
lista[::2] # Devolverá los elementos de dos en dos
lista[::3] # Devolverá los elementos de tres en tres
```

### Última posición de una lista

Podemos acceder a la última posición con el signo negativo (-).

```Python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista[-1] # Devolverá el 10
```

```Python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista[-2] # Devolverá desde el 9
```

## Copiar una lista

Podemos copiar una lista simplemente reasigándola a una nueva variable.

```Python
mi_lista = ['A', 'B', 'C', 'D', 'E', 'F']
mi_lista_2 = mi_lista
```

Esto conlleva que cualquier cambio que hagamos en ```mi_lista_2``` también afectarán a la original.

¿Y si simplemente quiero hacer una copia sin que afecte los cambios? Para eso usamos ```copy()```.

```Python
mi_lista = ['A', 'B', 'C', 'D', 'E', 'F']
mi_lista_2 = mi_lista.copy()
```

## Unir listas

Existen varias formas de unir dos listas diferentes.

### Unir usando el operador +

```Python
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8, 9 10]
lista_completa = lista_1 + lista_2
print(lista_completa) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Pero este método no se recomienda porque es más lento al tener que copiar primero la lista para manipularla después.

Lo mejor en este caso sería de la siguiente forma:

```Python
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8, 9 10]
lista_1 += lista_2
print(lista_completa) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Esto es más eficiente que el primer método.

### Unir usando el método extend()

Es igual que el anterior, pero usando el método ```extend()``` e incluyendo como argumento la lista a unificar.

```Python
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8, 9 10]
lista_1.extend(lista_2)
print(lista_1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## Contar elementos repetidos usando count()

Con el método ```count()``` podemos saber el número de elementos iguales que tiene la lista

```Python
lista_1 = [1, 2, 3, 4, 5, 5]
print(lista_1.count(5)) # 2
```

## Encontrar un elemento indexado de una lista con index()

```index()``` devuelve el índice de un elemento de la lista. No devuelve el valor, sino su posición.

```Python
lista_1 = [1, 2, 3, 4, 5]
print(lista_1.index(2)) # 1
```

## Revertir el orden con reverse()

Podemos revertir el orden de una lista usando ```reverse()```.

```Python
lista_1 = [1, 2, 3, 4, 5]
lista_1.reverse()
print(lista_1) # [5, 4, 3, 2, 1]
```

## Ordenar una lista con sort()

Al contrario que el anterior, con ```sort()``` podemos ordenar una lista. Podemos indicar si queremos ordenarlo ascendentemente o descendentemente.

```Python
lista_1 = [5, 4, 3, 2, 1]
lista_1.sort() # Ascendentemente.
print(lista_1) # [1, 2, 3, 4, 5]
```

```Python
lista_1 = [1, 2, 3, 4, 5]
lista_1.sort(reverse = True) # Descendentemente.
print(lista_1) # [5, 4, 3, 2, 1]
```

## Enumerar la lista con enumerate

Los elementos de una lista podemos enumerarla creándole un índice. Para ello usamos el método _enumerate()_. Este método devuelve un objeto enumerado. Podemos transformarlo a una lista o a un diccionario si lo deseamos. En este caso lo transformaremos a una lista usando el método _list()_.

```Python
estaciones = ["Primavera", "Verano", "Otoño", "Invierno"]
print(list(enumerate(estaciones))) # [(0, 'Primavera'), (1, 'Verano'), (2, 'Otoño'), (3, 'Invierno')]
```

Pues ya hemos terminado esta clase, tengo que darte otra vez mi enhorabuena, porque si has llegado hasta el final, una de dos, o te gusta mucho Python como para dejarlo, o tan mal no lo hago 😜

Vamos a los [ejercicios](/09_Listas/ejercicios_lista.md).

De forma avanzada, puedes echarle un vistazo a las [listas compactas](/18_Lista_Compacta/readme.md), que es un forma más eficaz y rápida de crear y operar con listas.

***

⬅️ [Clase anterior](/08_Strings/) | [Clase siguiente](/10_Tuplas/readme.md) ➡️