def ex_permutation(iterable, now_list=[]):
    if not iterable: 
        yield now_list
        return
    for i in [iterable.index(i) for i in set(iterable)]:
        yield from ex_permutation(iterable[:i] + iterable[i+1:], now_list + [iterable[i] ])


def counter():
    var = 0
    while True:
        var += 1
        yield var


if __name__ == '__main__':
    import time
    import itertools
    itarable = 'abcdefghijklmnopqrstu'
    start = time.time()
    list(ex_permutation(itarable) )
    #set(itertools.permutation(itarable) )
    print(time.time() - start)
