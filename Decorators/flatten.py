import os
import datetime

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            res = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as f:
                t = datetime.datetime.now()
                data = f'Время вызова функции {old_function.__name__} с аргументами {args} и {kwargs} - {t}, результат - {res}\n'
                f.write(data)
            return res
        return new_function

    return __logger


PATH = 'log_4.log'


@logger(PATH)
# функция преобразования вложенного списка в плоский
def flatten(l):
    if l == []:
        return l
    if isinstance(l[0], list):
        return flatten(l[0]) + flatten(l[1:])
    return l[:1] + flatten(l[1:])

list_of_lists_3 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], 7],
        [1, 2, 4, [[[[['!']]]]], []]
    ]



if __name__ == '__main__':
    if os.path.exists(PATH):
            os.remove(PATH)
    flatten(list_of_lists_3)