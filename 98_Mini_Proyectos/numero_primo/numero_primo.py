def calcular_numero_primo(numero: int) -> bool:
    '''
    Esta función determina si un número es primo o no.
    Un número primo es aquel que solo es divisible por 1 y por sí mismo.

    Args:
        numero (int): El número a evaluar.

    Returns:
        bool: True si el número es primo, False en caso contrario.
    '''

    # Casos especiales
    if numero <= 1:
        # 1 y negativos no son primos
        return False
    if numero <= 3:
        # 2 y 3 son primos
        return True

    # Si el número es par o divisible por 3, no es primo
    if numero % 2 == 0 or numero % 3 == 0:
        return False

    # Verificar divisibilidad desde 5 hasta la raíz cuadrada del número
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True


numero = 29
if calcular_numero_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
