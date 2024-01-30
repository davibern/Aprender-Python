'''
La búsqueda binaria divide la búsqueda en tres tramos, el principio, la mitad, y el final de la lista.

La eficiencia de este algoritmo es increíblemente eficaz y rápido.
'''
def busqueda_binaria(lista, objetivo, min = None, max = None):
    
    # Configurar los límites si no se especifican como parámetros
    if min is None:
        min = 0
    if max is None:
        max = len(lista) - 1
    
    # Validar que se incluyen límites válidos
    if max < min:
        return -1
    
    # Recursión para implementar búsqueda binaria
    # Obtenemos la parte central de los extremos, de esta forma no calculamos la lista entera, sino por partes
    mediana = (min + max) // 2
    
    if lista[mediana] == objetivo:
        #return -1
        return mediana
    elif objetivo < lista[mediana]:
        return busqueda_binaria(lista, objetivo, min, mediana -1)
    else:
        return busqueda_binaria(lista, objetivo, mediana + 1, max)
