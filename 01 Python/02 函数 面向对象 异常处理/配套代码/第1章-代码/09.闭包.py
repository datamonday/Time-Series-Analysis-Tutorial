# 将函数作为返回值返回，也是一种高阶函数
# 这种高阶函数我们也称为叫做闭包，通过闭包可以创建一些只有当前函数能访问的变量
#   可以将一些私有的数据藏到的闭包中

def fn():

    a = 10

    # 函数内部再定义一个函数
    def inner():
        print('我是fn2' , a)

    # 将内部函数 inner作为返回值返回   
    return inner

# r是一个函数，是调用fn()后返回的函数
# 这个函数实在fn()内部定义，并不是全局函数
# 所以这个函数总是能访问到fn()函数内的变量
r = fn()    

# r()

# 求多个数的平均值
# nums = [50,30,20,10,77]

# sum()用来求一个列表中所有元素的和
# print(sum(nums)/len(nums))

# 形成闭包的要件
#   ① 函数嵌套
#   ② 将内部函数作为返回值返回
#   ③ 内部函数必须要使用到外部函数的变量
def make_averager():
    # 创建一个列表，用来保存数值
    nums = []

    # 创建一个函数，用来计算平均值
    def averager(n) :
        # 将n添加到列表中
        nums.append(n)
        # 求平均值
        return sum(nums)/len(nums)

    return averager

averager = make_averager()

print(averager(10))
print(averager(20))
print(averager(30))
print(averager(40))


