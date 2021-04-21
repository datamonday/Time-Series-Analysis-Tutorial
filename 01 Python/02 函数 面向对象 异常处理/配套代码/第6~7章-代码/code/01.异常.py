# print('hello')
# try:
#     # try中放置的是有可能出现错误的代码
#     print(10/0)
# except:
#     # except中放置的是出错以后的处理防暑
#     print('哈哈哈，出错了~~~')
# else:
#     print('程序正常执行没有错误')    
# print('你好')


# print(10/0)


def fn():
    print('Hello fn')
    print(a)
    print(10/0)

def fn2():
    print('Hello fn2')
    fn()

def fn3():
    print('Hello fn3')
    fn2()

fn3()    
