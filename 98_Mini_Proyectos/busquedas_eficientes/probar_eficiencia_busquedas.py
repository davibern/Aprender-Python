import time
import random


from busqueda_binaria import busqueda_binaria
from busqueda_inocente import busqueda_inocente

size = 10000
lista_inicial = set()

while len(lista_inicial) < size:
    lista_inicial.add(random.randint(-3 * size, 3 * size))
    
lista = sorted(list(lista_inicial))

# Medimos el tiempo que toma conseguir el elemento de la lista con el algormito inocente
inicio = time.time()
for i in lista:
    busqueda_inocente(lista, i)
fin = time.time()
print(f'Tiempo de búsqueda inocente en {fin - inicio} segundos')

# Medimos el tiempo que toma conseguir el elemento de la lista con el algormito binario
inicio = time.time()
for i in lista:
    busqueda_binaria(lista, i)
fin = time.time()
print(f'Tiempo de búsqueda binaria en {fin - inicio} segundos')