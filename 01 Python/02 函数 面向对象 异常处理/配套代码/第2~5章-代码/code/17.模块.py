# import m

# # 访问模块中的变量：模块名.变量名
# # print(m.a , m.b)

# # m.test2()

# p = m.Person()

# print(p.name)

def test2():
    print('这是主模块中的test2')


# 也可以只引入模块中的部分内容
# 语法 from 模块名 import 变量,变量....
# from m import Person
# from m import test
# from m import Person,test
# from m import * # 引入到模块中所有内容，一般不会使用
# p1 = Person()
# print(p1)
# test()
# test2()

# 也可以为引入的变量使用别名
# 语法：from 模块名 import 变量 as 别名
# from m import test2 as new_test2

# test2()
# new_test2()

from m import *
# print(_c)

# import xxx
# import xxx as yyy
# from xxx import yyy , zzz , fff
# from xxx import *
# from xxx import yyy as zz
