# Реализовать класс который можно использовать и как декоратор и как менеджер контекста
# Пусть он тоже замеряет время выполнения.
# Проверить что работает быстрее - вызвать и обработать исключение или использовать условный оператор
from contextlib import ContextDecorator
import time
class my_context_decorator(ContextDecorator):

        def __init__(self):
            pass

            # print('init')


        def __enter__(self):
            # print('enter')
            self.k = time.time()

        def __exit__(self, exc_type, exc_val, exc_tb):
            # print('exit')
            print(time.time() - self.k)
            return True


def delen1(b):
    # print('begin')

    try:
         r = 5 / b
    except:
            return 'mistake'
    # print('end')
    return r

def delen2(b):
    if b != 0:
        return 5 / b
    else:
        return 'mist'

with my_context_decorator():
    for i in range(100):
        print(delen1(0))

with my_context_decorator():
    for i in range(100):
        print(delen2(0))
