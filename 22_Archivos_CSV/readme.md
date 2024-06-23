# Archivos CSV

Los ficheros __CSV__ están separados normalmente por coma, aunque puedes encontrar otros separadores como el punto y coma, el tabulador o el espacio. Dependerá de cada órgano o empresa el separador que utilicen.

Este fichero es de texto plano, por lo que sólo vas a encontrar en el un fichero con datos separados por el separador que hemos comentado. No vas a encontrar ninguna fórmula, ni ninguna imagen, ni ningún gráfico, ni ninguna tabla. Por lo tanto, si quieres trabajar con este tipo de ficheros.

En Python tenemos un módulo que nos permite trabajar de forma sencilla con este tipo de ficheros.

El módulo se llama __csv__ y lo vamos a importar de la siguiente forma:

```Python
import csv
```

Con esto ya tendríamos el módulo cargado y listo para trabajar con estos ficheros.

Lo siguiente sería abrir el fichero y lo haremos tal y como hemos aprendido en el capítulo anterior, con el método ```open()```.

```Python
f = open("fichero.csv", "r")
```

Ahora que tenemos el fichero abierto, vamos a leerlo línea a línea. Para ello, vamos a utilizar el método del módulo __csv__ que se llama ```reader()```.

```Python
csv_reader = csv.reader(f, delimiter=',')
```

Si guardásemos el contenido del fichero en una lista, obtendríamos una lista de listas, donde cada lista interna contiene los datos de cada línea del fichero.

```Python
list(csv_reader)

# Deberíamos obtener algo como esto:
[['nombre', 'apellido', 'edad'],
 ['Juan', 'Pérez', '25'],
 ['María', 'Gómez', '30'],
 ['Pedro', 'López', '35']]
```

Igualmente podemos recorrer toda  la lista con un bucle __for__ y obtener cada línea del fichero de la siguiente forma:

```Python
for line in csv_reader:
    print(line)
```

Y no sólo podemos leer un fichero __csv__, sino además, escribir en él.  Para ello, vamos a utilizar el método ```writer()``` para abrirlo en modo escritura, y luego añadimos el contenido con el método ```writerow()```.

Este método recibe como parámetro el fichero abierto en modo escritura y el separador que queremos utilizar. En este caso, vamos a utilizar la coma como separador.

```Python
csv_writer = csv.writer(f, delimiter=',')
csv_writer = csv.writer(['Elena', 'Fernández', '28'])
```

***

⬅️ [Clase anterior](/21_Archivos/readme.md) | [Clase siguiente](/23_Archivos_JSON/readme.md) ➡️