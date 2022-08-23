'''
Crea una variable que se llame maximo_permitido. La inicializas a 20.
Crea un bloque if-else y comprueba si maximo_permitido es mayor o igual a 20.
Si es verdadero, imprime por pantalla el valor es igual o mayor a 20,
y si no imprime por pantalla el valor es menor a 20.
'''

maximo_permitido = 20

if maximo_permitido >= 20:
    print('el valor es igual o mayor a 20')
else:
    print('el valor es menor a 20')
    
'''
Crea una variable llamada temperatura y la inicializas a 21. Si temperatura es mayor de 0 y menor o igual de 10 imprime Hace mucho frío si está entre 11 y 20
imprime Hace algo de frío si está entre 21 y 30 imprime Hay temperatura cálida si está entre 31 y 40 imprime
Hace calor y si está por encima de 40 imprime Vamos a morir!!!
'''
temperatura = 21

if temperatura > 0 or temperatura <= 10:
    print('Hace mucho frío')
elif temperatura > 11 or temperatura <= 20:
    print('Hace algo de frío')
elif temperatura > 20 or temperatura <= 30:
    print('Hay temperatura cálida')
elif temperatura > 30 or temperatura <= 40:
    print('Hace calor')
else:
    print('Vamos a morir!!!')
    
'''
Crea una variable llamada edad y aplícale un input para solicitarle la edad al usuario. Si el usuario tiene 18 años o más,
indica que puede sacarse el carnet de condudir, si no, calcula los años que faltan para poder hacerlo.
Tendrás que validar si la edad introducida por el usuario es un número 😜, y además convertir el dato a número...
'''
edad = input('¿Cuántos años tienes? ')
if edad.isdigit():
   if int(edad) >= 18:
       print('Puedes sacar el carnet de conducir.')
   else:
       print(f'Aún te faltan {18-int(edad)} años.')
else:
    print('No has introducido un número.')
    
'''
Tienes la siguiente lista de colores ['blanco', 'rojo', 'azul']. Vas a añadir el color azul, pero antes tienes que comprobar si existe en la lista.
Si no existe, lo añadies, y si existe, indica con un print que ya se encuentra.
'''
colores = ['blanco', 'rojo', 'azul']
if 'amarillo' not in colores:
    colores.append('amarillo')
    print('Color amarillo añadido.')
else:
    print('El color amarillo ya se encuentra en la lista.')
