import string


def print_results(*args, action=None, result=None):
    txt1 = 'A'
    txt2 = str(args[0])
    act = ' ' + action + ' '
    res = 'Результат'
    result = str(result)
    for i in range(1, len(args)):
        txt1 += act + string.ascii_uppercase[i]
        txt2 += act + str(args[i])
    second = '|' + txt2.center(len(txt2) + 10, ' ') + '|' + result.center(len(result) + 10, ' ') + '|'
    first = '|' + txt1.center(len(txt2) + 10, ' ') + '|' + res.center(len(result) + 10, ' ') + '|'
    line = ('=' * len(second)) + '\n'
    print(line + first + '\n' + line + second + '\n' + line)
