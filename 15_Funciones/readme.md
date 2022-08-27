# Funciones

Una función es un bloque de código que guardas como una variable con la finaidad de poder reutilizarla más adelante. Este bloque de código que realiza una tarea en concreto se crean con la idea de reutilizar código.

Si puedes hacer algo varias veces, escríbelo sólo una vez, así ahorras líneas de código, y éste será más legible.

Las funciones pueden hacer principalmente dos cosas:

* Realizar una ejecución sin devolver nada.
* Realizar una ejecución devolviendo un dato.

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

Y para rizar el rizo, podemos llamar a una función dentro de otra función. Esto es de lo más normal en programación.

```Python
def nombre(nombre):
    return nombre
def longitud_nombre(nombre):
    return len(nombre)

print(longitud_nombre(nombre('davibern')))
# Devolverá 8
```

Puede que el ejemplo no sea el mejor del mundo, pero espero que se capte el mensaje 🤓

😀 Estamos llegando bastante lejos, y estás siendo muy perseverante, mi más sincera enhorabuena 😀

Ahora vamos con los [ejercicios](/15_Funciones/ejercicios_funciones.md).

***

⬅️ [Clase anterior](/14_Bucles/readme.md) | [Clase siguiente](/16_Modulos/readme.md) ➡️