# Entrada y salida estándar

## Entrada

Por terminal en Phyton podemos solicitarle datos al usuario (entrada estándar) y mostrarlo por pantalla (salida).

La función que hay que usar para solicitar al usuario algún dato es ```input()```. Esto leerá los datos introducidos por el teclado.

Además, ```input()``` **siempre devolverá el resultado en una cadena de caracteres (str)**.

Por ejemplo:

```Python
num1 = input("Dame un número:")
type(num1)
# str
```

En este caso, indicar también que ```input()``` tiene como argumento un _string_ que nos servirá para añadir accesibilidad al programa, es decir, especificarle al usuario qué es lo que esperamos que nos de.

Evidentemente, si lo que queremos hacer es operaciones con los datos que nos de el usuario, tendremos que convertirlo a entero.

```Python
int(num1)
type(num1)
# int
```

Y si queremos convertir caracteres no numéricos a número, pues saltará una [excepción](/19_Excepciones/readme.md) para indicarnos que no es posible hacer lo que pretendemos.

```Python
num2 = input("Ingresa un número:")
# el usuario ingresa hola
int(num2)
# ValueError: invalid literal for int()...
```

## Salida

Las salidas, como ya hemos visto, se hace con la función ```print()```. Podemos añadir varios valores separados por coma, y Python automáticamente añadirá espacios entre ellos.

> Ya hemos visto algo de esta función en la [biblioteca estándar](/06_Biblioteca_Estándar/readme.md)

```Python
print(1, 2, 3)
# 1 2 3
```

Pero podemos indicarle en el argumento ```sep``` qué separador usar, por ejemplo:

```Python
print(1, 2, 3, sep="-")
# 1-2-3
```

Pero incluso podemos indicarle que cuando llegue al final, añada otro carácter, esto lo haremos con ```end```.

```Python
print(1, 2, 3, sep="-", end=".")
# 1-2-3.
```

También podemos concatener con el operador ```+```, y aquí print si no lo separamos por coma, no los separará automáticamente.

```Python
print("hola"+"qué tal")
# holaque tal
```

Para __formatear__ las salidas ya hemos visto buenas partes de sus posibilidades en el [capítulo de strings](/08_Strings/readme.md).

***

Hemos visto como con unas pocas líneas podemos hacer que el usuario interactúe con la aplicación y mostrarles los resultados.

Ahora toca el turno de [Practicar](/22_Entrada_Salida_Estandar/ejercicios_salida_estandar.md). También lo tienes directamente en un cuaderno de [Jupyter](/22_Entrada_Salida_Estandar/ejercicios_salida_estandar.ipynb) si lo prefieres.

Recuerda no ver las soluciones antes salvo que estés muy atascado.

***

⬅️ [Clase anterior](/21_Archivos/readme.md) | [Clase siguiente](/98_Mini_Proyectos/) ➡️