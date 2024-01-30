try:
    file = open('data_temp.txt')
    content = file.read().splitlines()
    print(content)
    file.close()
except FileNotFoundError:
    print('Error: el fichero no existe')
