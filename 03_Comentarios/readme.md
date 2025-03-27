# Insertar comentarios en Python

Una de las primeras cosas que tenemos que aprender en un lenguaje de programación es cómo se insertan los comentarios.

Son importantes para documentar nuestras líenas de código, aquellas partes que sean importantes dejarlas claras.

Tenemos dos formas:

- Comentar una línea usando el símbolo ```#``` y posteriormente incluir las explicaciones.
- Comentar varias líneas usando ```''' '''```.

## Ejemplos

Te dejo a continuación un ejemplo de cada tipo.

<u>Comentario en una línea</u>

```Python
# Comentario de una línea
# Comentario en otra línea
```

<u>Comentario multilínea</u>

```Python
'''
Este es un comentario multilínea.

Se puede añadir el texto de una forma más cómoda
si necesitamos más espacio
'''
```

¿Y cómo se comentan las funciones? Bueno, aún no hemos llegado a eso, pero como buena práctica se recomienda que el comentario sea multilínea y dentro de la propia función.

```Python
def mi_funcion():
    '''
    Esta función hace bla blab bla
    '''
    return None
```

## Practica los comentarios

Puedes ver cómo queda en el fichero de prácticas llamado [practicar_comentarios.py].

Recuerda que si lo ejecutas en el intérprete de Python, éste no te va a devolver nada, porque son comentarios 😉

[practicar_comentarios.py]: practicar_comentarios.py

***

⬅️ [Clase anterior](/02_Fichero_Python/readme.md) | [Clase siguiente](/04_Tipos_de_datos/readme.md) ➡️