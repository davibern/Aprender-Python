# Crea una lista que se llame numbers y que contengan números del 1 al 100.
numbers = range(100)

# Usa un bucle for para imprimir sólo los pares.
for number in numbers:
    if number % 2 == 0:
        print(number)

# Usa el mismo bucle anterior
# pero añade un else para indicar que el impar no se imprime.
for number in numbers:
    if number % 2 == 0:
        print(number)
    else:
        print('El impar no se imprime')

# Crea la tabla de multiplicación del número 5.
multiplicador = 5
for i in range(11):
    print(f'{i} x {multiplicador} = {i * multiplicador}')
    i = i + 1

# Crea una lista que contenga los siguientes valores: Python, Java, C#, PHP...
# E itera sobre la lista para mostrar todos los valores.
lenguajes = ['Pyhon', 'Java', 'C#', 'PHP', 'JavaScript']
for lengauje in lenguajes:
    print(lengauje)

# Crea una variable que se llame i, ésta valdrá 0. Luego en un while,
# mientras i sea menor a 200, sumará cada elemento al anterior
# y muestra el total
i = 0
total = 0
while i < 500:
    i = i + 1
    total = i + total
else:
    print(total)
