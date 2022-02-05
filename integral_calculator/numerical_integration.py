from math import sqrt


top = 5
low = 0


def function(z):
    integ = (7 / ((z ** 2) + 1))
    return integ


def permanent_integral(met=1, split=10):
    r = abs(((top - low) ** 2 / (2 * split)) * 16)
    step = (top - low) / split
    result = 0
    if met == 1:
        x = low
        while x <= top - step:
            result += function(x)
            x += step
        result *= step
        return f'Шаг = {step}, Результат: {result}\nОстаточный член: {r}'

    elif met == 2:
        x = low + step
        while x <= top:
            result += function(x)
            x += step
        result *= step
        return f'Шаг = {step}, Результат: {result}\nОстаточный член: {r}'

    elif met == 3:
        x = low + step
        while x <= top - step:
            result += function(x)
            x += step
        result = step * ((function(low) + function(top)) / 2 + result)
        return f'Шаг = {step}, Результат: {result}\nОстаточный член: {r}'

    elif met == 4:
        result1 = 0
        result2 = 0
        x = low + step
        while x <= top - step:
            result1 += function(x)
            x += 2 * step
        x = low + 2 * step
        while x <= top - 2 * step:
            result2 += function(x)
            x += 2 * step
        result = step / 3 * (function(low) + function(top) + 4 * result1 + 2 * result2)
        return f'Шаг = {step}, Результат: {result}\nОстаточный член: {r}'


def variable_integral1(split=10):
    k = abs(((top - low) ** 2 / (2 * split)) * 16)
    step = (top - low) / split
    e = 10 ** (-6)
    i1 = 0
    while True:
        summa = 0
        x = low
        while x <= top - step:
            summa += function(x)
            x += step
        i2 = step * summa
        r = abs(i2 - i1)
        i1 = i2
        step /= 2
        if not r > e:
            break
    return f'Результат1 = {i2}\nОстаточный член: {k}'


def variable_integral2():
    e = 0.1
    s = 0
    sum = 0
    fx = (function(low) + function(top)) / 2
    hv = e ** 1/4
    x = low + hv
    while x <= top - hv:
        s += function(x)
        x += hv
    In = hv * (fx + sum)
    hs = hv / 2
    x = low + hs
    while x <= top - hs:
        sum += function(x)
        x += hv
    I2n = hs * (fx + sum)
    while True:
        hv = hs
        r = abs(I2n - In)
        In = I2n
        hs = hv / 2
        x = low + hs
        while x <= top - hs:
            sum += function(x)
            x += hv
        I2n = hs * (fx + sum)
        if not r > e:
            break
    return f'Результат2 = {I2n}'


def sum(x):
    return f'{variable_integral1(x)}\n{variable_integral2()}'
