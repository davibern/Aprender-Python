# Funciones

Una función es un bloque de código que guardas como una variable con la finaidad de poder reutilizarla más adelante. Este bloque de código que realiza una tarea en concreto se crean con la idea de reutilizar código.

Si puedes hacer algo varias veces, escríbelo sólo una vez, así ahorras líneas de código, y éste será más legible.

Las funciones pueden hacer principalmente dos cosas:

* Realizar una ejecución sin devolver nada.
* Realizar una ejecución devolviendo un dato.

Ten en cuenta además que como en ```Python``` todo es un objeto, las funciones también lo son, __por lo que puedes asignar una función a una variable, y pasar una función como parámetro de otra función__.

Además, si te fijas, ya has estado usando funciones desde el principio, ahora la diferencia, es que vamos a crearla.

En Python, una función se define por la palabra reservada ```def```.

¿Y cuándo se ejecuta una función? Cuando la invocas en tu código.

La síntaxis para declarar una función e invocarla es la siguiente:

```Python
# Crear función
def mi_funcion():
    # código

# Invocar función
mi_funcion()
```

Las funciones pueden ejecutarse con parámetros o sin parámetros.

## Función sin parámetros

Una función sin parámetros se declara cuando dentro de los ```()``` no hay nada. Esto quiere decir que nuestra función ejecutará algo y no le hará falta ningún dato del exterior para funcionar.

```Python
def decir_hola():
    print('Buenos días')
decir_hola()
# 'Buenos días'
```

## Función con parámetros

A diferencia del anterior, la función con parámetros signitiva que dentro de los ```()``` se incluye una referencia a un dato, esta referencia sólo se usa dentro del bloque de la función, no es accesible desde fuera.

Piensa en ello como una variable que sólo puede usarse para la función, y nada más.

```Python
def decir_hola(nombre):
    print('Buenos días', nombre)
decir_hola('davibern')
# 'Buenos días davibern'
```

¿Esto significa que ```nombre``` sólo puede declararse una vez en mi código? No, porque como digo, ```nombre``` es una variable interna de la función. Lo verás más claro con este ejemplo.

```Python
nombre = 'davibern'
def decir_hola(nombre):
    print('Buenos días', nombre)
decir_hola(nombre)
# 'Buenos días davibern'
```

Ahora bien, si quiero usar la variable de forma global, aunque esté definida dentro de una función, también se puede hacer. Recuerda que una función es también un __objeto__, por lo que puedes devolver un dato desde una función.

Esto lo haremos con la palabra reservada ```global``` y el nombre de la variable. Ahora bien, esto no es una buena práctica, ya que si tienes muchas funciones, y estás usando variables globales, puede que te encuentres con problemas de legibilidad y mantenimiento de tu código, así que no lo hagas, pero es bueno que sepas que se puede hacer, y que es una opción que tienes disponible si lo necesitas.

Vamos a ver un ejemplo de lo que te comento.

```Python
def operar(a, b):
    global resultado
    resultado = a + b
    print(resultado)

operar(2, 3)
print(resultado)
```

Una función puede incluir tantos parámetros como nos haga falta en el diseño de la misma.

```Python
def suma(x, y):
    print('Suma:', x + y)
suma(4, 2)
```

El orden de los parámetros es el que indicamos por defecto, pero podemos cambiarlo cuando los invocamos, pongo mejor un ejemplo.

```Python
def suma(x, y):
    print('Suma:', x + y)
suma(y = 4, x = 2)
```

Ahora bien, también podemos indicar que un parámetro tenga un valor por defecto si cuando se usa la función, no se añade ninguno.

Imagina que tenemos una función para calcular un porcentaje. Si no añadiésemes argumentos, la división nos dará un error, con el valor por defecto evitamos esto último.

```Python
def dividir(numerador = 100, denominador = 100):
    print(f'{numerador} de {denominador} representa {(numerador / denominador) * 100}%')
dividir()
dividir(25, 100)
```

## Función con retorno

La función, como indicaba al principio, puede devolver un dato o *ninguno*. Esto en otros lenguajes de programación puede que sea vea más claro, como en ```Java```, que tenemos funciones ```void```, que simplemente ejecutan el código para, por ejemplo, cambiar el estado de una clase, o bien, una función que tiene un tipo de dato, esto significa que la función devolverá ese tipo de dato.

En Python esto no es así del todo. Una función que no devuelva nada, sí devuelve algo, ese algo es ```None```. ¿Entonces cómo puedo saber si devuelve o no devuelve? Con la palabra reservada ```return```.

```Python
def sumar(a, b):
    return a + b
sumar(5, 3)
print(sumar(5, 3))
```

Este ejemplo devuelve la suma de ambas, ahora la diferencia es que si lo ejecutas, no verás nada por la salida estándar, tendrías que envolver la función con el print para mostrarlo.

Pongo un ejemplo un pelín más complejo.

```Python
valor = 5
def comprobar_valor(valor):
    if valor < 5:
        return 'Por debajo de 5'
    elif valor > 5:
        return 'Por encima de 5'
    else:
        return 'En equilibrio'

resultado = comprobar_valor(5)
print(resultado)
```

## Función con números arbitrarios de argumentos

Imagina que tienes una función que no sabes cuántos elementos vas a necesitar como parámetros. Es decir, no tienes ni idea de cuántos parámetros vas a necesitar, algunas veces serán 3, otra 20, otras 100.

Para hacer una función con elementos arbitrarios necesitarás añadir ```*``` antes de la definición del parámetro.

