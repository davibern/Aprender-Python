# Archivos JSON

[JSON](https://en.wikipedia.org/wiki/JSON) es un lenguaje de marcas que nos permite estructurar la información de una forma muy sencilla y legible. Surge de una notación de objetos para __JavasScript__, pero es independiente de este lenguaje.

Ha tenido tanto auge este tipo de fichero que está sustituyendo por ejemplo los __XML__, que son mucho más complejos y pesados. Por ejemplo, en la API de __Twitter__ se usa __JSON__ en lugar de __XML__.

Y en __Python__ tenemos por supuesto un módulo para poder trabajar con este tipo de ficheros.

Lo primero que tenemos que hacer es importar el módulo __json__.

```Python
import json
```

Vamos a suponer que tenemos un fichero __datos.json__ con el siguiente contenido:

```Python
datos_json = {"nombre": "Juan", "apellidos": "Pérez", "edad": 25}
```

Con el método ```load()``` leemos el fichero y  lo convertimos en un diccionario de __Python__, que es más fácil de trabajar que el __JSON__. 

```Python
with open("datos.json") as fichero:
    datos = json.load(datos_json)
    type(datos)
    # <class 'dict'>
```

Ahora si accedo a un elemento del diccionario, tendré de vuelta su valor correspondiente accediendo al diccionario.

```Python
datos["edad"] # 25
```