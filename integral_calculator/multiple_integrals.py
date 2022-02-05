import math


def multiple_integral(n_x, n_y):
    b = math.pi / 2
    a = c = 0
    d = math.pi / 4
    h_x = (b - a) / n_x
    h_y = (d - c) / n_y
    s_x = 0
    x = a
    while x <= (b - h_x):
        s_y = y = 0
        while y <= (b - h_y):
            s_y += abs(math.sin(x + y))
            y += h_y
        i_y = h_y * s_y
        s_x += i_y
        x += h_x
    i_x = h_x * s_x
    return f'Hx = {h_x}\nHy = {h_y}\nSy = {s_y}\nINy = {i_y}\nSx = {s_x}\nINx = {i_x}'
