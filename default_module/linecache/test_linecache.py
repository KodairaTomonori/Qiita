import linecache

if __name__ == '__main__':
    a = input('取り出したい行数は？：')
    target_line = linecache.getline('sample.txt', int(a))
    print(target_line)
    linecache.clearcache()

