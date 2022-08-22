'''
Crea un diccionario llamado persona, y añadele las siguientes claves con sus valores:
    * first_name: tu nombre
    * last_name: tu apellido
    * edad: tu edad
    * ciudad: tu ciudad
    * país: tu pais
'''
persona = {
    'first_name' : 'davibern',
    'last_name' : 'developer',
    'years': 145,
    'city' : 'Seville',
    'country' : 'Spain',
    'hobbies' : ['videogames', 'reading', 'develop']
}

# Imprime por pantalla el diccionario.
print(persona)

# Calcula la longitud del diccionario y lo imprimes por pantalla.
print(len(persona))

# Muestra por pantalla la ciudad de la persona.
print(persona['country'])

# Añade un nuevo elemento llamado job y su valor.
persona['job'] = 'developer'

# Cambia la ciudad de persona por el valor 'in your dreams'.
persona['city'] = 'In your dreams'

# Imprime por pantalla el diccionario.
print(persona)

# Comprueba si el elemento years está en el diccionario e imprímelo por pantalla.
print('years' in persona)

# Elimina el último elemento del dicionario e imprime el diccionario por pantalla.
persona.popitem()
print(persona)