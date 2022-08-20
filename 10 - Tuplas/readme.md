# Tuplas (tuples)

Como ya habrás visto en la [clase de tipos de datos](/4%20-%20Tipos%20de%20datos/readme.md), existen varios tipos de colecciones, este recordatorio lo voy a incluir en cada una de ellas, porque machacar información es también la mejor manera de que entre en la cabezita 🤯

Pero primero, ¿qué es una Tupla?

> Es una colección de datos ordenada, pero que no permite modificar los datos. Y permite duplicados.

Y ahora el resto:

* **Lista**: Es una colección de datos ordenada, modificable y que permite duplicados.
* **Set**: es una colección de datos desordenada, pero indexada, que no permite modificaciones y tampoco duplicados.
* **Diccionario**: es una colección de datos desordenada, modificable e indexada, que funciona por par clave-valor, y que no permite duplicados.

## Crear una Tupla

Para crear una tupla tenemos que crear un objeto de tipo ```tuple()```.

```Python
tupla = tuple() # Creamos un objeto vacío de tipo tuple
```

O bien podemos usar directamente los paréntesis ```()```.

```Python
tupla = ()
```

Una tupla, cuando se crea y está vacía, tendrá cero elementos dentro.

```Python
tupla = tupla()
print(len(tupla))
# Devuelve 0
```

Pero, ¿y si quiero crear una tupla con datos? Pues es exactamente igual, pero añadiendo datos dentro de los paréntesis.

```Python
letras = ('a', 'b', 'c', 'd')
numeros = (1, 2, 3, 4, 5)
lenguajes = ('Python', 'Java', 'R', 'C#', 'Visual Basic', 'JavaScript')
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
# Indicará 4
```

```Python
tupla = ('Sun', 'Venus', 'Mercurio', 'Marte', 'Tierra')
print(f'Planetas en la lista {len(tupla)}')
print(f'Planetas: {tupla}')
```

## Datos de una Tupla

Los datos que se pueden guardar en una tupla no tienen porqué ser los mismos. A diferencia de otros lenguajes, cuando se crea un array, éste debe contener siempre el mismo tipo de dato, como en Java.

Pero en Python, las tuplas permiten que los datos puedan ser diferentes, incluso que contengan otra matriz de datos.

```Python
tupla_rara = (1, 2, 'Tres', 'Cuatro', [1, 3, 4])
```

## Accediendo a las posiciones de una tupla

Podemos acceder a la tupla, para entendernos, desde la izquierda (posición 0) o desde la derecha (última posición), pero para acceder a su última posición se usan los negativos.

Vamos a verlo mejor con un ejemplo.

```Python
mi_tupla = ('Red', 'Orange', 'Blue', 'Black')
#           0       1        2       3
```

En este fragmento de código vemos que la tupla empieza en 0 y acaba en 3, siendo 0 'Red' y 3 'Black'. Por lo que sabemos siempre que la primera posición será cero, 3 la última.

Si escribimos ```mi_tupla[1]``` sabemos que accederemos al valor 'Orange'.

Y ahora veremos el índice contrario.

```Python
mi_tupla = ('Red', 'Orange', 'Blue', 'Black')
#           -4      -3       -2       -1
```

Ahora, si queremos acceder al último valor, pero no sabemos cuántos elementos tiene la tupla (aunque se puede calcular), bastaría con acceder a la posición -1.

Te puedes estar preguntando si por la izquierda se usa el 0, porque en la derecha no. La respuesta es que hay que diferenciarlo de algún modo, podría haberse usado el -0, pero como 0 es un número que no tiene signo negativo ni positivo, porque es neutro, se decidió el -1.

Y tiene sentido.

Ahora, si accedemos a ```mi_tupla[-3]``` estaremos accediendo a 'Orange'.

## Desempaquetando todos los items

Al igual que con las listas, podemos desempaquetar una tupla en sus respectivas variables.

```Python
mi_tupla = ('A', 'B', 'C', 'D', 'E', 'F')
a, b, c, d, e, f  = mi_tupla
print(a) # Imprime 'A'
print(b) # Imprime 'B'
print(c) # Imprime 'C'
print(e) # Imprime 'E'
print(f) # Imprime 'F'
```

También podemos desempaquetar parcialmente una tupla usando ```*``` seguido del nombre de la variable.

```Python
mi_tupla = ('A', 'B', 'C', 'D', 'E', 'F')
a, b, c, *resto  = mi_tupla
print(a) # Imprime 'A'
print(b) # Imprime 'B'
print(c) # Imprime 'C'
print(resto) # Imprime ['D', 'E', 'F']
```

También podemos desempaquetar parcialmente una tupla especificando un intervalo de posición.

```Python
mi_tupla = ['A', 'B', 'C', 'D', 'E', 'F']
tupla_troceada = mi_tupla[0:3] # Guarda sólo de la posición 0 a la 3
tupla_completa = mi_tupla[0:] # Guarda todos los elementos de la tupla, empezando por el 0.
tupla_pares = mi_tupla[::2] # Guardará los elementos pares: 'B', 'D', 'F'.
```

Esto es aplicable también usando el índice negativo que hemos visto anteriormente.

## Cambiar una tupla por una lista

Como las tuplas son inmutables, no podemos cambiar ninguno de sus valores cuando son creados. ¿Entonces y si necesitamos cambiar la tupla? ¿Cómo lo hacemos?

Pues el truco está en el título, podemos mutar un objeto a otro y aprovecharnos de sus propiedades, y las listas permiten modificaciones 😎

```Python
tupla = (1, 2, 3, 4, 5)
print(type(tupla))
# Devolverá tipo tupla
lista = list(tupla)
print(type(lista))
# Devolverá tipo lista
```

Modificamos la lista y luego hacemos lo mismo para convertirlo a tupla, pero usando ```tuple()```.

```Python
tupla = tuple(lista)
```

## Comprobar si existe un elemento en la tupla

Podemos comprar si un elemento se encuentra en una tupla usando el operador ```in```.

```Python
tupla = ('a', 'b', 'c')
print('a' in tupla) # Devuelve True
```

Si no estuviera, devuelve *False*

## Unir tuplas

Se pueden unir dos tuplas o más usando el operador ```+```.

```Python
tupla_1 = (1, 2, 3, 4, 5)
tupla_2 = (6, 7, 8, 9, 10)
tupla_3 = tupla_1 + tupla_2
```

Y no te tienes que preocupar de duplicados porque las tuplas los permiten.

## Elimnando tuplas

Para borrar una tupla se usa la función ```del```.

```Python
tupla = tuple()
del tupla
```

🎉 Y ya hemos acabado 🎉 Este tema es más cortito porque realmente es casi casi igual que las listas, es decir, muchas de los métodos de la lista los tendrás en la tupla, por lo que sería repetir un poco más de lo mismo.

Aún así, ¡felicidades!

***

Y ahora a [practicar](/10%20-%20Tuplas/ejercicios_tuples.md).