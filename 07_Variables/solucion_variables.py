"""
Crea una variable que se llame edad y que tenga
como calculo restar la fechaactual menos tu fecha de nacimiento.
No tienes porqué calcular la fecha actual con ninguna función.
"""
edad = 2022 - 250

# Crea una variable que se llame nombre de tipo str y lo inicializas
nombre: str = 'davibern'

# Crea una variable que se llame is_open, y que sea falso.
is_open = False

# Crea una lista de valores numéricos y la llamas mi_lista.
mi_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Crea un diccionario que se llame biblioteca, que tenga 3 pares de clave-valor
biblioteca = {
    'num_libros': 100,
    'casillas': 150,
    'prestados': 20
}

# Crea una variable que divida 1000 / 25
divide = 1000 / 25

# Crea una variable que calcule el resto de 125 / 9
resto = 125 % 9

# Crea una variable text, de tipo string, y la inicializas con 'Is magic'.
text: str = 'Is magic'

# Imprime por pantalla el tipo de la variable anterior (usa type(()).
type(text)

# Cambia el valor de la variable anterior por 2022 y vuelve a comprobarlo
text = 2022
type(text)
