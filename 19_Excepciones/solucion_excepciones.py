# Crea una excepción usando sólo except para el siguiente problema matemático 5-'5'.
try:
    print(5-'5')
except TypeError:
    print('Se ha producido un error')

# Captura el error exacto de la operación anterior para añadirlo al except.
try:
    print(5-'5')
except TypeError:
    print('Se ha producido un error')

# Añade al programa anterior un else por si se realiza la operación.
try:
    print(5-'5')
except TypeError:
    print('Se ha producido un error')
else:
    print('Operación realizada con éxito.')

# Por último añade un bloque final para indicar que se cierra el programa.
try:
    print(5-'5')
except TypeError:
    print('Se ha producido un error')
else:
    print('Operación realizada con éxito.')
finally:
    print('Cierre del programa')
