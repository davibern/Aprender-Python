import random
import string


def generar_contrasenia(longitud=12) -> str:
    """
    Genera una contraseña aleatoria de una longitu determinada.

    Args:
        longitud (int, opcional): La longitud de la contraseña, por defecto 12.

    Returns:
        str: La contraseña generada.
    """

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasenia = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasenia


if __name__ == "__main__":
    longitud = int(input("Ingresa la longitud de la contraseña:"))
    contrasenia = generar_contrasenia(longitud)
    print(f'Tu contraseña es: {contrasenia}')
