'''
Juego del ahorcado:

- El jugador tendrá 7 vidas o terminar todo el abecedario para adivinar la palabra.

Proyecto de FreeCodeCamp (https://github.com/estefaniacn/freecodecamp-proyectos-youtube)
'''
import random
import string

from palabras import palabras
from vidas import interfaz_vidas


def obtener_palabra(palabras):
    # 1. Seleccionamos una palabra al azar de la lista importada de palabras
    palabra = random.choice(palabras)
    
    # 2. Pasamos la palabra a mayúscula
    return palabra.upper()


def ahorcado():
    
    print("⭐ Bienvenido al Ahorcado ⭐")
    
    # 1. Obtenemos la palabra aleatoria
    palabra = obtener_palabra(palabras)
    # 2. Conjunto de letras que tienen que ser adivinadas (los conjuntos no admiten duplicados)
    letras_por_adivinar = set(palabra)
    # 3. El conjunto de letras del abecedario
    abecedario = set(string.ascii_uppercase)
    # 4. Añadimos la Ñ al abecedario
    abecedario.add("Ñ")
    # 5. Conjunto de letras usadas, creamos un conjunto vacío
    letras_usadas = set()
    # Inicializamos las vidas
    vidas = 7
    
    '''
    Algoritmo:
    
    - Bucle donde obtenemos la respuesta del usuario mientras existan letras pendientes
    y al jugador le queden vidas
    '''
    while len(letras_por_adivinar) > 0 and vidas > 0:
        # Letras adivinadas
        print(f'Te quedan {vidas} vidas y has usado estas letras: {" ".join(letras_usadas)}')
        
        # Estado de la palabra
        # Si la letra usada está en la palabra la incluye, si no, escribe un guión
        lista_palabra = [letra if letra in letras_usadas else '-' for letra in palabra]
        print(interfaz_vidas[vidas])
        print(f'Palabra: {" ".join(lista_palabra)}')
        
        # El usuario escoge una letra nueva
        letra_usuario = input('Escoge una letra: ').upper()
        
        # Si la letra escogida está en el abecedario y no está en el conjunto de letras que ya eligió
        # se añaden al conjunto de letras añadidas
        if letra_usuario in abecedario - letras_usadas:
            letras_usadas.add(letra_usuario)
            # Si la letra está en la palabra, se elimina del conjunto de letras pendientes por adivinar
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            # Si la letra no está, se elimina una vida
            else:
                vidas -= 1
                print(f'\nTu letra {letra_usuario} no está en la palabra.')
        elif letra_usuario in letras_usadas:
            print('\nYa elegiste esta letra, por favor elige otra.')
        else:
            print('\nEsta letra no es válida')
    
    # El juego llega a esta línea cuando no queden vidas o se adivinen todas las letras de la palabra
    if vidas == 0:
        print(f'¡Ahorcado! Lo siento has perdido 😢, la palabra era {palabra}')
    else:
        print(f'⭐ ¡Has ganado!, adivinaste la palabra {palabra}')
        

if __name__ == '__main__':
    ahorcado()