# Clases y objetos

Python es un lenguaje de programación orientado a objetos. Todo en Python es un objeto, con sus propiedades y sus métodos.

Cuando hemos vistos los [tipos de datos](/04_Tipos_de_datos/readme.md), hemos estado viendo clases y objetos. Puesto que cada tipo contiene sus propios métodos y sus atributos.

Para construir un objeto, antes hay que definir su clase. Y una clase es una representación abstracta de un objeto en el mundo real. Piensa en una clase como la receta para construir ese objeto real.

Otra de las particularidades de las clases y objetos, es que éstos hay que instanciarlos, porque una cosa es crearlos, pero otra invocarlos. Para instanciar una clase se necesita un constructor, éste puede recibir argumentos (como las [funciones](/15_Funciones/readme.md)) o no recibirlos.

Luego además, tenemos la herencia y herencia múltiple, que no es otra cosa que la reutilización de código. Es decir, podemos crear una clase que represente a un Animal, y otra clase que represente a un Mamífero. Mamífero heredará las propiedades de Animal.

Vamos a ir viendo poco a este tema.

## Crear una clase

Para crear una clase usamos la palabra reservada ```class```, seguido del nombre de la clase. La case, por convención, se escribirá siempre con la primera letra en mayúscula.

```Python
class Persona:
    pass
```

Si imprimimos persona, Python nos devolverá lo siguiente:

```Python
<class '__main__.Persona'>
```

## Instanciar una clase

Para instanciar una clase creamos una variable, que será nuestro futuro objeto, que representará a dicha clase.

```Python
class Persona:
    pass

p = Persona()
```

```p``` es un objeto, si imprimimos ```type(p)```, nos encontraremos con lo mismo de antes.

```Python
<class '__main__.Persona'>
```

## Constructor de una clase

El constructor de una clase es un método especial que tiene la clase para instanciar al objeto. De este modo podemos dinamizar dicha instanciación, es decir, podemos crear un tipo de objeto ```Persona```, por ejemplo, indicando en su constructor un argumento, y éste se podrá usar para personalizar los atributos de nuestra clase.

```Python
class Persona:
    
    def __init__(self, name):
        print('Hola', name)

p = Persona('davibern')
```

En este ejemplo, no hay atributos, pero ¿qué son los atributos de clase?

## Atributos de clase

Un atributo de clase es una descripción de nuestro objeto. Para seguir con nuestro ejemplo, ```Persona``` tendrá un nombre, unos apellidos y por ejemplo una edad. Los atributos, por norma general, se declaran antes del constructor, y no dejan de ser variables internas de la clase.

```Python
class Persona:
    
    # Atributos de clase
    first_name = ""
    last_name = ""
    age = 0
```

Estos atributos, cuando creamos un objeto Persona, podemos darle uso en su constructor, e instanciar un objeto personalizado.

```Python
class Persona:
    
    # Atributos de clase
    first_name = ""
    last_name = ""
    age = 0
    
    # Constructor de clase
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# Instanciación de clase usando el constructor personalizado
p = Persona('davibern', 'dev', 300)
```

## Métodos de clase

Un metodo de clase se llama a una función que esté dentro de una clase. Los métodos de una clase nos sirven para que un objeto pueda comunicarse con otros objetos, y que éstos puedan o recibir información, enviar información o poder cambiar su comportamiento.

Te dejo el ejemplo anterior, pero con un método que nos servirá para poder mostrar por salida estándar los datos de nuestra clase.

```Python
class Persona:
    
    # Atributos de clase
    first_name = ""
    last_name = ""
    age = 0
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __str__(self):
        print(f'Mi nombre es {self.first_name} y mi edad es de {self.age}')

p = Persona('davibern', 'dev', 300)
p.__str__()
```

## Herencia

La herencia nos permite reutilizar toda una clase en la nueva que la implemente. De nuevo nos encontramos con fórmulas para poder reutilizar nuestro código sin necesidad de reescribirlo.

Por ejemplo, si tenemos una clase que se llama ```Persona```, que contiene una serie de atributos y métodos, podemos crear una clase nueva que se llame ```Profesor``` que herede de ```Persona```.

```Python
class Persona:
    pass

class Profesor(Persona):
    pass
```

Veámoslo más claro con este ejemplo, donde tenemos a ```Persona``` y a ```Profesor```. Profesor hereda de Persona, lo que significa que tendrá acceso a su contructor y al método para mostrar los datos por pantalla, y si te fijas, Profesor no tiene nada declarado en su interior.

```Python
class Persona:
    
    # Atributos de clase
    first_name = ""
    last_name = ""
    age = 0
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __str__(self):
        print(f'Mi nombre es {self.first_name} y mi edad es de {self.age}')
        
class Profesor(Persona):
    pass

p = Profesor('davibern', 'dev', 300)
p.__str__()
```

Pero, ¿y si necesito que por ejemplo, el método ```__str__``` de Profesor difiera del original? Para eso tenemos la ```sobrecarga de métodos```.

```Python
class Persona:
    
    # Atributos de clase
    first_name = ""
    last_name = ""
    age = 0
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __str__(self):
        print(f'Mi nombre es {self.first_name} y mi edad es de {self.age}')
        
class Profesor(Persona):
    
    def __str__(self):
        print(f'Mi nombre es {self.first_name} y mi edad es de {self.age} y soy profesor.')

p = Profesor('davibern', 'dev', 300)
p.__str__()
```

🧑🏻‍💻 ¡Vas increíblemente bien! Poco a poco y con firmeza, vamos avanzando con Python.

Ahora vamos con unos [ejercicios](/17_Clases/ejercicios_clases.md) básicos.

***

⬅️ [Clase anterior](/16_Modulos/readme.md) | [Clase siguiente](/18_Lista_Compacta/readme.md) ➡️