def print_triangle(size):
    for row in range(size):
        for col in range(row + 1):
            print("*", end="")
        print()


if __name__ == "__main__":
    size = int(input("Ingrese el tamaño del triángulo: "))
    print_triangle(size)
