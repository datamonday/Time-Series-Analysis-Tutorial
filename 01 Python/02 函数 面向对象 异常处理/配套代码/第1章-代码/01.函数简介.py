# 比如有如下三行代码，这三行代码是一个完整的功能
# print('Hello')
# print('你好')
# print('再见')

# 定义一个函数
def fn() :
    print('这是我的第一个函数！')
    print('hello')
    print('今天天气真不错！')

# 打印fn
# print(fn) <function fn at 0x03D2B618>
# print(type(fn)) <class 'function'>

# fn是函数对象  fn()调用函数
# print是函数对象 print()调用函数
# fn()

# 定义一个函数，可以用来求任意两个数的和
# def sum() :
#     a = 123
#     b = 456
#     print(a + b)

# sum()

# 定义函数时指定形参
def fn2(a , b) :
    # print('a =',a)
    # print('b =',b)
    print(a,"+",b,"=",a + b)

# 调用函数时，来传递实参
fn2(10,20)
fn2(123,456)
