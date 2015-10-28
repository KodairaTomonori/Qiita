
def addition(num_a: int, num_b: int, flag: bool=True) -> int:
    '''
    この関数は、num_a + num_bを計算して返すプログラムです。
    flagをTrueにすると結果を見やすくprintしてくれます。
    '''
    if flag: print('{} + {} = {}'.format(num_a, num_b, num_a + num_b) )
    return num_a + num_b


if __name__ == '__main__':
    result = addition(1234, 4321)
    print('result:', result) 
    print('引数の情報: ', addition.__annotations__)
    print('関数の説明: ', addition.__doc__)
