import random

MAX_INTENTOS = 10


def adivinar_numero() -> None:
    """
    Juego para adivinar un número aleatorio entre 1 y 100.
    El jugador tiene 10 intentos para adivinar el número.
    Returns:
        bool: devuelve True si el jugador adivina el número, False si se queda sin intentos.
    """
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("Bienvenido al juego de adivinar el número.\nEstá comprendido entre 1 y 100.")
    print("Tienes 10 intentos para dar con él, ¡suerte!")

    while intentos <= MAX_INTENTOS:
        try:
            numero_usuario = int(input(f'Te quedan {MAX_INTENTOS - intentos} intentos. ¿Cuál es tu número? '))

            if intentos == 11:
                print(f'El número secreto era {numero_secreto}')
                print('Más suerte la próxima vez :(')
                break

            if numero_usuario < 1 or numero_usuario > 100:
                print('El número debe estar entre 1 y 100.')
                continue

            if numero_usuario == numero_secreto:
                print(f'¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.')
                break
            elif numero_usuario < numero_secreto:
                print('El número es mayor.')
                continue
            else:
                print('El número es menor.')
                continue

        except ValueError:
            print('Por favor, introduce un número válido.')
            continue
        except KeyboardInterrupt:
            print('\nJuego terminado por el usuario.')
            break
        except Exception as e:
            print(f'Error inesperado: {e}')
            break
        finally:
            intentos += 1


if __name__ == '__main__':
    adivinar_numero()
