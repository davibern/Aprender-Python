# Operadores

Como en cualquier lenguaje de programación en Python también tenemos los operadores.

¿Y qué son? Símbolos mediantes los cuales podemos realizar operaciones que nos ayudarán a obtener resultados.

Existen varios tipos de operadores.

## Operadores Aritméticos

| Operador       | Símbolo | Descripción                                                |
|----------------|---------|------------------------------------------------------------|
| Suma           | +       | La adición de varios números                               |
| Resta          | -       | La sustración e varios números                             |
| Multiplicación | *       | Hallar el producto de dos o más factores                   |
| División       | /       | Distribución de un producto en varias partes               |
| Divisió entera | //      | Realiza una división pero descartando la parte fraccionada |
| Resto          | %       | Calcula la parte fraccionada de una división, su resto     |
| Potencias      | **      | Multiplicar por si misma un valor n veces                  |

## Operadores Relacionales

| Operador       | Símbolo | Descripción                                                |
|----------------|---------|------------------------------------------------------------|
| Mayor que           | >       | Devuelve True si el operador de la izquierda es mayor que el de la derecha                               |
| Mayor o igual que          | >=      | Devuelve True si el operador de la izquierda es mayor o igual que el de la derecha                          |
| Menor  | <       | Devuelve True si el operador de la izquierda es menor que el de la derecha                   |
| Menor o igual que       | <=       | Devuelve True si el operador de la izquierda es menor o igul que el de la derecha               |
| Comparación | ==      | Devuelve True si ambos operadores son iguales |
| Desigualdad          | !=       | Devuelve True si ambos operadores son diferentes     |

Si no cumple la condición entonces es Falso.

## Operadores de Asignación

| Operador       | Símbolo | Descripción                                                |
|----------------|---------|------------------------------------------------------------|
| Igualdad           | =       | Asigna el valor de la derecha a una variable                             |
| Sumar           | +=       | Suma el valor de la derecha al total de una variable                            |
| Restar           | -=       | Resta el valor de la derecha al total de una variable                             |
| Multiplicar           | *=       | Multiplica el valor de la derecha al total de una variable                             |
| División           | /=       | Divide el valor de la derecha al total de una variable                             |
| Resto           | %=       | Calcula el resto del valor de la derecha al total de una variable                             |
| Potencia           | **=       | Calcula la potencia del valor de la derecha al total de una variable                             |
| División sin resto          | //=       | Divide el valor de la derecha al total de una variable sin resto                             |

## Operadores Lógicos

| Operador       | Símbolo | Descripción                                                |
|----------------|---------|------------------------------------------------------------|
| Y           | and       | Devuelve True si ambos operadores son True                               |
| O          | or       | Devuelve True si uno de los operadores son True                            |
| No | not       | Devuelve True si ninguno operadores son True                   |

Si no cumple la condición entonces es False.

### Tablas de la Verdad

Los operadores lógicos nos llevan irremediablente (y muy necesariamente) a conocer la **Tabla de la Verdad**.

Esto, que puede sonar muy místico, en realidad es de lo *más importante que puedas aprender para poder programar*, porque toda lógica de un programa se basará, sí o sí, en saber el resultado de una condición.

Dominar las condicionales es imprescindible, y no es ya un tema para Python, sino para cualquier lenguaje.

Yo voy a ponerte un resumen de todo lo que hay escrito de las tablas de la verdad, pero tienes en la [wikipedia](https://es.wikipedia.org/wiki/Tabla_de_verdad) información mucho más detallada.

**Operador AND**

El operador AND, que significa Y, funciona de tal forma que necesita que todas las condiciones sean verdaderas, si una no lo es, entonces el resultado es falso.

* True and True -> True
* True and False -> False
* False and True -> False
* False and Flse -> False

Como vemos, sólo la primera condición es verdadera, porque siempre que tengamos una condición falsa, esta será falsa. El AND ('Y') es una condición muy restrictiva.

**Operador OR**

El operador OR, que signfica O, funciona de tal forma que necesita sólo que una de las dos condiciones sea verdadera, por lo tanto, es más laxa, porque permite más opciones.

* True or True -> True
* True or False -> True
* False or True -> True
* False or False -> False

**Operador XOR**

Esta se da menos, se llama **OR Exclusivo**, es decir, que implementa el O únicamente. Me explico, una salida verdadera resulta si una, y sólo una de las entradas a la puerta es verdadera. Si ambas entradas son falsas, o ambas son verdaderas, resulta en una salida falsa. Sé que cuesta un poco de entender, pero piensa que necesitas que una sea falta y otra verdadera para devolver verdadero, si ambas son iguales, es falso.

El operador en Python es '^'.

* True ^ True -> False
* True ^ False -> True
* False ^ True -> True
* False ^ False -> False

# ¡Y hay más!

Hay varios más, pero para empezar creo que no está mal, hay que ir poco a poco.

Yo te he puesto los que considero imprescindibles, porque luego hay operadores bit a bit, de identidad, etc., que seguro que en algún otro momento los podremos ver y los asentaremos mejor cuando más conocimientos tengamos.

Igualmente te dejo aquí dos enlaces por si quieres tener más detalles o no quieres esperarme 😜

* [Página oficial de Python](https://docs.python.org/es/3/tutorial/introduction.html#)
* [Freecodecamp](https://www.freecodecamp.org/espanol/news/operadores-basicos-en-python-con-ejemplos/)

# Toca practicar

Ahora toca practicar lo que acabamos de leer. Te dejo por aquí el enlace al los [ejercicios](/5%20-%20Operadores/ejercicios_operadores.md), ¡al lío!

***

⬅️ [Clase anterior](/4%20-%20Tipos%20de%20datos/readme.md) | [Clase siguiente](/6%20-%20Biblioteca%20Est%C3%A1ndar/readme.md) ➡️