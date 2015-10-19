#usr/bin/python
'''
 python 3.5
'''

import collections
import see
dict_a = dict(a=1, b=2, c=3)
dict_b = dict(x=10, y=11, z=12)
def get_name(arg_id, arg_values):
    for key, value in arg_values.items():
        if id(value) == arg_id: return key
    return 'NotDefined'

def print_arguments(*args, arg_values):
    for arg in args:
        print(get_name(id(arg), arg_values) + ' : ' + repr(arg) )


if __name__ == '__main__':
    chain_map = collections.ChainMap(dict_a, dict_b)
    child = chain_map.new_child()
    print('make_chain_maps')
    print_arguments(chain_map, child, arg_values=locals() )
    print('chain_map.maps: ' + repr(chain_map.maps) )
    print()

    child.update(d=4, a=0)
    print('update_child_map')
    print_arguments(chain_map, child, arg_values=locals() )
    print()

    chain_map.update(z=100)
    print('update_parent_map')
    print_arguments(chain_map, child, arg_values=locals() )
    print()


    child2 = child.new_child()
    child2['a'] += 5
    print('make_second_child')
    print_arguments(chain_map, child, child2, arg_values=locals() )
    print()
    print('value key=a')
    print('chain_map[a] = ' + repr(chain_map['a']) )
    print('child[a]     = ' + repr(child['a']) )
    print('child2[a]    = ' + repr(child2['a']) )
    print()
    print('each_Chain')
    print('chain_map:', dict(**chain_map) )
    print('child    :', dict(**child) )
    print('child2   :', dict(**child2) )
