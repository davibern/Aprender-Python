# Importar
from datetime import datetime
import math


# Solicita al usuario su edad.
def solicitar_edad():
    edad = 0
    mensaje = ""

    try:
        edad = int(input("¿Qué edad tienes?: "))
    except ValueError:
        mensaje = "Error: el dato introducido no es un número válido."
    finally:
        mensaje = f'Tu edad es {edad} años'

    if edad < 0:
        mensaje = "La edad debe ser mayor o igual a cero."
        return solicitar_edad()

    print(mensaje)


solicitar_edad()


# Solicita al usuario su año de nacimiento y le calculas la edad mostrándolo por pantalla
def calcular_nacimiento():
    edad = 0
    anio = 0
    mensaje = ""

    try:
        edad = int(input("¿Qué edad tienes para calcular tu edad?: "))
        now = datetime.now()
        anio = now.year - edad
    except ValueError:
        mensaje = "Error: el dato introducido no es nu número válido."
    finally:
        mensaje = f'El año de nacimiento fue en {anio}'

    if edad < 0:
        mensaje = "La edad debe ser mayor o igual a cero."
        return calcular_nacimiento()

    print(mensaje)


calcular_nacimiento()


# Calcular el factorial
def calcular_factorial():
    num = 0
    mensaje = ""

    try:
        num = int(input("Ingrese un número: "))
        mensaje = f'El factorial de {num} es {math.factorial(num)}'
    except ValueError:
        mensaje = "Error: el dato introducido no es un número"

    print(mensaje)


calcular_factorial()
