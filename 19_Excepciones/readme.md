# Excepciones

Cuando un programa falla, éste normalmente genera un error, este tipo de errores (algunos más molestos que otros) generan una mala experiencia de usuario.

Por ejemplo, en un programa de escritorio, si éste se cierra abruptamente (con o sin mensaje de error) dejará al usuario sin saber qué ha pasado. Porque si se cierra sin mensaje del error el usuario no sabrá que ha pasado.
Pero si se cierra con un mensaje de error que no somos capaces de controlar, el usuario seguramente verá una serie de datos que no le son familiares y se quedará igual que si no mostramos el error.

El control de errores es super importante en nuestros desarrollos y Python no es menos en este sentido. ¿Y cómo controlamos los errores? Con el **control de excepciones**.

## Control de excepción

Para controlar el error en Python usamos los bloques ```try-except```. Dentro del ```try``` irá el bloque de código que es sensible a una excepción (un objeto que no se pueda abrir, una división por cero, una operación con tipos incompatibles, etc., etc., etc.).

Luego en el ```except``` irá la sentencia para controlar el error, ¿qué hacemos si se da un error? Por ejemplo un aviso al usuario, un control del log del programa, un aviso a otro programa, un rollback, etc., etc., etc.

Por lo tanto, la síntaxis básica del control de errores sería:

```Python
try:
    # Aquí va el código que puede dar error
except:
    # Y aquí va lo que haremos si se da el error
```

Vamos a verlo con un ejemplo claro.

```Python
# Voy a realizar una división por cero
a = 5
b = 0

print(a/b)
```

Si ejecuto el programa, la shell de Python me devolverá lo siguiente, muy resumidamente:

```
print(a/b)
ZeroDivisionError: division by zero
```

¿Qué está ocurriendo? Que no estamos controlando el error de una división por cero, o en este caso, que haya una excepción, sea cual sea, y estamos mostrando el error por defecto de Python, que a un usuario de nada le vale.

Vamos a mejorar este código añadiendo la excepción.

```Python
a = 5
b = 0

try:
    print(a/b)
except:
    print("Error: división por cero")
```

Ahora, tendremos una salida muchísimo más elegante a nuestro error y el usuario sabrá que está pasando.

```
Error: división por cero
```

## Controlando una excepción conocida

Cuando usamos ```except``` sabemos que puede haber un error, pero no cual, pero en el ejemplo anterior sabemos perfectamente que podemos tener un error por división por cero, ¿entonces vamos a afinar aún más el control del error no?

Para ello añadimos el error que nos devuelve Python justo a la derecha de ```except```.

```Python
a = 5
b = 0

try:
    print(a/b)
except ZeroDivisionError:
    print("Error: división por cero")
```

¿Te das cuenta que hemos incluido ```ZeroDivisionError``` como excepción? Esto es porque lo conocemos. Cuando Python devuelve un error, siempre te dirá qué tipo de error es, y está siempre en la Shell, tal y como te mostré antes.

Podemos añadir tantos como se den en nuestro programa.

```Python
try:
    print(5/'0')
except ZeroDivisionError:
    print("Error: división por cero")
except TypeError:
    print("Error: tipo de dato")
except ValueError:
    print("Error: tipo de valor")
```

Aquí nos devolvería ```Error: tipo de dato``` porque estaría entrando por ```TypeError```.

## Entradas y salidas de la excepción

El control de excepción siempre tendrá obligatoriamente dos instrucciones:

* ```try:``` que es el bloque a evaluar
* ```except:``` que es el bloque que se ejecuta si entra en el error

Mínimo tiene que entrar en ambos, no puedes añadir un ```try``` sin la excepción porque Python se va a quejar.

Ahora bien, y si tenemos varias excepciones, como en el ejemplo anterior, ¿se ejecutan todas las exepciones?

La respuesta es **no**. Sólo se ejecuta la excepción que provoque el error, no pasa por todas, de lo contrario, Python mostraría las tres líneas de salida de errores, y en realidad, sólo muestra la que proceda.

Pero, adicionalmente, tenemos dos ejecuciones opcionales, para completar nuestro control de errores:

* ```else:``` controlará la ejecución si no se da un error
* ```finally:``` se ejecutará siempre que termine el bloque de control de excepciones

### Excepción else

Cuando añadimos el bloque ```else``` le estamos indicando a Python que si nuestro bloque no da error que ejecute la segunda salida.

Esta segunda salida, el else, si el error se produce, no saltará. Funciona realmente como el else en las condicionales, ¿te acuerdas?

```Python
try:
    print(5/5)
except:
    print("Error en la operación")
else:
    print("Operación realizada")
```

En este ejemplo vamos a dividir ```5/5```, evidenemente no tienen ningún error, así que va mostrar por la salida estándar ```1```, pero luego, como **no ha saltado ninguna excepción** se va a ejecutar el **else**, y mostrará la salida "Operación realizada"

```
1.0
Operación realizada
```

Pero si nos diera error, no ejecutaría la línea del **else**.

### Excepción finally

La excepción **finally**, que también es opcional como la anterior, si la incluimos se ejecutará siempre en el código de nuestro pograma.

Es decir, se ejecuta el bloque try, si hay o no hay error, éste lanzará el **finally** para terminar el bloque de control de errores. Si hubiera un **else** éste se ejecutará y por último el cierre.

Veámoslo con un ejemplo:

```Python
try:
    print(5/5)
except:
    print("Error en la operación")
else:
    print("Operación realizada con éxito")
finally:
    print("Cierre del programa")
```

En este caso se mostrará la siguente salida:

```
1.0
Operación realizada con éxito
Cierre del programa
```

⭐ ¿Cómo lo has visto? ¿Fácil verdad? ⭐

Pues ahora vamos con los [ejercicios](/19_Excepciones/ejercicios_excepciones.md).

***

⬅️ [Clase anterior](/18_Lista_Compacta/readme.md) | [Clase siguiente]() ➡️