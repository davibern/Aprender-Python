# Recursividad

Una vez vista las [funciones](/15_Funciones/readme.md) ya podemos ver el siguiente concepto de **funciones recursivas**, pero ¿qué es la recursividad?

> La **recursividad**, o también llamada **recurrencia**, es la forma en la cual se especifica un proceso basado en su propia definición

O dicho de otro modo, que una función pueda volver a llamarse a sí misma, es decir, vamos a resolver un problema inicial, pero este problema, lo dividimos en pequeños pasos resolviendo este problema con la misma función.

Al final de lo que se trata es de ir reduciendo casos, o problemas, hasta llegar a un mínimo en el cual la función no pueda continuar, muy similar a un bucle, ¿verdad? Pero esta vez llamándose la función a si misma una y otra vez.

![Secuencia de Fibonacci](https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Fibonacci_spiral_34.svg/1920px-Fibonacci_spiral_34.svg.png)

Lo vemos mejor con el ejemplo de **Fibonacci**.

```Python
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

En esta función, ¿te das cuenta que si no se cumple la primera condición volvemos a ejecutar la función otra vez?

Como te indicaba, se trata de dividir un problema en casos más pequeños, hasta que lleguemos a un mínimo, y cuál es en este caso, pues que la función retorne o cero, o uno.

## Paso a paso

Vamos a entender mejor cómo se comporta la recursividad ejecutando la función poco a poco:

Si nosotros ejecutamos ```fibonacci(3)```, tendremos lo siguiente

1. Primero evaluamos que sea 0 ó 1, como es falso, saltamos al else.
2. Luego volvemos a ejecutar ```fibonacci(3-1)```, que es 2. Como tenemos que volver a ejecutar la función ésta se queda parada ahí y comprobamos que 2 es 0 ó 1, es falso.
Pues nos quedamos con el 2.
3. Luego volvemos a ejecutar la función, pero como hemos llegado al mínimo, porque ya no podemos reducirla más según el algoritmo, la respuesta es 2.

Intenta hacerlo tu con varias ejecuciones con este [ejemplo](/20_Recursividad/fibonacci.py), a ver qué te sale 😉

También hay otro ejemplo de recursividad en el mini proyecto de [búsqueda binaria](/98_Mini_Proyectos/busquedas_eficientes/busqueda_binaria.py).

Puedes ver más detalles de la recursividad en el vídeo que tienen en [youtube](https://youtu.be/DLikpfc64cA?t=11022) los chicos de [FreeCodeCamp](https://www.freecodecamp.org/learn/).

***

⬅️ [Clase anterior](/19_Excepciones/readme.me) | [Clase siguiente](/21_Archivos/readme.md) ➡️