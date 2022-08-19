# Crea una lista de números de los siguientes valores: 33, 5, 67, 199, 31, 10, 90, 24, 56, 33 y llamala mi_lista.
mi_lista = [33, 5, 67, 199, 31, 10, 90, 24, 56, 33]

# Imprime por pantalla la cantidad de elementos que contiene.
print(len(mi_lista))

# Imprime por pantalla las posiciones 4 y 6.
print(mi_lista[4])
print(mi_lista[6])

# Imprime por pantalla el último valor.
print(mi_lista[-1])

# Imprime por pantalla los valores comprendidos entre la posición 5 y 7.
print(mi_lista[5:7])

# Ordena la lista ascendentemente e imprímela por pantalla.
mi_lista.sort()
print(mi_lista)

# Ordena la lista descendentemente e imprímela por pantalla.
mi_lista.sort(reverse = True)
print(mi_lista)

# Añade el valor 34 al final, e imprime la lista.
mi_lista.append(34)
print(mi_lista)

# Añade el valor 1 en la posición 5, e imprime la lista.
mi_lista.insert(5, 1)
print(mi_lista)

# Calcula la cantidad de valores 33 que existen en la lista y lo imprimes por pantalla.
print(mi_lista.count(33))

# Elimina la posición 4 e imprime la lista por pantalla, e imprímela por pantalla.
mi_lista.pop(4)
print(mi_lista)

# Crea una nueva lista llamada mi_lista_2 con los valores 214, 36, 5, 99.
mi_lista_2 = [214, 36, 5, 99]

# Une ambas listas usando extend() e imprime todos los valores.
mi_lista.extend(mi_lista_2)
print(mi_lista)

# Limpia la lista usando clear().
mi_lista.clear()