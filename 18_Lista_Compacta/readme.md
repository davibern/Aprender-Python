# Lista compacta

En Python podemos crear una lista compacta en una sola sentencia. Es una forma rápida y corta de crear una nueva lista.

Es muchísimo más rápido en proceso que crear una lista y luego iterarla.

```Python
# Sintaxis
[i for i in lista if expresion]
```

A simple vista puede parecer algo más complejo, pero qué mejor que ponerse a probar y practicar para cogerle el truco.

## Ejemplos de listas compactas

Imagina que tienes un string, y que tienes que convertirla a lista.

```Python
salida = 'Esto es el resultado de la función Y'
lista = list(salida)
```

Pero puedes hacerlo de una sola vez.

```Python
lista = [i for i in salida]
```

En este ejemplo no tienes que estar convertiendo los tipos.

Ahora piensa que necesitas generar una serie de números.

```Python
numeros = [i for i in range(21)] # rango del 0 al 20
print(numeros) # Mostrará la lista de números
```

Pero también podemos operar directamente en la lista compacta

```Python
cuadrados = [i * i in range(21)]
print(cuadrados) # [0, 1, 4, 9, 16, 25,...]
```

O incluso hacer una lista de tuplas

```Python
numeros = [(i, i * i) in range(21)]
print(numeros) # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), ...]
```

Pero las listas compactas van mucho más allá y permiten incluir expresiones.

```Python
pares = [i for i in range(21) if i % 2 == 0] # Generará números pares en la lista hasta 20
print(pares) # [0, 2, 4, 6, 8, 10, ...]

impares = [i for i in range(21) if i % 2 != 0] # Generará números pares en la lista hasta 20
print(impares) # [1, 3, 5, 7, 9, 11, ...]
```

## Funciones lambda

Una función [lambda](https://es.wikipedia.org/wiki/Expresi%C3%B3n_lambda) es una pequeña función anónima sin nombre, ésta puede contener una serie de argumentos, pero sólamente puede tener una expresión.

Las necesitaremos cuando queramos escribir una función anónima dentro de otra función.

Para crear una función lambda usamos la expresión **lambda** seguido de los parámetros y la expresión.

```Python
x = lambda parametro1, parametro2: parametro1 + parametro2
print(x(argumento1, argumento2))
```

Vemaos un ejemplo práctico para entenderlo mejor.

```Python
cuadrado = lambda x : x ** 2
print(cuadrado(4)) # 16
```

Como puedes ver la funcióin lambda es anónima, no se le está dando ningún nombre, se está aplicando a una variable, y siempre devuelve una expresión.

Ahora veamos cómo usarla dentro de una función.

```Python
def potencia(x):
    return lambda y: x ** y

# La función potencia necesita dos argumentos, la base y la exponencia.
# La base es x, la exponencia es la y, de ahí que se incluyan los argumentos
# entre paréntesis separados
resultado = potencia(2)(3) 
print(resultado)
```

¿Qué te está pareciendo las listas compactas? Potentes, ¿verdad? Son complicadas por el nivel de abstracción que tiene, pero super poderosas 💪🏻😤✊🏻

Ahora vamos con unos [ejercicios](/18_Lista_Compacta/ejercicios_lista_compacta.md) básicos.

***

⬅️ [Clase anterior](/17_Clases/readme.md) | [Clase siguiente](/19_Excepciones/readme.md) ➡️