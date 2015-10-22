def ex_permutation(iterable, now_list=[]):
    if not iterable: 
        yield now_list
        return
    for i in [iterable.index(i) for i in set(iterable)]:
        yield from permutation(iterable[:i] + iterable[i+1:], now_list + [iterable[i] ])


def counter():
    var = 0
    while True:
        var += 1
        yield var


if __name__ == '__main__':
    for i in ex_permutation([1,2,3,4,5,5,6]):
        print i
