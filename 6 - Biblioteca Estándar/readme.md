# Biblioteca Estándar (Built-in)

Existen muchísimas funciones que ya vienen por defecto en Python listas para usar. Estas funciones se conocen como **Buil-in Functions**.

Su acceso es global y los puedes usar sin necesidad de importarlas a tu proyecto, porque forman parte del núcleo de Python. Es decir, no te hará falta importarlas, no te hará falta configurarlas.

Existen unas 70 funciones del paquete básico, tales como:

- print()
- len()
- type()
- inpu()
- etc...

![Built-in Functions](/99%20-%20Imagenes/built-in_functions.png)

Puedes leer más información en su [documentación oficial](https://docs.python.org/3.9/library/functions.html). Aunque a continuación veremos el ejemplo de uso de algunas de ellas para que te hagas una idea de cómo funcionan.

## Ejemplos de Uso

A continuación dejo algunos ejemplos de funciones preinstaladas y su ejecución en la shell de Python.

### abs()

Devuelve el valor absoluto de un número. Su argumento debe ser un número entero, decimal o un objeto que implemente la propia función. Si por ejemplo indicas un número complejo, se devolverá su magnitud.

![Built-in abs()](/99%20-%20Imagenes/buil-in_abs.png)

Si te fijas, cuando he puesto el valor -100, el valor devuelvo es 100. Recuerda que te devuelve el valor absoluto.

### all()

Comprueba si todos los items de uan lista son verdaderos, si alguno es falso, devuelve falso.

![Built-in all()](/99%20-%20Imagenes/buil-in_all.png)

### dir()

Esta función devolverá la lista de funciones de una biblioteca importada, o dicho de otro modo, es la forma de leer qué métodos contienen un proyecto importado, por ejemplo.

Viene bien para consultar la lista de métodos/funciones de forma rápida por si no te acuerdas del nombre en concreto de una y no quieres acudir a la web para consultarla.

![Built-in dir()](/99%20-%20Imagenes/buil-in_dir.png)

### help()

Invoca la ayuda de la biblioteca estándar. Este función se puede usar con o sin argumentos, es decir, si incluyes una función en concreta como argumento, de devolverá la ayuda de ésta.

![Built-in help()](/99%20-%20Imagenes/buil-in_help.png)

### hex()

Convierte un número entero a su valor exadecimal (y en minúsculas).

![Built-in hex()](/99%20-%20Imagenes/buil-in_hex.png)

### len()

Devuelve la longitud del número de items de un objeto. El argumento debe ser una secuencia, tales como una cadena de texto, bytes, tupla, etc.

![Built-in len()](/99%20-%20Imagenes/buil-in_len.png)

### print()

Imprime por salida estándar (consola Python, intérprete Python, etc.) información del programa. Como argumento se incluye un dato de tipo string, pero se puede incluir también otro tipo de dato que la propia función se encargará de convertirlo.

De hecho se puede incluir variables como argumentos, que veremos más adelante, o icluso operaciones, como puedes ver en el siguiente ejemplo.

![Built-in print()](/99%20-%20Imagenes/buil-in_print.png)

### range()

Devuelve una secuencia de números indicando el inicio o final.

![Built-in range()](/99%20-%20Imagenes/buil-in_range.png)

***

He dejado unos 8 ejemplos de 70 que tiene la biblioteca, pero para hacernos una idea creo que viene bien. Insisto, lo mejor es consultar la documentación oficial, porque además está en español, a diferencia de otros lenguajes, y nos ayudará mucho en nuestras futuras tareas.

## Practicar para Aprender

Como en el resto de temas, os dejo el acceso a los ejercicios para practicar un poco lo que hemos visto, habrá alguna que otra función que no he explicado para que te adentres en la ayuda 😉

[Ejercicios del tema](/6%20-%20Biblioteca%20Est%C3%A1ndar/ejercicios_biblioteca_estandar.md).

***

⬅️ [Clase anterior](/5%20-%20Operadores/readme.md) | [Clase siguiente](/7%20-%20Variables/readme.md) ➡️