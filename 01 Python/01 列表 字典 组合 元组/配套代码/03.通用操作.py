# + 和 *
# +可以将两个列表拼接为一个列表
my_list = [1,2,3] + [4,5,6]

# * 可以将列表重复指定的次数
my_list = [1,2,3] * 5

# print(my_list)

# 创建一个列表
stus = ['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精','沙和尚','沙和尚']

# in 和 not in
# in用来检查指定元素是否存在于列表中
#   如果存在，返回True，否则返回False
# not in用来检查指定元素是否不在列表中
#   如果不在，返回True，否则返回False
# print('牛魔王' not in stus)
# print('牛魔王' in stus)

# len()获取列表中的元素的个数

# min() 获取列表中的最小值
# max() 获取列表中的最大值
arr = [10,1,2,5,100,77]
# print(min(arr) , max(arr))

# 两个方法（method），方法和函数基本上是一样，只不过方法必须通过 对象.方法() 的形式调用
# xxx.print() 方法实际上就是和对象关系紧密的函数
# s.index() 获取指定元素在列表中的第一次出现时索引
# print(stus.index('沙和尚'))
# index()的第二个参数，表示查找的起始位置 ， 第三个参数，表示查找的结束位置
# print(stus.index('沙和尚',3,7))
# 如果要获取列表中没有的元素，会抛出异常
# print(stus.index('牛魔王')) ValueError: '牛魔王' is not in list
# s.count() 统计指定元素在列表中出现的次数
print(stus.count('牛魔王'))