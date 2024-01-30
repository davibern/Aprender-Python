# Crea una tupla con los valores 1, 2, 3, 4, 5. Llámalo tupla_1 y muéstralo.
tupla_1 = (1, 2, 3, 4, 5)
print(tupla_1)

# Crea una tupla con los valores 6, 7, 8, 9, 10. Llámalo tupla_2 y muéstralo.
tupla_2 = (6, 7, 8, 9, 10)
print(tupla_2)

# Crea una tupla con la unión de las dos anteriores y muéstralo.
tupla_3 = tupla_1 + tupla_2
print(tupla_3)

# Calcula la longitud de la tupla 3 y la imprimes por pantalla.
print(len(tupla_3))

# Muetra por pantalla la última posición de la tupla 3.
print(tupla_3[-1])

# Muestra las posiciones de la 5 a la 9 de la tupla 3.
print(tupla_3[5:9])

# Convierte la tupla en una lista y muestra por pantalla su tipo.
lista = list(tupla_3)
print(type(lista))
