# 高阶函数
# 接收函数作为参数，或者将函数作为返回值的函数是高阶函数
# 当我们使用一个函数作为参数时，实际上是将指定的代码传递进了目标函数

# 创建一个列表
l = [1,2,3,4,5,6,7,8,9,10]

# 定义一个函数
#   可以将指定列表中的所有的偶数，保存到一个新的列表中返回

# 定义一个函数，用来检查一个任意的数字是否是偶数
def fn2(i) :
    if i % 2 == 0 :
        return True

    return False    

# 这个函数用来检查指定的数字是否大于5
def fn3(i):
    if i > 5 :
        return True    
    return False

def fn(func , lst) :

    '''
        fn()函数可以将指定列表中的所有偶数获取出来，并保存到一个新列表中返回

        参数：
            lst：要进行筛选的列表
    '''
    # 创建一个新列表
    new_list = []

    # 对列表进行筛选
    for n in lst :
        # 判断n的奇偶
        if func(n) :
            new_list.append(n)
        # if n > 5 :
        #     new_list.append(n)

            


    # 返回新列表
    return new_list

# def fn4(i):
#     if i % 3 == 0:
#         return True    
#     return False

def fn4(i):
    return i % 3 == 0
        
# print(fn(fn4 , l))

# filter()
# filter()可以从序列中过滤出符合条件的元素，保存到一个新的序列中
# 参数：
#  1.函数，根据该函数来过滤序列（可迭代的结构）
#  2.需要过滤的序列（可迭代的结构）
# 返回值：
#   过滤后的新序列（可迭代的结构）

# fn4是作为参数传递进filter()函数中
#   而fn4实际上只有一个作用，就是作为filter()的参数
#   filter()调用完毕以后，fn4就已经没用
# 匿名函数 lambda 函数表达式 （语法糖）
#   lambda函数表达式专门用来创建一些简单的函数，他是函数创建的又一种方式
#   语法：lambda 参数列表 : 返回值
#   匿名函数一般都是作为参数使用，其他地方一般不会使用

def fn5(a , b):
    return a + b

# (lambda a,b : a + b)(10,20)
# 也可以将匿名函数赋值给一个变量，一般不会这么做
fn6 = lambda a,b : a + b
# print(fn6(10,30))


r = filter(lambda i : i > 5 , l)
# print(list(r))

# map()
# map()函数可以对可跌倒对象中的所有元素做指定的操作，然后将其添加到一个新的对象中返回
l = [1,2,3,4,5,6,7,8,9,10]

r = map(lambda i : i ** 2 , l)

# print(list(r))

# sort()
# 该方法用来对列表中的元素进行排序
# sort()方法默认是直接比较列表中的元素的大小
# 在sort()可以接收一个关键字参数 ， key
#   key需要一个函数作为参数，当设置了函数作为参数
#   每次都会以列表中的一个元素作为参数来调用函数，并且使用函数的返回值来比较元素的大小
l = ['bb','aaaa','c','ddddddddd','fff']
# l.sort(key=len)

l = [2,5,'1',3,'6','4']
l.sort(key=int)
# print(l)

# sorted()
# 这个函数和sort()的用法基本一致，但是sorted()可以对任意的序列进行排序
#   并且使用sorted()排序不会影响原来的对象，而是返回一个新对象

l = [2,5,'1',3,'6','4']
# l = "123765816742634781"

print('排序前:',l)
print(sorted(l,key=int))
print('排序后:',l)