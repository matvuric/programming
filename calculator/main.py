import math
import decimal
import doctest


def convert_precision(precision):
    """
        Возвращает целое число, соответствующее количеству знаков после запятой в переданном аргументе

        >>> convert_precision(0.000001)
        6

        >>> convert_precision("0.000001")
        6

        >>> convert_precision(0.01)
        2
    """
    try:
        return abs(decimal.Decimal(str(precision).rstrip('0')).as_tuple().exponent)
    except decimal.InvalidOperation:
        raise TypeError('Неверный тип аргумента')


def std(args, precision):
    """
        Возвращает среднеквадратичное отклонение с заданной точностью

        >>> std([1, 2, 3, 4, 5, 6], '0.000001')
        1.707825

        >>> std([1, 6, 10, 25, 76, 16], '0.0001')
        25.1705

        >>> std([5, 1, 8, 9, 15], 0.00000001)
        4.63033476
    """
    try:
        s = 0
        for i in args:
            s += (i - sum(args) / len(args)) * (i - sum(args) / len(args))
        r = round(math.sqrt(1 / len(args) * s), convert_precision(precision))
        return r
    except TypeError:
        raise TypeError('Неверный тип аргумента')


def mult_with_prec(x, y, precision=None):
    """
        Возвращает результат умножения с заданной точностью

        >>> mult_with_prec(2.1231241, 3.12312453, '0.00001')
        6.63078

        >>> mult_with_prec(5.1235652, 7.89593, '0.001')
        40.455

        >>> mult_with_prec(3, 2, 0)
        6.0
    """
    try:
        x = float(x)
        y = float(y)
        r = x * y
        if precision:
            r = round(r, convert_precision(precision))
        return r
    except ValueError:
        raise TypeError('Неверный тип аргумента')


def calculate(x, y, act):
    """
        Возвращает результат введенной операции

        >>> calculate(2.0001, 3, '+')
        5.0001

        >>> calculate(2, 3, '-')
        -1

        >>> calculate(2, 3, '*')
        6
    """
    try:
        if act == '+':
            r = x + y
        elif act == '-':
            r = x - y
        elif act == '*':
            r = x * y
        elif act == '/':
            try:
                r = x / y
            except ZeroDivisionError:
                raise ZeroDivisionError('Деление на 0 невозможно')
        elif act == "^":
            r = x ** y
        elif act == '//':
            try:
                r = x // y
            except ZeroDivisionError:
                raise ZeroDivisionError('Деление на 0 невозможно')
        elif act == '%':
            try:
                r = x % y
            except ZeroDivisionError:
                raise ZeroDivisionError('Деление на 0 невозможно')
        else:
            raise ValueError('Введенное действие нельзя выполнить')
        return r
    except TypeError:
        raise TypeError('Неверный тип аргумента')


if __name__ == '__main__':
    doctest.testmod()
