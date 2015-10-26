#usr/bin/python

import time


def timer(func):
    def print_time(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(func.__name__ + \
            'の実行にかかった時間は{}秒です'.format(time.time() - start) )
    return print_time

@timer
def roop_timer(a):
    return roop(a)


def roop(a):
    sum_ = 0
    for i in range(a):
        sum_ += i
    return sum_


if __name__ == '__main__':
    roop_timer(10000)
    timer(roop)(10000)
