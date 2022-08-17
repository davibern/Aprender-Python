# Strings

Empezamos a partir de ahora a profundizar un poco más en los tipos de datos y aprender sobre ellos. El primero va a ser el tipo de dato **texto**. Éste se llama **String**, y su traducción podría ser ***cadena de texto***.

Te recuerdo que una cadena de texto, a partir de ahora String, se puede escribir con comillas simles o comillas dobles.

Este tema será ya más denso que el resto, ¡al lío! 💪

## Creando un String

Vamos a crear una variable string llamada ```texto``` con el valor "Hola Python".

```Python
texto = 'Hola Python'
```

Como **texto** es un tipo de dato, podemos aplicarle por ejemplo una función básica para comprobar su longitud, en este caso, len().

```Python
texto = 'Hola Python'
print(len(texto))
11
```

Y vemos que nos devuelve 11. ¿Qué signfica este 11? Significa que existen 11 posiciones, entre caracteres, espacios y símbolos, comprendidos desde el principio de la cadena hasta el final.

## Creando un String con multilíneas

Hemos creado un string que sólo tiene 1 línea, que suele ser lo habitual, pero puede darte el caso de necesitar más de una línea para, por ejemplo, explicar el funcionamiento de un campo.

Las multilíneas se crean con la triple comilla, ya sea simple o doble (''' o """) ¿te suena de los [comentarios](/3%20-%20Comentarios/readme.md)?

```Python
texto_multi = '''En un lugar de la mancha,
de cuyo nombre no quiero acordarme,
vivía un joven hidalgo...'''

print(texto_multi)

'''
Salida ->
En un lugar de la mancha,
de cuyo nombre no quiero acordarme,
vivía un joven hidalgo...
''' 
```

## Concatenar

Una variable puede ser la "suma" de varias variables, me explico, podemos concatener varios textos en uno.

```Python
name = 'Marco'
last_name = 'Polo'
name_complete = name + ' ' + last_name
print(name_complete)
# Salida -> Marco Polo
```

## Secuencias de escape

Podemos aplicar también a nuestro texto saltos de línea, para ello en el texto hay que usar la barra (\) y luego la n.

```Python
texto = 'En un lugar de la mancha\nde cuyo nombre no quiero...'
print(texto)
'''Salida ->
En un lugar de la mancha
de cuyo nombre no quiero...
'''
```

También podemos añadir tabulación, y sus espacios, con /t + la cantidad, tales como /t3, /t4, etc.

Esto nos puede venir genial cuando queremos imprimir por salida estándar por ejemplo una tabla de resultados.

```Python
print('Table of Results\n')
print('Id\tType\tPoints')
print('1\tA\t10')
print('2\tB\t15')
print('3\tC\t7')
```

Si queremos poder mostrar la \ como un símbolo en la salida estándar, lo que tenemos que hacer es aplicarlo doblmente (\\)

Y si queremos poder mostrar las comillas en el texto, también con la barra y la comilla (\")

## Formatear el texto

Hay varios caminos para formatear el texto en su salida, no los veremos todos, pero sí los más importantes.

El operador % se usa para formatear una tupla, y juntos formar un String. Pero necesita que se le indique antes qué tipo de datos vas a añadir:

* %s -> String
* %d -> Integer
* %f -> Decimal
* %.numero de dígitos + f -> Decimal con cantidad decimal a mostrar.

```Python
name = 'davibern'
age = 333
output = 'Hi there, I am %s and I am %d years old' %(name, age)
print(output)
```

Si te fijas, hemos creado 3 variables, dos contienen datos y la última la concatenación de ambas. Además, esta última, usa el operador % para concatenar dos datos diferentes, un String y un Integer.

Es tan potente, que podemos incluso concatener ya una colección de datos ya creada.

```Python
books_reads = ['The Lord of the Rings', 'The Witcher', 'Game of Thrones']
output = 'I have read the following books' %(books_reads)
print(output)
```

Pero esta forma de **formatear** está en desuso, actualmente para las versiones 3.X, la que se está usando es la *String Interpolation*, o comúnmente llamada *f-String*.

> Se recomienda usar f-String por su facilidad de uso

Para crear una f-String en una salida incluimos una f, seguida de las comillas, y luego del texto. 

Aquellas variables que vayamos a incluir se escriben con llaves {} y dentro el nombre de la variable.

```Python
name = 'Cristóbal Colón'
discover = 'The New World: The Americas'
print(f'{name} discovered {discover}, long time ago')
```

## Las cadenas de texto son secuencia de caracteres

En Python, como en cualquier otro lenguaje, el String se considera un tipo primitivo, porque representa el texto en su forma más simple.

Pero si escarbamos un poquito, una cadena de texto no es más que la concatenación de letras. Y estas letras se llaman carácter, que en inglés se representa como *char*.

El char es el tipo más básico de texto porque sólo representa una unidad de texto, como por ejemplo 'a', o 'A'.

Tenemos además una tabla con la representación del texto y su valor en bytes. ¿Te suena [ASCII](https://es.wikipedia.org/wiki/ASCII)? Seguro que sí 😉

Y podemos probar lo que decimos desempaquetando una cadena de texto.

```Python
# Cadena de texto
texto = 'hola'
# Desempaquetamos texto guardando cada posición en una variable
a, b, c, d = texto
print(a) # Imprime h
print(b) # Imprime o
print(c) # Imprime l
print(d) # Imprime a
```

## Accediendo a la posición de un carácter

En programación, por lo general, la primera posición de un vector empieza siempre en 0. Hay algunas excepciones, como [R](https://www.r-project.org/), en el que empiezan en 1. Pero no es lo habitual.

Si volvemos a nuestra variable anterior y escbribimos:

```Python
texto = 'hola'
print(texto[0]) # -> 'h'
print(texto[1]) # -> 'o'
print(texto[2]) # -> 'l'
print(texto[3]) # -> 'a'
```

Vemos como estamos accediendo, empezando por 0, a la posiciónd de cada carácter.

¿Y si queremos acceder la última posición?

Te dejo a continuación dos métodos.

<u>Contar y luego acceder</u>

Si no sabemos la longitud de una cadena de texto, lo mejor es calcularle su longitud.

Luego, al total se le resta 1, porque las cadenas de texto internamente siempre se guardan con un espacio a su final.

```Python
planet = 'Earth'
planet_length = len(planet)
print(planet[planet_length - 1]) # Devuelve 'h'
```

<u>Usar el símbolo negativo</u>

Si queremos acceder de forma mucho más fácil usamos el símbolo negativo para acceder a la última posición.

```Python
planet = 'Earth'
print(planet[-1]) # Devuelve 'h'
```

Si quisiéramos acceder a la penúltima, sería un -2, y así sucesivamente.

Lo que antes nos ha ocupado 3 líneas, aunque se puede reducir, con esta forma de Python lo hemos hecho en una línea.

## Trocear texto

Esto se usa muchísimo en cálculo de datos científicos, analítica de datos y estadística.

```Python
animal = 'cocodrile'
primeras_tres_letras = animal[0:3] # Empieza en la cero y acaba en la tercera posición.
ultimas_tres_letras = animal[5:8] # Empieza en la cinco y termina en la ocho.
```

## Revertir texto

También podemos hacer el efecto espejo de un texto.

```Python
text = 'Hello, world'
print(text[::-1]) # dlrow ,olleH
```

## Funciones de la clase String

String, como recordatorio, es una clase que maneja la concatenación de caracteres.

Y como toda clase que se precie, tiene sus atributos y métodos. Más adelante veremos qué es una clase, pero por ahora, tienes que saber que String tiene una serie de "herramientas" para poder jugar con el texto.

### capitalize()

Convierte la primera letra de una frase en mayúscula.

```Python
text = 'hello, world'
print(text.capitalize())) # Hello, world.
```

### count()

Cuenta el número de ocurrencias de una cadena de texto. Es decir, le indicas el carácter a buscar y devuelve las veces que existen. 

Se puede incluso focalizar en una parte del texto.

```Python
text = 'I wish to found an adventure...'
print(text.count('o')) # Devuelve 2
```

### endswith()

Comprueba si la parte final de un string coincide con lo que indiques en sus argumentos.

```Python
despedida = 'hasta luego'
print(despedida.endswith('ego')) # Devuelve True
print(despedida.endswith('ar')) # Devuelve False
```

### expandtabs()

Reemplaza los tabuladores por espacios. El espaciado de la tabulación está por defecto en 8.

```Python
texto_tabulado = 'What\tis\tthis'
print(challenge.texto_tabulado())   # 'What  is    this'
print(challenge.texto_tabulado(10)) # 'What    is      this'
```

### find()

Devuelve la posición de la primera ocurrencia de un substring. Si no encuentra concurrencia, devuelve -1.

```Python
texto = 'Encuentrame'
print(texto.find('c')) # Devuelve 2
```

### rfind()

Devuelve la posición de la última concurrencia de un substring. Si no encuentra concurrencia, devuelve -1.

```Python
texto = 'Encuentrame'
print(texto.rfind('m')) # Devuelve 9
```

### format()

Da formato a un string con una salida más amena.

```Python
name = 'davibern'
job = 'data scientist'
output = 'I am {}, and i work as {}'.format(name, job)
print(output)
```

### index()

Devuelve el índice mayor de una cadena. Adicionalmente si se le añaden números en sus argumentos, se está especificando el inicio y final.

```Python
text = 'learning Python'
index = 'ing'
print(text.index(index)) # Devuelve 5
```

### isalnum()

Comprueba un caracter alfanumérico.

```Python
text = 'Python'
print(text.isalnum()) # Devuelve True

text_2 = 'Hello Python'
print(text.isalnum()) # Devuelve False, porque el espacio no se considera alfanumérico
```

### isalpha()

Comprueba si en una cadena todos los elementos son caracteres del alfabeto (a-z o A-Z).

```Python
text = 'Python'
print(text.isalpha()) # Devuelve True

text_2 = '22'
print(text.isalpha()) # Devuelve False
```

### isdecimal()

Comprueba si un valor es número (0-9).

```Python
num = '123'
print(num.isdecimal()) # Devuelve True

num_2 = '22 1'
print(num_2.isdecimal()) # Devuelve False
```

### isdigit()

Comprueba si todos los caracteres de un string son números (0-9) y contiene algún otro carácter numérico unicode.

```Python
num = '123'
print(num.isdecimal()) # Devuelve True

num_2 = '\u00B2'
print(num_2.isdecimal()) # Devuelve True
```

### isnumeric()

Igual que isdigit(), pero también admite números relativos, como el ½.

```Python
num = '123'
print(num.isdecimal()) # Devuelve True

num_2 = '\u00BD'
print(num_2.isdecimal()) # Devuelve True
```

### isidentifier()

Comprueba si existe algún valor identificativo válido. Es decir, comprueba si una variable está bien construida en su nombre.

```Python
text = '4Gamers'
print(text.isidentifier()) # Devuelve False, porque empieza por un número

text = 'name_complete'
print(text.isidentifier()) # Devuelve True
```

### islower()

Comprueba si todos los caracteres de un string son minúsculas.

```Python
text = 'HOLA PYTHON'
print(text.islower()) # Devuelve False

text = 'hola pyhton'
print(text.islower()) # Devuelve True
```

### isupper()

Comprueba si todos los caracteres de un string son mayúsculas.

```Python
text = 'HOLA PYTHON'
print(text.isupper()) # Devuelve True

text = 'hola pyhton'
print(text.isupper()) # Devuelve False
```

### join()

Devuelve una concatenación de strings.

```Python
sports = ['Football', 'Formula 1', 'Basketball']
output = 'I like so much '.join(sports)
print(ouput) # Devuelve I like so much Football Formula 1 Basketball'
```

### strip()

Elimina todos los caracteres que se indiquen como argumento, empezando en la posición 0 hasta el final de la cadena.

```Python
text = 'learning Python'
print(text.strip('rng')) # Devuelve -> leaig Pytho
```

### split()

Divide una cadena de texto por según el separador que se indique en su argumento.

```Python
text = 'I am learning Python'
print(text.split()) # Devuelve ['I', 'am', 'learning', 'Python']
```

### replace()

Reemplaza un caracter en una cadena de texto por el indicado. Necesita la cadena a reemplazar y el reemplazo.

```Python
text = 'I love Python'
print(text.replace('Python', 'Java')) # Devuelve -> 'I love Java'
```

### title()

Devuelve una cadena de texto con la primera letra de una palabra en mayúscula.

```Python
text 'hello world'
print(text.title()) # Devuelve -> 'Hello World'
```

### swapcase()

Convierte todas las mayúculas a minúsculas y viceversa.

```Python
text = 'WhaT iS This'
print(text.swapcase()) # Devuelve -> 'wHAt Is tHIS'
```

### startswith()

Comprueba si una cadena de texto empieza por los caracteres especificados.

```Python
text = 'four fantastics'
print(text.startswith('fou')) # Devuelve True
```

***

😍😲 Si has llegado hasta aquí leyendo todo, tengo que darte mi más sincera enhorabuena, porque no todo el mundo tiene capacidad ni fuerza de voluntad para aguantar tremenda chapa. 😲😍

<span style="color:orange">**¡Eres increíble!**</span>