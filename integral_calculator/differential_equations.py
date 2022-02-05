def du(x, y):
    return y * (1 - x)


def fx():  # метод Эйлера
    x = 0
    b = 1
    y = 1
    n = 10
    h = (b - x) / n  # шаг интегрирования
    strokax = ''
    strokay = ''
    for i in range(n):
        y += h * du(x, y)
        x += h
        strokax += str(round(x, 5)) + ' '
        strokay += str(round(y, 5)) + ' '
    return f'Шаг: {h}\nx: {strokax}\ny: {strokay}'


def rk():  # метод Рунге-Кутта
    x = 0
    b = 1
    y = 1
    n = 10
    h = (b - x) / n
    strokax = ''
    strokay = ''
    for i in range(n):
        k1 = h * du(x, y)
        k2 = h * du(x + h / 2, y + k1 / 2)
        k3 = h * du(x + h / 2, y + k2 / 2)
        k4 = h * du(x + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
        strokax += str(round(x, 5)) + ' '
        strokay += str(round(y, 5)) + ' '
    return f'Шаг: {h}\nx: {strokax}\ny: {strokay}'


def sum():
    return 'Метод Эйлера:\n' + fx() + '\n\nМетод Рунге-Кутта:\n' + rk()
