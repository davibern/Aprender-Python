'''
La búsqueda inocente recorre una lista de principio a fin.
'''
def busqueda_inocente(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return 1
    return -1
