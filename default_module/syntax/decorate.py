#usr/bin/python

deco =  '｡+ﾟ+｡･ﾟ･｡+*+｡･★･｡+*+｡･===[ '
deco_end = deco.replace('[', ']')[::-1]
deco_result = [' ∧____∧  結果を', '( ｀Д´ )    出力するぞ', '(っ▄︻▇〓┳═ ', '/　　 )', '( /￣∪']

def deco_func(func):
    def wrapper(*args, **kwargs):
        print(deco + 'start   ' + func.__name__ + deco_end)
        for i in range(len(deco_result) ):
            if i != 2: print(deco_result[i])
            else: print(deco_result[i], func(*args, **kwargs) )
        print(deco + 'end     ' + func.__name__ + deco_end)
    return wrapper


def timer(func):
    def print_time(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(func.__name__ + \
            'の実行にかかった時間は{}秒です'.format(time.time() - start) )
    return print_time

@deco_func
def addition(a, b):
    return '{} + {} = {}'.format(a, b, a + b)


if __name__ == '__main__':
    addition(103842, 283746)
