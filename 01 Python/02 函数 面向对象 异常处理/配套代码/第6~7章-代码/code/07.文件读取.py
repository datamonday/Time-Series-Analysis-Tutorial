import pprint
import os
file_name = 'demo.txt'

with open(file_name , encoding='utf-8') as file_obj:
    # readline()
    # 该方法可以用来读取一行内容
    # print(file_obj.readline(),end='')
    # print(file_obj.readline())
    # print(file_obj.readline())

    # readlines()
    # 该方法用于一行一行的读取内容，它会一次性将读取到的内容封装到一个列表中返回
    # r = file_obj.readlines()
    # pprint.pprint(r[0])
    # pprint.pprint(r[1])
    # pprint.pprint(r[2])

    for t in file_obj:
        print(t)

    