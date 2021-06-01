# IPython log file

import collections
collections.defaultdict(int)
collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
# OrderedDict是字典子类，记得其内容被添加的顺序
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'
for k, v in d.items():
    print (k, v)
# namedtuple 标准的元组使用数值索引来访问其成员
Person = collections.namedtuple('Person', 'name age gender')
print('Type of Person:', type(Person))
bob = Person(name='Bob', age=30, gender='male')
print('\nRepresentation:', bob)
jane = Person(name='Jane', age=29, gender='female')
print('\nField by name:', jane.name)
print('\nFields by index:')
for p in [bob, jane]:
    print('%s is a %d year old %s' % p)
get_ipython().run_line_magic('pinfo', 'd')
def func():
    """
    this is a function.
    """
    pass
get_ipython().run_line_magic('pinfo2', 'func')
get_ipython().run_line_magic('run', 'test.py')
get_ipython().run_line_magic('paste', '')
import numpy as np
a = np.random.rand(10, 10)
a
get_ipython().run_line_magic('time', 'np.dot(a, a)')
get_ipython().run_line_magic('timeit', 'np.dot(a, a)')
get_ipython().run_line_magic('pinfo', '%timeit')
# 显示IPython的快速参考
get_ipython().run_line_magic('quickref', '')
# 显示所有魔术命令的文档
get_ipython().run_line_magic('magic', '')
raise ValueError("Test")
# 从最新的异常跟踪的底部进入交互式调试器
get_ipython().run_line_magic('debug', '')
# 打印命令的输入（可选输出）的历史
get_ipython().run_line_magic('hist', '')
# 删除交互式命令空间中的全部变量/名称
get_ipython().run_line_magic('reset', '')
# 通过分页打印输出对象
get_ipython().run_line_magic('page', 'a')
# 显示交互式命名空间中定义的变量，信息级别/冗余度可变
get_ipython().run_line_magic('who', '')
get_ipython().run_line_magic('who_ls', '')
get_ipython().run_line_magic('whos', '')
b = 10
c = b
# 删除变量，并尝试清楚其在IPython中的一切引用
get_ipython().run_line_magic('xdel', 'b')
# 变量b被删除，并把b的引用c一并删除！
c
get_ipython().run_line_magic('logstart', '')
get_ipython().run_line_magic('pinfo', '%logstart')
get_ipython().run_line_magic('logon', '')
get_ipython().run_line_magic('logstate', '')
# pycharm ipython console测试可用
# jupyter notebook不可用
get_ipython().system('python')
# pycharm ipython console测试可用
# jupyter notebook不可用
get_ipython().system('cmd')
get_ipython().run_line_magic('dirs', '')
get_ipython().run_line_magic('bookmark', 'bm ./bookmarks/')
get_ipython().run_line_magic('cd', 'bm')
# 列出所有书签
get_ipython().run_line_magic('bookmark', '-l')
get_ipython().run_line_magic('ls', '')
# 将当前目录入栈，并专项目标目录
get_ipython().run_line_magic('pushd', './bookmarks')
# 弹出栈顶项目录，并转向目标目录
get_ipython().run_line_magic('popd', '')
# 返回上级目录
cd ..
# 返回上级目录
cd ..
# 返回上级目录
cd ..
# 返回上级目录
get_ipython().system('cd ..')
# 返回一个含有当前目录栈的列表
get_ipython().run_line_magic('dirs', '')
# 打印目录访问历史
get_ipython().run_line_magic('dhist', '')
# 以字典形式返回系统环境变量
get_ipython().run_line_magic('env', '')
get_ipython().system('nvcc -V')
# 返回系统的当前工作目录
pwd
# 返回系统的当前工作目录
get_ipython().system('pwd')
get_ipython().system('htop')
# 返回系统的当前工作目录
get_ipython().system('cwd')
# 返回系统的当前工作目录
get_ipython().system('pdw')
# 返回系统的当前工作目录
get_ipython().system('pwd')
