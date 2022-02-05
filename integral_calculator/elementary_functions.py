import math


def ex(x):
    e = 0.0000002
    n = 7
    a = [0.9999998, 1, 0.5000063, 0.1666674, 0.41635, 0.0083298, 0.0014393, 0.000204]
    c = a[0]
    k = p = 1
    while k < n:
        p *= x
        u = p * a[k]
        c += u
        if abs(u) <= e:
            return f'C = {c}, K = {k}'
        k += 1
    print("Требуемая точность не достигнута")


def sinx(x):
    e = 0.000000006
    n = 5
    a = [1.000000002, -0.166666589, 0.008333075, -0.000198107, 0.000002608]
    x *= math.pi / 180
    c = a[0] * x
    k = p = 1
    while x < n:
        p *= (x * x)
        u = p * a[k] * x
        c += u
        if abs(u) <= e:
            return f'C = {c}, K = {k}'
        k += 1
    print("Требуемая точность не достигнута")


def iterat1():
    e = 0.00001
    y0 = y = 3.8
    x = 14.76
    r = 1
    while r > e:
        y = (y0 + x / y0) / 2
        r = abs(y - y0)
        y0 = y
    return f'y = {y}'


def iterat2():
    e = 0.00001
    y0 = y = 0.24
    x = 14.32
    r = 1
    while r > e:
        y = y0 / 2 * (3 - x * y0 * y0)
        r = abs(y - y0)
        y0 = y
    return f'y = {y}'


def sum(x):
    return 'e^x: ' + ex(x) + '\nsin(x): ' + sinx(x) + '\nМетод итераций (1): ' + iterat1() + '\nМетод итераций (2): ' + iterat2()
