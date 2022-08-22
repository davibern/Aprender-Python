# Set

Como ya habrás visto en la [clase de tipos de datos](/04_Tipos_de_datos/readme.md), existen varios tipos de colecciones, este recordatorio lo voy a incluir en cada una de ellas, porque machacar información es también la mejor manera de que entre en la cabezita 🤯

Pero primero, ¿qué es Set?
 
> Es una colección de datos desordenada, pero indexada, que no permite modificaciones y tampoco duplicados.

Es decir, en Python usamos los sets para almacenar elementos únicos, a los que les podemos ejecutar *uniones*, *intersecciones*, *diferencias*, *simetrías*, etc.

Y ahora el resto:

* **Lista**: es una colección de datos ordenada, modificable y que permite duplicados.
* **Tupla**: es una colección de datos ordenada, pero que no permite modificar los datos. Y permite duplicados.
* **Diccionario**: es una colección de datos desordenada, modificable e indexada, que funciona por par clave-valor, y que no permite duplicados.

## Crear un Set

Para crear un set tenemos que crear un objeto de tipo ```set()```.

```Python
st = set()
```

O bien, creandolo con ```{}```.

```Python
st = {}
```

Y como los conjuntos de datos anteriores, puedes crearlo vacío, o con datos.

```Python
new_set = {'red', 'yellow', 'blue'}
```

Recuerda además, que como en las anteriores, para conocer la longitud de un set, se usa ```len()```.

```Python
mi_set = {1, 2, 3, 4, 5}
print(len(mi_set)) # Devuelve 5
```

## Comprobar si un elemento está en un set

Para comprobar si un elemento se encuentra en un set usamos el operador ```in```. Si se encuentra devuelve *True*, sino, es *False*.

```Python
mi_set = {'rojo', 'azul', 'negro'}
print('rojo' in mi_set) # Devuelve True
```

## Añadir elementos al set

Como ya sabes, una colección set no permite modificaciones de sus elementos, pero sí podemos añadir más elementos, siempre y cuando éste no esté en la colección.

Para añadir un elemento se usa el método ```add()```.

```Python
frutas = {'manzana', 'sandía', 'melón', 'fresa'}
frutas.add('plátano')
```

Además, podemos añadir varios elementos de una tacada, así nos ahorramos usar el ```ad()``` varias veces, para ello deberemos usar ```update()```.

```Python
frutas = {'manzana', 'sandía', 'melón', 'fresa'}
frutas.update(['plátano', 'pera', 'melocotón'])
```

¿Te has fijado que para añadir varios de una tacada estamos usando una lista?

## Eliminar elementos del set

Podemos eliminar elementos del set usando ```remove()```. Si el método no encuentra el elemento a mostrar devolverá un error. Es buena práctica controlar el error con un ```if``` para evitar el error.

```Python
frutas = {'manzana', 'sandía', 'melón', 'fresa'}
frutas.remove('sandía')
```

Podemos evitar el error con el método ```discard()```, pero si no encuentra el elemento no lo sabríamos.

```Python
frutas = {'manzana', 'sandía', 'melón', 'fresa'}
frutas.discard('melocotón') # No sabríamos que este elemento no existe, porque no devuelve el error.
```

Hay otra forma de eliminar un elemento y es usando ```pop()```. Éste elimina un elemento aleatorio, devolviéndolo antes, es decir, que sabríamos que elemento borra.

```Python
frutas = {'manzana', 'sandía', 'melón', 'fresa'}
fruta_eliminada = frutas.pop()
print(fruta_eliminada) # Mostrará por pantalla el elemento eliminado del set
```

## Limpiar un set

Si queremos limpiar una lista usamos el método ```clear()```, esto eliminará todos los elementos, pero no el conjunto.

```Python
frutas = {'manzana', 'sandía', 'melón', 'fresa'}
frutas.clear()
print(len(frutas)) # Mostrará 0
```

## Eliminando un set

Para eliminar un conjunto se usa ```del```. Esto es igual que en resto de conjuntos que hemos visto ya.

```Python
frutas = {'manzana', 'sandía', 'melón', 'fresa'}
del frutas
```

## Convertir un Set en Lista y viceversa

Imagina que tenemos una lista (que sí tiene duplicados) y nos queremos quedar con los elementos únicos de esta. ¿Cómo lo haríamos? Convirtiendo la lista en un conjunto.

```Python
paises = ['Spain', 'France', 'Italy', 'Portugal', 'Germany', 'Spain']
paises_unicos = paises.set(paises)
print(paises_unicos) # Devolverá el conjunto de paises_unicos sin elementos repetidos
# {'Germany', 'Italy', 'France', 'Spain', 'Portugal'} El orden es aleatorio
```
## Uniendo Sets

Podemos unificar dos colecciones con el método ```union()``` o ```update()```.

