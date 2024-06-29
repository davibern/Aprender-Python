import csv

FICHERO_CSV: str = "liga.csv"

'''
Lee el fichero CSV y devuelve una lista de diccionarios con los datos de los partidos.
'''


def leer_fichero():
    datos = []
    keys = ["fecha", "equipo1", "equipo2", "final", "mitad"]
    with open(FICHERO_CSV, 'r') as fichero:
        contenido = csv.reader(fichero)
        for row in list(contenido)[1:]:
            partido = dict(zip(keys, row))
            datos.append(partido)
    return datos


'''
Recibe una lista de diccionarios y devuelve un conjunto único con los e equipos que aparecen en la lista.
'''


def equipos(datos):
    return (set(([partido["equipo1"] for partido in datos] + [partido["equipo2"] for partido in datos])))


'''
Función que recibe un resultado y calcula el ganador 1 si gana el equipo1, 0 si hay empate y -1 si gana el equipo visitante
'''


def quien_gana(resultado):
    goles_casa = int(resultado.split("-")[0])
    goles_visitante = int(resultado.split("-")[1])
    if goles_casa > goles_visitante:
        return 1
    elif goles_casa < goles_visitante:
        return -1
    else:
        return 0


'''
Recibe una lista con los partidos ganados, empatados y perdidos y devuelve
los puntos
'''


def puntos(info):
    return 3 * info[0] + info[2]


'''
Recibe una lista de diccionarios y devuelve una lista de tuplas, en cada
tupla se guarda un equipo con los partidos ganados, empatados y perdidos
y los puntos obtenidos
'''


def info_equipos(liga, *equipos):
    resultados = []
    for equipo in equipos:
        resultado = [0, 0, 0]
        for partido in liga:
            # Local
            if partido["equipo1"] == equipo and quien_gana(partido["final"]) == 1:
                resultado[0] += 1
            if partido["equipo1"] == equipo and quien_gana(partido["final"]) == -1:
                resultado[1] += 1
            if partido["equipo1"] == equipo and quien_gana(partido["final"]) == 0:
                resultado[2] += 1

            # Visitante
            if partido["equipo2"] == equipo and quien_gana(partido["final"]) == -1:
                resultado[0] += 1
            if partido["equipo2"] == equipo and quien_gana(partido["final"]) == 1:
                resultado[1] += 1
            if partido["equipo2"] == equipo and quien_gana(partido["final"]) == 0:
                resultado[2] += 1

        resultado.append(puntos(resultado))
        resultado.insert(0, equipo)

        resultado.append(tuple(resultado))
    return resultados


'''
Recibe una lista generada con la función anterior y la ordena según el número de puntos
'''


def clasificacion(datos):
    datos_ordenados = datos[:]
    datos_ordenados.sort(key=lambda datos: datos[4], reverse=True)
    return datos_ordenados


'''
Recibe una lista de diccionarios y genera la clasificación y los imprime por pantalla
'''


def imprimir_clasificacion(liga):
    datos = info_equipos(liga, *equipos(liga))
    contador = 1
    line = '-' * 61
    print(line)
    print("|   №    |     Equipo      |   PG   |   PP  |  PE   |Puntos |")
    print(line)
    for dato in clasificacion(datos):
        print('| {0:^6} | {1:^15} | {2:^6} |{3:^6} |{4:^6} |{5:^6} |'.format(contador, dato[0], dato[1], dato[2], dato[3], dato[4]))
        contador += 1
    print(line)


if __name__ == "__main__":
    liga = leer_fichero()
    imprimir_clasificacion(liga)
