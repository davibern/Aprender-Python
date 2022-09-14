# Crea una función con dos argumentos que se llame multiplicación y que devuelva el producto de ambos.
from audioop import mul
from cmath import pi
from statistics import multimode
import random

def mulitplicacion(a, b):
    return a * b
print(mulitplicacion(20, 3))

# Crea una función que se llame resto y que calcule el resto de dos números (éstos deben pasarse como parámetros).
def resto(a, b):
    return a % b
print(resto(10, 3))

# Crea una función que se llame area_triangulo, la fórmula es π x r x r.
def area_triangulo(a, b):
    return pi * a * b
print(area_triangulo(3, 4))

# Crea una función que se llame mi_lista y que calcule el número de elementos que tiene y que los muestre por pantalla.
# La lista tendrá los siguientes elementos [1, 3, 4, 5, 6, 7, 8, 9, 10].
lista = [1, 3, 4, 5, 6, 7, 8, 9, 10]
def mi_lista(lista):
    for i in lista:
        print(i)
    print(f'La lista continene {len(lista)} elementos')

mi_lista(lista)

# Crea una función que se llame suma_total y que tenga parámetros arbitrarios, y que devuelva la suma de todos los elementos.
# Pásale como argumento los valores: 3, 5, 6, 888, 333, 22, 1.
def suma_total(*args):
    total = 0
    for i in args:
        total += i
    return total

print(suma_total(3, 5, 6, 888, 333, 22, 1))

'''
Declara una función que se llame caja. Tendrá dos argumentos: entrada, valor. Y funcionará de la siguiente manera:
    * entrada tendrá como valores "entrada" o "salida".
    * valor tendrá como valor un número.
    * dentro de la función tendremos una variable llamada total inicializada a 1000.
    * si el argumento entrada es entrada se le sumará a total lo indicado en valor.
    * si el argumento entrada es salida se le restará al total lo indicado en valor.
    * la función devolverá con un return el valor de total.
'''
def caja(entrada, valor):
    total = 1000
    if entrada == 'entrada':
        total += valor
    elif entrada == 'salida':
        total -= valor
    else:
        pass
    return total

print(caja('entrada', 100))
print(caja('salida', 100))

# Crea una función que se llama es_par_impar(), recibirá como argumento un número, y devolverá par si es par o impar si es impar.
def es_par_impar(numero):
    if numero % 2 == 0:
        return 'Es par'
    else:
        return 'Es impar'
    
print(es_par_impar(4))
print(es_par_impar(5))

'''Crea una función que servirá para adivinar un número aleatorio. Este número aleatorio estará comprendido entre 1 y un máximo que se
indicará como argumento de nuestra función. El usuario tendrá que ir añadiendo números hasta dar con el aleatorio, para ello habrá que ayudarle
e indicarle si se está acercando o alejando del número a encontrar.

Tendrás que importar el módulo random.'''
def adivinar_numero_aleatorio(maximo):

   aleatorio = random.randint(1, maximo)
   
   numero_a_adivinar = 0
   
   while numero_a_adivinar != aleatorio:
       numero_a_adivinar = int(input(f'Adivina un número comprendido entre 1 y {maximo}: '))
       
       if numero_a_adivinar < aleatorio:
           print('Vaya tu número está por debajo! Inténtalo de nuevo :)')
       elif numero_a_adivinar > aleatorio:
           print('Vaya tu número está por encima! Inténtalo de nuevo :)')
           
   print(f'¡Enhorabuena! Has adivinado el número {aleatorio} ¡Felicidades!')
    
adivinar_numero_aleatorio(10)