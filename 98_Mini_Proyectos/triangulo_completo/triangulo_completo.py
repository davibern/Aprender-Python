def draw_triangule(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))


draw_triangule(5)
