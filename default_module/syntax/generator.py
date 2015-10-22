#usr/bin/python

def sub_generator():
    for i in range(0, 101, 10):
        yield i
    return 'finished'

def pp():
    print('b')

def fibonatti():
    now = 0
    next_num = 1
    while True:
        yield now
        now, next_num = next_num, now + next_num

def counter():
    num = 0
    while True:
        yield num
        num += 1

def generator(step):
    val = 0
    prev = 0
    while True:
        if step == None:
            step = prev
        prev = step
        val += step
        step = yield val



if __name__ == '__main__':
    count = counter()
    print('print 1-3, for i in count')
    for i in count:
        print(i, end=', ')
        if i >= 3:
            print()
            break
    print('next_count, count.__next__()')
    print(count.__next__())
    print('print 5-7, for i in count')
    for i in count:
        print(i, end=', ')
        if i >= 7:
            count.close()
            print()
    print('print fibonatti')
    for i in fibonatti():
       if i > 100: break
       print(i, end=', ')
    print(i)
    gen = generator(0)
    print(gen.__next__(), end=', ')
    for i in [1,2,3,4,5,6]:
        print(gen.send(i) , end=', ')
    print()