La diferencia entre ambas es que ```union()``` devuelve un nuevo conjunto y ```update()``` inserta un conjunto en uno existente. Lo vemos mejor con el siguiente ejemplo.

```Python
frutas_1 = {'manzana', 'sandía', 'melón', 'fresa'}
frutas_2 = {'pera', 'melocotón', 'plátano', 'uva'}
frutas_3 = frutas_1.union(frutas_2) # Tenemos que crear una tercera lista que sea la unión de dos existentes.
```

```Python
frutas_1 = {'manzana', 'sandía', 'melón', 'fresa'}
frutas_2 = {'pera', 'melocotón', 'plátano', 'uva'}
frutas_1.update(frutas_2) # Actualizamos el conjunto 1 con el conjunto 2.
```

## Buscando intersecciones entre conjuntos

Imagina que tienes dos conjuntos, ambos, tienen que tener elementos únicos, pero no significa que cada una no pueda tener un elemento que ya tenga otra. ¿Y cómo detectar qué elementos iguales puedan tener ambos conjuntos? Con el método ```intersection()```.

Veámoslo mejor con un ejemplo.

```Python
frutas_1 = {'manzana', 'sandía', 'melón', 'fresa'}
frutas_2 = {'fresa', 'melocotón', 'plátano', 'manzana'}
frutas_1.intersection(frutas_2) # Nos devolverá fresa y manzana, que son los elementos repetidos que tienen ambas
```

## Comprobando la diferencia entre dos conjuntos

A la inversa, podemos conocer qué elementos son diferentes entra ambos conjuntos, para ello usamos ```difference()```.

```Python
frutas_1 = {'manzana', 'sandía', 'melón', 'fresa'}
frutas_2 = {'fresa', 'melocotón', 'plátano', 'manzana'}
frutas_1.difference(frutas_2) # Nos devolverá sandía y melón. No indicará las otras diferencias porque estamos buscándolas sobre el conjunto 1.
```

## Comprobando si es subconjunto o superconjunto

En matemáticas un conjunto puede ser subconjunto de otro conjunto (el segundo sería superconjunto) o viceversa. Es decir, si un conjunto superior tiene elementos que un conjunto menor tiene del primero, el primero sería superconjunto, en cambio, el menor, si tiene elementos del mayor, sería subconjunto.

Para detectar ambas tenemos los siguientes métodos:

* ```issubset()``` -> Indicará si es un subconjunto.
* ```issuperset()``` -> Indicará si es un super conjunto.

Un ejemplo para verlo más claro.

```Python
frutas_1 = {'manzana', 'sandía', 'melón', 'fresa', 'plátano', 'maracuyá'}
frutas_2 = {'fresa', 'melocotón', 'plátano', 'manzana'}
frutas_1.issuperset(frutas_2) # Devuelve True
frutas_2.issubset(frutas_1) # Devuelve True
```

## Buscando diferencias simétricas entre dos conjuntos

Devuelve la diferencia simétrica entre dos conjuntos. Significa que devuelve un conjunto que contiene todos los elementos de ambos conjuntos, excepto los elementos que están presentes en ambos conjuntos, matemáticamente: (A\B) ∪ (B\A).

```Python
paises_1 = {'Spain', 'France', 'Portugal', 'Greece'}
paises_2 = {'Portugal', 'France'}
paises_2.symmetric_difference(paises_1) # Devuelve {'Spain', 'Greece'}
```

## Uniendo dos conjuntos

Si tenemos dos conjuntos que no tengan elementos comunes, éstos serán **disconjuntos*. Se puede verificar si dos conjuntos son conjuntos o disconjuntos usando el método ```isdisjoint()```.

```Python
set_1 = {1, 2, 3, 4, 5}
set_2 = {2, 3}
set_2.isdisjoint(set_1) # Devuelve False porque tienen elementos comunes, el 2 y el 3
```

```Python
set_1 = {0, 2, 4, 6, 8}
set_2 = {1, 3, 5, 7, 9}
set_2.isdisjoint(set_1) # Devuelve True porque no tienen elementos comunes
```

Ahora es cuestión de utilizar tu imaginación, usando ```isdisjoint()``` ya sabes si puedes unificar ambos conjuntos o no 😉

🥳 ¡Sigues en buena racha! Ya hemos terminado los conjuntos ¿No es increíble? **Mi más sincera enhorabuena**.

Ya sabes lo que toca ahora, [practicar](/11_Sets/ejercicios_sets.md). Los ejercicios ya estás viendo que no son muy difíciles, principalmente porque son para mi 😲, pero bueno, poco a poco los iré acomplejando, lo prometo.

***

⬅️ [Clase anterior](/10_Tuplas/readme.md) | [Clase siguiente](/12_Diccionarios/readme.md) ➡️