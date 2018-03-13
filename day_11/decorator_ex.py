import time
import random


def log_time(func):
    def inner():
        start = time.time()
        x = func()
        end = time.time() - start
        print(f'czas dzialania funkcji {end}')
        return x
    return inner

@log_time
def foo():
    val = random.randint(1, 5)
    print('before sleep')
    time.sleep(val)
    print('after sleep')


if __name__ == '__main__':
    # log_time(foo)
    foo()  # inner()