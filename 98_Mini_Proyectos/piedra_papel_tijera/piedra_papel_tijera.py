import random


def jugar_piedra_papel_tijera():
    
    usuario = input('Escoje primero tu opción (piedra, papel o tijera):\n').lower()
    ia = random.choice(['piedra', 'papel', 'tijera'])
    
    if (usuario == ia):
        return '⭐⭐ ¡Ha habido un empate! ⭐⭐'
    
    if es_empate(usuario, ia):
        return '⭐⭐ ¡Has ganado! ⭐⭐\nLa IA ha seleccionado ' + ia
    
    return '😭😭 ¡Has perdido! 😭😭\nLa IA ha seleccionado ' + ia

    
def es_empate(usuario, ia):
    
    if ((usuario == 'piedra' and ia == 'tijera')
        or (usuario == 'tijera' and ia == 'papel')
        or (usuario == 'papel' and ia == 'piedra')):
        return True
    else:
        return False
    
print(jugar_piedra_papel_tijera())