# Diccionarios

Como ya habrás visto en la [clase de tipos de datos](/04_Tipos_de_datos/readme.md), existen varios tipos de colecciones, este recordatorio lo voy a incluir en cada una de ellas, porque machacar información es también la mejor manera de que entre en la cabezita 🤯

Pero primero, ¿qué es Set?
 
> Es una colección de datos desordenada, modificable e indexada, que funciona por par clave-valor, y que no permite duplicados.

Es decir, en Python usamos los sets para almacenar elementos únicos, a los que les podemos ejecutar *uniones*, *intersecciones*, *diferencias*, *simetrías*, etc.

Y ahora el resto:

* **Lista**: es una colección de datos ordenada, modificable y que permite duplicados.
* **Tupla**: es una colección de datos ordenada, pero que no permite modificar los datos. Y permite duplicados.
* **Set**: es una colección de datos desordenada, pero indexada, que no permite modificaciones y tampoco duplicados.

## Crear un diccionario

Podemos crear un diccionario usando la función ```dict()``` que pertenece a una función básica de Python, o bien, las llaves ```{}```, incorporando dentro el par *clave-valor*.

```Python
dct_vacio = dict()
dct_con_datos = {'key1': '1', 'key2': '2', 'key3': '3'}
```

Te dejo otro ejemplo de diccionario que seguro que viene mejor para entenderlo.

```Python
car = {
    'brand':    'Citroen',
    'model':    'C4-Cactus',
    'color':    'green',
    'cv':       110,
    'cc':       1200,
    'doors':    5,
    'accesories' :  ['android', 'google maps', 'radio', 'bluetooth']     
}
```

Como puedes ver, el diccionario se comporta como un objeto complejo que puede albergar dentro otros tipos de datos y estructuras.

Y su construcción siempre va estar estructurada en:

* la referencia del dato que será siempre string.
* el dato en sí que podrá ser un string, número, decimal, booleano, lista, etc.

## Calcular la longitud de un diccionario

Para calcular la longitud de un diccionario se usa la función ```len()``` que contará la cantidad de llaves (keys) que tenga.

```Python
dct = {'key1': '1', 'key2': '2', 'key3': '3'}
print(len(dct)) # Devuelve 3
```

## Acceder al elemento de un diccionario

Para acceder a un elemento de un diccionario usaremos su *key*, dejo un ejemplo para verlo más claro.

```Python
persona = {
    'fist_name':    'davibern',
    'last_name':    'dev',
    'age':          288,
    'is_married':   True,
    'country':      'Spain'
}

print(persona['first_name']) # Devuelve 'davibern'
print(persona['is_married']) # Devuelve True
```

Pero, ¿qué ocurre si intentas acceder a una llave que no exista? Pues que obtendremos un error. Para evitar esto último tendremo que comprobar primero si dicha *key* existe usando un *if*, o bien, usando el método ```get()```.

Este método devuelve ```None``` si la llave no existe.

```Python
print(persona['country']) # Devuelve Spain
print(persona['job']) # Devuelve None porque no está especificado 'job' como llave de 'persona'
```

## Añadir un elemento al diccionario

Fácil, para añadir un nuevo elemento, llamamos al objeto, y le asignamos uno nuevo indicando nombre de la key, y por supuesto, su valor.

```Python
dct = {'key1': '1', 'key2': '2', 'key3': '3'}
dct['key4'] = '4'
```

## Modificando un diccionario

Igualmente, y con el método anterior, podemos modificar un diccionario, haciendo referencia a la llave y luego cambiando su valor.

```Python
dct = {'key1': '1', 'key2': '2', 'key3': '3'}
dct['key3'] = 3
```

## Comprobar si un elemento se encuentra en un diccionario

Al igual que con las otras estructuras de datos, esto se hace con el operador ```in```. Lo que se hace es comprobar si se encuentra la llave en el diccionario.

```Python
dct = {'key1': '1', 'key2': '2', 'key3': '3'}
print('key' in dct)
```

## Eliminar un elemento

Para eliminar un elemento tenemos varios métodos:

* pop(): elimina un elemento indicando la llave como argumento.
* popitem(): elimina el último elemento del diccionario.
* del(): elimina un elemento indicando su llave (igual que pop())

```Python
dct = {'key1': '1', 'key2': '2', 'key3': '3'}
dct.pop('key3') # Elimina el elemento cuya llave es 'key3'
dct.popitem() # Elimina el último elemento
del dct['key2'] # Elimina el elemento cuya llave es 'key2'
```

## Cambiar un diccionario a una lista

Podemos cambiar un diccionario a una lista, esto nos creará una lista de tuplas. Mejor lo vemos con un ejemplo. ¿Y cómo se hace? Usando el método ```items()```.

```Python
dct = {'key1': '1', 'key2': '2', 'key3': '3'}
print(dct.items()) # Devuelve: dct_items(['key1', '1'], ['key2', '2'], ['key3', '3'])
```

Si te fijas, cada par de clave valor lo ha pasado a una tupla, y habrá una por cada par clave-valor.

## Limpiar un diccionario

Podemos limpiar un diccionario con el método ```clear()```. Esto elimanará cada par clave-valor, pero no el diccionario.

```Python
dct = {'key1': '1', 'key2': '2', 'key3': '3'}
dct.clear()
```

## Elimninar un diccionario

Con ```del``` borramos el diccionario.

```Python
dct = {'key1': '1', 'key2': '2', 'key3': '3'}
del dct
```

## Copiar un diccionario

Para copiar un diccionario usamos ```copy()```, con esto evitamos las modificaciones que se le hagan al diccionario principal.

```Python
dct = {'key1': '1', 'key2': '2', 'key3': '3'}
dct_2 = dct.copy()
```

## Obtener las claves de un diccionario como una lista

Con el método ```keys()``` obtendremos una lista de las claves (llaves) del diccionario.

```Python
dct = {'key1': '1', 'key2': '2', 'key3': '3'}
claves = dct.keys()
print(claves) # Devuelve ['key1', 'key2', 'key3']
```

## Obtener los valores de un diccionario como una lista

Con el método ```values()``` obtendremos una lista de los valores del diccionario.

```Python
dct = {'key1': '1', 'key2': '2', 'key3': '3'}
claves = dct.values()
print(claves) # Devuelve ['1', '2', '3']
```

Y hasta aquí lo más notorio de los diccionarios, como ves, y si ya conoces otros lenguajes de programación, los diccionarios funcionan como una clase.

☀️ ¡Sigues brillando con tu esfuerzo y dedicación! ☀️

Ahora ya sabes lo que toca, ¡[practicar](/12_Diccionarios/ejercicios_diccionarios.md)!

***

⬅️ [Clase anterior](/11_Sets/readme.md) | [Clase siguiente]() ➡️