class Dog:
    '''
        表示狗的类
    '''
    def __init__(self , name , age , gender , height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def jiao(self):
        '''
            狗叫的方法
        '''
        print('汪汪汪~~~')

    def yao(self):
        '''
            狗咬的方法
        '''  
        print('我咬你~~')

    def run(self):
        print('%s 快乐的奔跑着~~'%self.name)     


d = Dog('小黑',8,'male',30)

# 目前我们可以直接通过 对象.属性 的方式来修改属性的值，这种方式导致对象中的属性可以随意修改
#   非常的不安全，值可以任意修改，不论对错
# 现在我们就需要一种方式来增强数据的安全性
#   1.属性不能随意修改（我让你改你才能改，不让你改你就不能改）
#   2.属性不能修改为任意的值（年龄不能是负数）
d.name = '阿黄'
d.age = -10
d.run()

print(d.age)

# print(d.name , d.age , d.gender , d.height)
        