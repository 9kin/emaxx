'''
import pytestlib
https://github.com/MikeMirzayanov/testlib
'''
import random
import os
import shutil


def gen_int(range=(0, 1)):
    ''' generate int '''
    if range == (0, 1):
        return random.random()
    return random.randint(*range)


def change(obj, value):
    '''add item'''
    obj.append(value)


def gen_test(list):
    """[[1test], [2test], ....] -> [1test, 2test, ....]"""
    return [''.join(str(item) for item in lines) for lines in list]


def refile(replace_map, file, data):
    '''write data in the file with replace_map'''
    for cur_replace in replace_map:
        file = file.replace(cur_replace, str(replace_map[cur_replace]))
    dir = file[:file.rfind('/')]
    if file.rfind('/') != -1 and not os.path.exists(dir):
        os.makedirs(dir)
    open(file, 'w').write(data)


def gen_to_file(string_refile, list):
    '''data [1test, 2test, ....] -> foo/{test}/input.txt'''
    for n_test in range(len(list)):
        refile({'{test}': n_test}, string_refile, list[n_test])


shutil.rmtree('foo', ignore_errors=True)
foo = []
for i in range(10):
    sampletest = str(i) + '\n'
    change(foo, sampletest)
a = gen_test(foo)
print('s')
gen_to_file('foo/{test}/input.txt', a)
