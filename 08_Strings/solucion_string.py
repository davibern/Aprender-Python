"""
Crea una variable llamada mi_texto con el siguiente valor
'Estoy aprendiendo Python, ¡y me está encantando'.
"""
mi_texto = 'Estoy aprendiendo Python, ¡y me está encantando!'

# Calcula la longitud de ```mi_texto``` y la muestras por pantalla.
print(len(mi_texto))

# Realiza un print de ```mi_texto``` y lo pasas todo a mayúsculas.
print(mi_texto.upper())

# Realiza un print de ```mi_texto``` y cambia el primer carácter en mayúscula.
print(mi_texto.title())

# Realiza un print de ```mi_texto``` y revierte el texto.
print(mi_texto[::-1])

# Muestra usando print, de ```mi_texto```, sólo las posiciones 2, 3, 7, 33
print(f'{mi_texto[2]}, {mi_texto[3]}, {mi_texto[7]}, {mi_texto[33]}')

# Trocea ```mi_texto``` desde la posición 10 a la 20 y lo muestras.
print(mi_texto[10:20])

# Comprueba ```mi_texto``` usando los métodos isalnum, isalpha y isdigit.
print(mi_texto.isalnum())
print(mi_texto.isalpha())
print(mi_texto.isdigit())

"""
Crea una variable lista_mi_texto y que se guarde el resultado
de usar el método split sobre ```mi_texto```.
"""
lista_mi_texto = mi_texto.split()
print(lista_mi_texto)
