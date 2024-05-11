# Variables

Una variable guarda un dato (el que sea) en una zona de memoria de tu ordenador. Antiguamente habia que guardar los datos en zonas y apuntar esas zonas para volverlas a invocar, sus nombres no eran simples y ayudaban a recordar qué guardaba.

De ahí que fuese tan importante para el mundo de la programación las llegadas de las variables, porque, con ayuda nemotécnica podemos saber qué guarda y qué tipo.

Por lo tanto, una variable es una referencia a un lugar de la memoria que almacena un valor.

Para crear una variable se recomienda que:

* Que su nombre sea algo descriptivo, es decir, que al leerlo ya sepas que almacena y su tipo
* Tiene que intentar ser corto.
* No tiene que tener al principio:
   * Números
   * Espacios
   * Caracteres especiales
   * Guión

Además, para Python, las variables se escriben en minúscula y separados por barra baja, como por ejemplo, first_name, last_name, etc.

Este estilo se llama **snake_case**, porque simula el de una serpiente, y llamándose el lenguaje Python, tiene todo el sentido del mundo usar este. ¿no? 😄

Te dejo algunos otros ejemplos de nombres de variables válidos

```
first_name
last_name
age
country
location
number1
num1
day_of_birthday
year
city
capital
is_open
```

Y nombres de variables no permitidos

```
first-name
first@name
num-1
121num
```

## Asignar una variable

Ya, más o menos, tenemos claro cómo llamar a nuestra variable, y ahora, ¿cómo la creo?

Fácil, las variables se escriben de izquierda a derecha, luego se usan el signo de igual y luego va el valor.

Te dejo algunos ejemplos válidos:

```Python
first_name = 'davibern'
job = 'developer'
country 'Spain'
city = 'Seville'
age = 288
is_married = True
hobbies = ['videogames', 'develop', 'reading']
```

Te recuerdo que tienes el tema de los [tipos de datos](/04_Tipos_de_datos/readme.md).

## Cómo guarda Python el dato en memoria

Python es muy efectivo con el rendimiento de memoria porque guarda en su espacio de memoria el valor de una variable, y lo referencia a la misma. Por ejemplo, si tenemos una variabla a que vale 5, y una variable b que vale 5 también, lo que hará Python será referenciar para ambas variables el único valor que se ha guardado en el espacio de memoria (5), tal y como se hace con un puntero.

Como consecuencia de esto tenemos el **tipado dinámico**.

Esto tiene algunos matices, como que realmente cuando asignamos un valor a una variable, estamos referenciando dicho valor en el espacio de memoria, y esa referencia no cambia.

Véamoslo con un ejemplo:

```Python
id(5)
#10771648

a = 5
id(a)
#10771648

b = a

id(b)
#10771648

a = 7

id(a)
#10771712

id(7)
#10771712
```

Como vemos con estos ejemplos, el valor de 5 es el mismo porque realmente es la misma referencia, y de hecho, como poder podemos cambiar el valor de una referencia, pero lo que estamos haciendo realmente es referenciar otra distinta, no cambiar a la referencia, es un poco lío, lo sé 😵‍💫.

Tenemos incluso el **operador de identidad** para comprobar si una variable es igual a otra, y esto lo hacemos con ```is```, veamos algunos ejemplos:

```Python
a = 5
b = 5

a is 5
# true

a is b
# true

a is not b
# false

b = 7
a is b
# false
```

## Python infiere el tipo de datos (tipo dinámico)

Tal y como se explicó en el tema de tipos de datos, **Python infiere de forma dinámica el tipo de dato**. A diferencia de por ejempo Java, donde es imperativo a parte de crear la variable, indicar su tipo.

<u>Variable en Pyhon</u>

```Python
first_name = 'davibern'
```

<u>Variable en Java</u>

```Java
String FirstName = 'davibern'
```

Como se puede ver, Java necesita que le digas primero, qué tipo de dato vas a almacenar, su nombre, y luego el valor. Pero en Python esto no es necesario.

En cualquier caso, podemos indicar el tipo cuando creamos la variable, pero esto no forzará el tipo, es decir, si creas una variable de tipo String, luego puedes cambiarle tipo a un Integer, que Python no se va a quejar.

![Crear variable en Python](/99_Imagenes/variables.png)

Como puedes ver en la imagen, indico el tipo:

```Python
name:str = 'davibern'
```

Pero luego le he cambiado el tipo a un número, y cuando ejecuto ```type(name)``` el dato que indica es ```int```.

Entonces, ¿para qué sirve indicarle el tipo a una variable si podemos cambiarla?

Este uso lo podemos usar como buenas prácticas, es decir, si estamos programando en algún equipo, le estaríamos diciendo al resto de compañeros que este tipo que creo es X, y que no se debería de cambiar.

O incluso para nosotros mismos, para que más adelante, recordemos el porqué lo hemos configurado de un tipo u otro.

## A practicar

Ahora llega el momento de [practicar lo aprendido](/07_Variables/ejercicios_variables.md), ¡vamos a ello!

***

⬅️ [Clase anterior](/06_Biblioteca%20Est%C3%A1ndar/readme.md) | [Clase siguiente](/08_Strings/readme.md) ➡️