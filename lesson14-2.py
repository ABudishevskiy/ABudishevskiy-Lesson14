# Использовать contextmanager и реализовать функцию, которая будет работать как менеджер контекста.
# И сможет замерять время выполнения блока

from  contextlib import  contextmanager
import time
@contextmanager
def foo(*args):
    print('__enter__ foo: ', args)
    k1 = time.time()
    try:
        yield 'hello'
    except: pass
    print('__enter__ foo')
    print(time.time()-k1)


with foo('start') as f:
    print(f)
    for i in range(10000):
        pass
    print('after exception')

class FFo:
    def __enter__(self):
        print('enter')

    def __exit__(self, *args):
        print('exit')

with FFo() as ff:
    print(ff)