import unittest

from main import calculate, convert_precision, write_log


class TestCalculate(unittest.TestCase):
    def test_exceptions(self):
        with self.assertRaisesRegex(TypeError, 'Неверный тип аргумента'):
            convert_precision('0.000001a')
            calculate(5, 'a', '+')
            calculate('b', 2, '+')

        with self.assertRaisesRegex(ZeroDivisionError,
                                    'Деление на 0 невозможно'):
            calculate(5, 0, '/')

    def test_creating_file_exception(self):
        args = [1, 2, 3, 4, 5]
        log_file = 'newoutput.txt'

        self.assertRaises(Exception,
                          write_log,
                          *args,
                          action='sum',
                          file=log_file)

    def test_creating_file_exception_with_descr(self):
        args = [1, 2, 3, 4, 5]
        log_file = 'newoutput.txt'
        # f'Ошибка записи в файл {file_new}. Записать не удалось.'

        regex_text = 'Ошибка записи в файл'
        with self.assertRaisesRegex(Exception, regex_text) as cm:
            write_log(*args, action='sum', file=log_file)
        # the_exception = cm.exception


if __name__ == '__main__':
    unittest.main(verbosity=1)
