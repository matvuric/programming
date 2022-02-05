import math


def func(x):
    return (x - 2) * (x - 2) * math.log10(x + 11) - 1


def newton(y):
    e = 0.000001
    i = 0
    while True:
        y1 = y - ((y - 2) * (y - 2) * math.log10(y + 11) - 1) / (((y - 2) * (y - 2) / math.log(10) * (y + 11)) + 2 * (y - 2) * math.log10(y + 11))
        r = abs(y-y1)
        y = y1
        i += 1
        if r <= e:
            break
    return f'Результат: {y}, Кол-во итераций: {i}'


def separation():
    e = 0.000001
    a = 0
    b = 10
    i = 0
    x = x1 = x2 = 5
    y = func(x)
    while True:
        x1 += e
        x2 -= e
        y1 = func(x1)
        y2 = func(x2)
        p1 = y * y1
        p2 = y * y2
        if p1 < 0:
            b = x1
            a = b - e
            break
        elif p2 < 0:
            a = x2
            b = a + e
            break
        i += 1
        if a == 10:
            break
    return f'a: {a}, F(a): {func(a)}, b: {b}, F(b): {func(b)}, Кол-во итераций: {i}'


def division():
    e = 0.000001
    a = 0
    b = 10
    i = 0
    while True:
        y = (a + b) / 2
        if func(y) > 0:
            b = y
        else:
            a = y
        i += 1
        if not abs(func(y)) > e:
            break
    return f'Результат: {y}, Кол-во итераций: {i}'


def hord():
    a = 0
    b = 10
    i = 0
    e = 0.000001
    z = b
    while True:
        f = (z - 2) * (z - 2) * math.log10(z + 11) - 1
        f0 = (a - 2) * (a - 2) * math.log10(a + 11) - 1
        z -= f / (f0 - f) * (a - z)
        i += 1
        if not abs(f) > e:
            break
    return f'Результат: {z}, Кол-во итераций: {i}'


def sum(x):
    return 'Ньютон: ' + newton(x) + '\nДихотомия (1): ' + separation() + '\nДихотомия (2): ' + division() + '\nХорд: ' + hord()
