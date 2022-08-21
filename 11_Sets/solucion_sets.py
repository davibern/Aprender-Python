# Crea un set llamado set_1 con los siguientes valores 1, 3, 5, 7, 9
set_1 = {1, 3, 5, 7, 9}

# Crea un set llamado set_2 con los siguientes valores 0, 2, 4, 6, 8
set_2 = {0, 2, 4, 6, 8}

# Comprueba si puedes hacer una unión de ambos. Que la comprobación se vea por pantalla.
print(set_2.isdisjoint(set_1))

# Ahora intenta realizar una unión de ambos set, usa union(), al nuevo conjunto llámalo set_3.
set_3 = set_1.union(set_2)

# Imprime por pantalla la longitud de set_3.
print(len(set_3))

# Añade el elemento 11 a set_3
set_3.add(11)

# Comprueba si el elemento 12 está en set_3 y muéstralo en pantalla.
print(12 in set_3)

# Limpia el conjunto
set_3.clear()

# Elimina los conjuntos set_1 y set_2.
del set_1
del set_2