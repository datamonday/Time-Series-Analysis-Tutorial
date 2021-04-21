# 继承

# 定义一个类 Animal（动物）
#   这个类中需要两个方法：run() sleep() 
class Animal:
    def run(self):
        print('动物会跑~~~')

    def sleep(self):
        print('动物睡觉~~~')


class Dog(Animal):
    def bark(self):
        print('汪汪汪~~~') 

    def run(self):
        print('狗跑~~~~')    


# 如果在子类中如果有和父类同名的方法，则通过子类实例去调用方法时，
#   会调用子类的方法而不是父类的方法，这个特点我们成为叫做方法的重写（覆盖，override）
# 创建Dog类的实例
# d = Dog()

# d.run()

# 当我们调用一个对象的方法时，
#   会优先去当前对象中寻找是否具有该方法，如果有则直接调用
#   如果没有，则去当前对象的父类中寻找，如果父类中有则直接调用父类中的方法，
#   如果没有，则去父类的父类中寻找，以此类推，直到找到object，如果依然没有找到，则报错
class A(object):
    def test(self):
        print('AAA')

class B(A):
    def test(self):
        print('BBB')

class C(B):
    def test(self):
        print('CCC')   

# 创建一个c的实例
c = C()
c.test()

