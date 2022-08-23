# Condicionales

Una vez que hemos visto todo lo relacionado con los [tipos de datos](/04_Tipos_de_datos/readme.md), las [funciones básicas](/06_Biblioteca_Est%C3%A1ndar/readme.md), las [variables](/07_Variables/readme.md), etc., es hora de empezar a programar líneas de código más interesante.

Y una de ellas y, puede ser, de las más importantes, son los condicionales.

Aunque antes de empezar, un aviso importante:

> En Python un script se ejecutará predeterminadamente de arriba a abajo. Y, sólo sí, la lógica de proceso requiere, se puede alterar este orden.

Ahora bien, ¿cómo podemos alterar el orden de ejecución?

**Con las ESTRUCTURAS DE CONTROL**.

Existen dos bloques de control:

- Bloque condicional (```if```): Un bloque de una o varias sentencias se ejecutará sólo si la expresión que contenga la condición es verdadera.
- Bloque repetitivo (```for```, ```while```): Un bloque de una o varias sentencias, se ejecutará repetidamente, si la expresión que contenga la condición es verdadera.

Los bloques repetitivos los veremos más adelante, ahora veremos las condicionales.

## ¿Qué es una condición?

Una condición es una pregunta, sin interrogantes, en las cuales esperas una respuesta:

- Que ésta sea verdadera.
- Que ésta sea falsa.
- O que no se cumpla ninguna de las dos.

Por ejemplo, imagina que tienes una variable que representa el estado de una puerta. Así que pensemos en una puerta, la del baño, o tu dormitorio. La puerta puede tener dos estados, cerrada o abierta.

Así que nos vamos a crear una variable que se llama ```esta_abierta```. Por defecto la puerta siempre estará cerrada, así que podríamos declararla tal que así:

```Python
esta_abierta = False # La puerta está cerrada
```

¿Qué ocurre si quiero entrar en la habitación? Que antes tengo que preguntar cómo está la puerta:

```
¿La puerta está abierta?
Si es no: tendré que abrirla.
Si es sí: podré pasar.
```

Y ahí terminaría mi algoritmo.

Lo importante es captar cómo funciona un algoritmo, es decir, tenemos que preguntar por algo, ese algo, se llama *expresión*.

Por lo tanto, la condición evalúa una expresión en su interior, si se cumple puede hacer "algo", y si no se cumple también.

¿Cuántas condiciones tenemos?

- Condición Si.
- Condición Si no también.
- Condición Si no.

Ahora veremos cómo se construye en Python.

## Condición Si (If)

En inglés, la condición "si..." se escribe como  ```if```. Y se ejecutará su bloque sólo si la condición es ```verdadera```.

```Python
if condition:
    # Hacer lo que sea
```

```Python
valor_control = 5
if valor_control > 5:
    print('WARNING: Hemos superado el valor máximo estimado.')
```

Como puedes ver, tenemos una variable llamada ```valor_control``` que vale 5, si por lo que sea este valor supera los 5, mostramos por pantalla una aviso.

Si no lo supera, no avisaremos de nada. Este aviso, en un modelo de negocio real, podría ser un aviso, un correo electrónico, una parada del sistema, un reinicio, una línea más en los logs de estados, etc., etc., etc.

## Condición Si no (If Else)

Podemos evaluar no sólo lo que ocurre en el bloque verdadero, sino también, lo contrario, es decir, si es ```Falso```.

Es decir, evaluamos una expresión, si es verdadero haz algo, pero si no fuese verdadero, ¿podemos hacer algo también? Sí, con el bloque ```else```, que evalúa el ```Falso```.

```Python
if condition:
    # Hacer lo que sea
else:
    # Hacer lo otro
```

```Python
valor_control = 5
if valor_control > 5:
    print('WARNING: Hemos superado el valor máximo estimado.')
else:
    print('AVISO: todo bajo control.')
```

## Condición si no también (If Elif Else)

¿Y si queremos evaluar varias condiciones? Que no sólo tengamos una verdadera y una falsa, sino, que podamos tener varias que puedan ser verdaderas. Para ello tenemos ```elif```.

```Python
if condition:
    # Hacer lo que sea
elif condition:
    # Hacer o que sea
else:
    # Hacer lo otro
```

```Python
valor_control = 5
if valor_control > 5:
    print('WARNING: Hemos superado el valor máximo estimado.')
elif valor_control < 5:
    print('WARNING: Hemos bajado el valor máximo estimado.')
else:
    print('AVISO: todo bajo control. El valor sigue estando en 5')
```

## Versión reducida

Podemos reducir la sintaxis del ```if``` del siguiente modo:

```Python
codigo if condicion else codigo
```

Vamos a verlo mejor con un ejemplo práctico.

```Python
valor = 10
print('Hemos alcanzado el valor 10') if a == 10 else print('Por debajo de 10')
```

## Condiciones anidadas

Como todo se puede complicar sobremanera, por supuesto, los condicionales podemos anidarlos, uno tras otro.

```Python
if condition:
    if condition:
        # Algo que hacer
```

Un ejemplo para verlo más claro.

```Python
esta_activado = False
valor = 5

if esta_activado == True:
    if valor > 5:
        print('El valor es superior a 5')
```

Estamos evaluando si ```esta_activado``` es verdadero, ¿cómo? con los dos iguales ```==```.

En Python, al igual que en otros lenguajes de programación, podemos ahorrarnos código en los ```if``` cuando queremos evaluar una condición verdadera, ¿cómo? Ahorrando el ```== True```.

```Python
esta_activado = False
valor = 5

if esta_activado:
    if valor > 5:
        print('El valor es superior a 5')
```

## Condicionales y operaciones de lógica

¿Te acuerdas que hemos visto los [operadores de lógica](/05_Operadores/readme.md)? Si no los tienes claro, te recomiendo que vuelvas y lo repases.

Una condición, puede evaluar más de una expresión, pero, una expresión puede ser la comprobación de varias variables.

Mejor lo vemos con un ejemplo:

```Python
status = 'admin'
level = 0

if status == 'admin' and level == 0:
    # Acceso a portal de administracion
else:
    # Acceso a portal de colaborador
```

😲 Vas por buen camino ¡sigue así!

Vamos ahora con los [ejercicios](/13_Condicionales/ejercicios_condicionales.md) de rigor.

***

⬅️ [Clase anterior](/12_Diccionarios/readme.md) | [Clase siguiente]() ➡️