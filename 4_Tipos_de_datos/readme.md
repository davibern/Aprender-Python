# Tipos de Datos

En Python hay varios tipos de datos. Estos datos elementales que veremos a continuación se pueden convertir (castear)
a otro tipo según necesidad.

Los datos en Python son de tipo dinámico, es decir, no es necesario declarar el tipo al declararse.

Cuando se declara un variable y se le asigna un valor, Python infiere su tipo automáticamente.

## Tipo NÚMERO (Number)

1. Puede ser de tipo entero (Integer): ...-3, -2, -1, 3, 4, 5...
2. Puede ser de tipo decimal (Float): ...-3.5, -1.5, 1.1, 3.3, 5333.33...
3. Puede ser de tipo complejo (Complex): 1 + 3j, 1 - 4i

## Tipo TEXTO (String)

Es una colección de uno o más caracteres que se declaran con comillas simples o dobles: ..."hola", "mundo"...
>'Bannana'
>
>'Peach'
>
>"Apple"
>
>"Santa Claus"

Tienes más información en la clase específico de [Strings](/8_Strings/readme.md).

## Tipo BOOLEAN (Boolean)

Son tipos que sólo admiten dos valores: verdadero o falso (0, 1)

* True > ¿Está la puerta cerrada? Si lo está es verdadero.
* False > ¿Está la puerta abierta? Si no lo está es falso.

## Tipo LISTA (List)

Una lista es una colección ordenada que permite almacenar diferentes tipos de elementos de datos.

Si quisiéramos compararlos podría ser una matriz en Javascript.

```Python
[0, 1, 2, 3, 4, 5] # Lista que contiene elementos del mismo tipo (integers)
['Sun', 'Venus', 'Mars', 'Jupiter'] # Lista que contiene elementos del mismo tipo (strings)
['Football', 'Rugby', 'Squash', 1, 3, False] # Lista que contiene elementos de diferentes tipos
```

Tienes más información en la clase específico de [Strings](/9_Listas/readme.md).

## Tipo DICCIONARIO (Dictionary)

Un diccionario en Python es una colección desordenada de datos que contiene un par de clave-valor

```Python
{
    'first_name': 'Davibern',
    'website' : 'https://ibpsimracer.com',
    'country': 'Spain',
    'skills' : ['Java', 'Sql', 'R', 'Python', 'Power Apps']
}
```

## Tipo TUPLA (Tuple)
Una tupla es una colección ordenada de diferentes tipos de datos, parecido a la lista pero con la diferencia
que sus datos no se pueden modificar una vez creados.

Son INMUTABLES.

```Python
('Seville', 'Granade', 'Malaga', 'Cadiz', 'Huelva', 'Jaen', 'Cordoba', 'Almeria')
```

## Tip SET (Set)
Un set es una colección de datos similares a una lista o tupla. Y a diferencia de ambas, sus datos no están ordenados.

Como en las matemáticas, set en Python almacena valores únicos.

El orden en Set no es importante, sino mantener una integridad de valores sin duplicados.

```Python
{2, 3, 4, 5}
```

## Comprobrar el tipo de DATO

Para comprobar un tipo de datos se usa la función type() y el valor o variable

```Python
type(3) # Tipo Integer
type(3.222) # Tipo Float
type(True) # Tipo Boolean
type("Good morning, Mr. Marshall") # Tipo String
type(2 + 3j) # Tipo Complex
type([1, 3, 4]) # Tipo List
type({'name' : 'Ironman'}) # Tipo Dict
type((2, 3, 4)) # Tipo Tuple
type({93.3, 33.23, 36.3}) # Tipo Set
```

## Ejercicios

Ahora que hemos visto todos los tipos de datos en Python es hora de aplicarlos en unos cuantos ejercicios muy básicos.

A parte de darle a la teoría, hay que practicar 🤓

Accede a los [ejercicios de datos] con el enlace directo o búscalo en el proyecto de github, no tiene pérdida.

[ejercicios de datos]: ejercicios_tipos_de_datos.md

El ejercicio contendrá además la resolución por si te atascas, pero recomiendo no verlos salvo que no sepas seguir.

La solución está en este otro enlace: [solucion ejercicios de datos].

**Intenta hacerlos sin mirar antes 🕵🏻‍♂️

[solucion ejercicios de datos]: solucion_ejercicios_tipos_de_datos.py

***

⬅️ [Clase anterior](/3_Comentarios/readme.md) | [Clase siguiente](/5_Operadores/readme.md) ➡️