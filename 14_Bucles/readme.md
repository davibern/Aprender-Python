# Bucles (Loops)

Los bucles son las otras **estructuras de control**, además de las condicionales, que nos ayudan en programación a tomar decisiones.

¿Y qué es un **bucle**? Una tarea que se repite durante un momento determinado (según la condición que tenga dicho bucle).

Y hay dos tipos de bucles:

* Bucle *while*
* Bucle *for*

## Bucle while

En Python usamos la palabra reservada *while* para iniciar un bucle, podemos traducir ```while``` por ```mientras```.

Y su síntaxis sería:

```Python
while condition:
    # haz algo tantas veces seguidas
```

Que se podría traducir por:

```
mientras (se cumpla esta condición):
    # haz algo tantas veces seguidas
```

Vamos a verlo ya con un ejemplo real.

```Python
i = 0
while (i < 10):
    print('Su valor es de', i)
    i = i + 1
```

¿Que está pasando en este bloque de código?

* Se ha creado una variable que vale 0
* Se ha creado un bucle con una condición, que mientras que ```i``` sea menor a 10 se va a ejecutar lo siguiente:
    * Se va a imprimir por salida estándar el valor de ```i```
    * Se va a incrementar el valor de ```i``` en +1
    * En la siguiente interacción ```i``` ya no vale 0, sino 1, y así sucesivamente hasta que valga 10.
    * En el momento que valga 10, la condición ya no será ```True```, sino ```False```, y no se ejecutará el bloque que hay dentro del ```while```.

Y aquí viene ahora una cosa muy interesante de **Python**, y es que a diferencia de otros lenguajes de programación, a un bucle le podemos añadir también un ```else```, para que se ejecute cuando un bucle termina.

```Python
while condition:
    # haz algo tantas veces seguidas
else:
    # haz algo diferente para cuando no se cumpla la condición
```

```Python
i = 0
while (i < 10):
    print('Su valor es de', i)
    i = i + 1
else:
    print('El contador final es', i)
```

### Romper y continuar el bucle while

Se pueden dar situaciones en las que necesitamos parar un bucle, y no esperar a que la condición sea ```False```, ¿cómo?

Con las palabras reservadas:

* ```break```: se usa cuando queremos salir o detener un bucle.
* ```continue```: se puede omitir la interacción actual y continuar en la siguiente, sin pararla.

<u>break</u>

```Python
while condition:
    # Código a ejecutar
    if new_condition:
        break
```

```Python
i = 0
while i < 10:
    print(i)
    i = i + 1
    if i == 5:
        print(f'Se ha llegado a {i}, se para')
        break;
```

Si te fijas, estamos incrementando ```i``` en 1 por cada iteracción, y el bucle durará 10 iteracciones, pero lo vamos a parar cuando llegue a 5, porque estamos añadiendo una condicional al bucle, si llega ```i``` a 5, te paras (con ```break```).

<u>continue</u>

```Python
while condition:
    # Código a ejecutar
    if new_condition:
        continue
```

```Python
i = 0
while i < 10:
    if i == 5:
        # Hacer algo...
        continue
    print(i)
    i = i + 1
```

Sólo imprimirá hasta 4, y el bucle se quedará esperando ha hacer algo.

## Bucle for

El bucle ```for``` difiere del ```while``` en que en vez de ejecutarse indefinidamente hasta que una condición deje de ser ```True```, ```for``` se usa más bien para iterar sobre una secuencia, es decir, sobre una estructura de datos de las cuales conocemos su principio y su final.

```Python
for iterador in lista:
    # haz algo repetidamente hasta que lleguemos al final de la lista
```

Lo vemos mejor con un ejemplo más práctico.

```Python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for numero in numeros:
    print(numero)
```

Este bloque imprimirá por pantalla desde la posición 0 hasta la 10, todos los elementos, uno a uno, y cuando llegue al final, terminará.

