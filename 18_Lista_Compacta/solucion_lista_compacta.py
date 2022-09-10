# Crea una lista compacta de números del 0 al 100.
numeros = [i for i in range(101)]
print(numeros)

# filtra los números negativos
numeros = [1, -1, 3, 5, 877, -223, -4, 45, -556]

negativos = [i for i in numeros if i < 0]
print(negativos)

# filtra los números pares
numeros = [98, 233, 56, 57, 4, 0, -125, 76, -24, 66, 100]

pares = [i for i in numeros if i % 2 == 0]
print(numeros)

# Crea una lista que sume el número de la lista + 5, luego lo multiplice por 5 y lo divida entre 2 al final, en un rango del 0 al 10.
numeros = [(i + 5) * 5 / 2 for i in range(11)]
print(numeros)

# Crea una función lambda que calcule el cuadrado de un número.
cuadrado = lambda x: x ** 2
print(cuadrado(5))