```Python
def mi_funcion(*args):
    # código
mi_funcion(arg1, arg2, arg3, arg4,...)
```

Ahora con un ejemplo se verás más claro.

```Python
def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(suma(1, 2, 3))
# Devolverá 6
```

Creamos una función llamada ```suma```, y le pasamos un parámetro arbitrario. Dentro creamos una variable ```total``` que se inicializa a 0, y luego tenemos un bucle que recorre todos los argumentos añadidos en el parámetro ```*args```, y por cada iteracción sumará el valor al anterior.

Por ultimo devuelve con ```return``` el valor de ```total```.

Se puede además mezclar parémetros definidos con arbitrarios.

```Python
def suma(multiplicardor, *args):
    total = 0
    for arg in args:
        total += arg
    return total * multiplicardor
print(suma(100, 1, 2, 3))
# Devolverá 600
```

## Funciones dentro de funciones

Podemos llamar a una función dentro de otra función. Esto es de lo más normal en programación.

```Python
def nombre(nombre):
    return nombre
def longitud_nombre(nombre):
    return len(nombre)

print(longitud_nombre(nombre('davibern')))
# Devolverá 8
```

## Funciones recursivas

Una __función recursiva__ es una función que se llama a si misma. Esto puede ser muy útil, por ejemplo, para recorrer una estructura de datos, como una lista, o un diccionario, o un árbol, etc. Pero hay que tener cuidado, porque si no se controla bien, puede que la función se llame a si misma indefinidamente, y esto puede provocar un error de pila de llamadas.

Un ejemplo de función recursiva sería por ejemplo el factorial de un número.

```Python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```

Esta función calcula el factorial de un número. El factorial de un número es el producto de todos los números enteros positivos desde 1 hasta ese número. Por ejemplo, el factorial de 5 es 5 * 4 * 3 * 2 * 1 = 120.

## Referenciar  funciones en variables

Como ya hemos comentado en ```Python``` todo es un objeto, y las funciones también. Puedes crear una función que ésta la puedes asignar a una variable y hacer que ésta sea también la misma función.

Mejor lo ves con este ejemplo:

```Python
def suma(a, b):
    return a + b

a = suma

print(a(5, 3))
# Devolverá 8
```

## Funciones anónimas o lambda

Las funciones anónimas o ```lambda``` son funciones que no tienen nombre, y que se definen en una sola línea. Se utilizan para definir funciones pequeñas y simples, que no se van a utilizar en otro sitio. Se definen con la palabra reservada __lamba__, y se utilizan de la siguiente manera:

```Python
cuadrado = lambda x: x ** 2
print(cuadrado(5))
# Devolverá 25
```

Y para qué podemos usar una lambda, pues por ejemplo, para ordenar una lista.

```Python
pares = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]
# Ahora cambiaremos la ordenación  de la lista por el segundo elemento de la tupla, es decir, el número, y no por el string.
pares.sort(key=lambda x: x[1])
print(pares)
# Devolverá [(2, 'two'), (4, 'four'), (1, 'one'), (3, 'three'), (5, 'five')]
```

## Decoradores en funciones

Un __decorador__ es una función que toma otra función y extiende el comportamiento de la segunda función sin cambiar su código. Por ejemplo imaginar que estamos haciendo algunas operaciones que tienen una primera parte que es muy similar (por ejemplo funciones que conectan con una base de datos, o abrir ficheros de texto), y todas las funciones una parte que es igual.

Pues podemos crear un decorador que se encargue de la parte común, y que las funciones que queramos que tengan ese comportamiento, se las pasemos como parámetro al decorador. Y el decorador se encargará de ejecutar la parte común, y luego ejecutará la función que le hemos pasado como parámetro.

Vamos a verlo con un ejemplo:

```Python
def tablas(funcion):
    def envoltura(tabla=1):
        print('Tabla del %i:' %tabla)
        print('-' * 15)
        for numero in range(0, 11):
            funcion(numero, tabla)
        print('-' * 15)
    return envoltura

@tablas
def suma(numero, tabla=1):
    print('%2i + %2i = %3i' %(numero, tabla, numero + tabla + numero))

@tablas
def multiplicar(numero, tabla=1):
    print('%2i x %2i = %3i' %(numero, tabla, numero * tabla))
```

## Generadores

Es un tipo especial de función que generan un iterador, y por lo tanto es una función que crea un generador, por cada vez que se ejecuta. Es decir, cada vez que se ejecuta la función, se crea un nuevo generador, y se puede recorrer ese generador con un bucle desde el último ítem que se haya recorrido hasta el final. Es decir, no se puede volver atrás, y no se puede acceder a un ítem concreto, solo se puede recorrer secuencialmente. Y cuando se llega al final, se vuelve a empezar desde el principio.

Veámoslo mejor con un ejemplo.

```Python
def par(inicio, fin):
    for i in range(inicio, fin):
        if i % 2 == 0:
            yield i

par(1, 10) # Devuelve un generador, que se puede recorrer con un bucle for, o con la función next()
for i in par(1, 10): # Devuelve 2, 4, 6, 8
    print(i)
```

😀 Estamos llegando bastante lejos, y estás siendo muy perseverante, mi más sincera enhorabuena 😀

Ahora vamos con los [ejercicios](/15_Funciones/ejercicios_funciones.md).

***

⬅️ [Clase anterior](/14_Bucles/readme.md) | [Clase siguiente](/16_Modulos/readme.md) ➡️