Y como funciona tan bien con estructuras de datos, podemos hacerlo sobre una palabra por ejemplo.

```Python
palabra = 'Python'
for letra in palabra:
    print(letra)
```

¿Qué crees que imprimirá este bloque de código? Pruébalo tu mismo a ver qué sale.

Si ya sabes programar, quizás te puedas sentir más cómodo con esta otra sintaxis.

```Python
palabra = 'Python'
for i in range(len(palabra)):
    print(palabra[i])
```

El resultando es exactamente el mismo.

Ahora bien, ¿y si queremos iterar sobre un diccionario? Porque un diccionario contiene un par que es clave-valor, ¿cómo se haría?

```Python
diccionario = dict()
for iterador in dict:
    # tu código
```

Pues como ves, no es muy diferente, eso sí, para acceder a la clave antes hay que especificarlas en el iterador.

Y además, hay que añadirle el método ```items()``` al diccionario para que pueda acceder a ambos (clave y valor).

Mejor lo vemos en el siguiente ejemplo.

```Python
coche = {
    'brand': 'Citroen',
    'model': 'C4 Cactus',
    'cv':    110,
    'cc':   1200
}

for key, value in coche.items():
    print(key, value)
```

O bien, imprimir sólo la clave:

```Python
for key in coche:
    print(key)
```

En el ```for``` también podemos usar ```else``` para hacer algo si se termina la secuencia.

```Python
lista = list()
for iterador in lista:
    # hacer algo
else:
    # hacer algo otro
```

Y para terminar con una breve explicación, podemos anidar bucles.

```Python
for i in j:
    for z in i:
        print(z)
```

¿Y se te ocurre qué ejemplo viene bien en un anidamiento del bucle for? Los diccionarios, porque como éstos tienen dos dimensiones, podemos obtener su clave y su valor.

```Python
coche = {
    'brand': 'Citroen',
    'model': 'C4 Cactus',
    'cv':    110,
    'cc':   1200,
    'accesories':   ['radio', 'bluetooth', 'android']
}

for key in coche:
    if key == 'accesories':
        for accesorie in coche['accesories']:
            print(accesorie)
```

### Romper y continuar con un bucle for

Al igual que con ```while```, podemos parar el bucle for con las siguientes palabras reservadas:

* ```break```: lo usaremos para parar el bucle antes de su finalización.
* ```continue```: lo usaremos para sltarnos algunos de los pasos de la iteracción.

<u>break</u>

```Python
numeros = (0,1,2,3,4,5)
for numero in numeros:
    print(numero)
    if numero == 3:
        break
```

<u>continue</u>

```Python
numeros = (0,1,2,3,4,5)
for numero in numeros:
    print(number)
    if numero == 3:
        continue
    print('El siguiente será ', numero + 1) if numero != 5 else print("Final")
print('Fuera del for')
```

## Bucle Range

La función ```range()``` se usa para listar números. Se necesitará un argumento de inicio y otro de final, para crear una sencuencia de números.

Además, también se necesitará un argumento para indicar el incremento.

```Python
lista = range(1, 10, 1)
# Creará una lista con los valores del 1 al 10, y de uno en uno
```

```Python
lista = range(1, 10, 2)
# Creará una lista con los valores del 1 al 10, y de dos en dos
```

```Python
# Creará un rango de 20 números, de uno en uno, y los imprimirá usando el bucle for
for numero in range(20):
    print(numero)
```

## Pass

Podemos usar ```pass``` para indicar que no se va a ejecutar ningún código en el bloque que hayamos implementado. Es una manera de indicar que tenemos una función o bloque, pero que éste no hará nada, para evitar errores.

```Python
for number in range(100):
    pass
```

🔔 Seguimos avanzando y estás a tope con Python 🔔

Ahora toca los [ejercicios](/14_Bucles/ejercicios_bucles.md), ¿te animas?

***

⬅️ [Clase anterior](/13_Condicionales/readme.md) | [Clase siguiente]() ➡️