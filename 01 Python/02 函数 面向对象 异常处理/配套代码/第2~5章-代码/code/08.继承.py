# 继承

# 定义一个类 Animal（动物）
#   这个类中需要两个方法：run() sleep() 
class Animal:
    def run(self):
        print('动物会跑~~~')

    def sleep(self):
        print('动物睡觉~~~')

    # def bark(self):
    #     print('动物嚎叫~~~')   

# 定义一个类 Dog（狗）
#   这个类中需要三个方法：run() sleep() bark()
# class Dog:
#     def run(self):
#         print('狗会跑~~~')

#     def sleep(self):
#         print('狗睡觉~~~')

#     def bark(self):
#         print('汪汪汪~~~') 

# 有一个类，能够实现我们需要的大部分功能，但是不能实现全部功能
# 如何能让这个类来实现全部的功能呢？
#   ① 直接修改这个类，在这个类中添加我们需要的功能
#       - 修改起来会比较麻烦，并且会违反OCP原则
#   ② 直接创建一个新的类
#       - 创建一个新的类比较麻烦，并且需要大量的进行复制粘贴，会出现大量的重复性代码
#   ③ 直接从Animal类中来继承它的属性和方法
#       - 继承是面向对象三大特性之一
#       - 通过继承我们可以使一个类获取到其他类中的属性和方法
#       - 在定义类时，可以在类名后的括号中指定当前类的父类（超类、基类、super）
#           子类（衍生类）可以直接继承父类中的所有的属性和方法
#           
#  通过继承可以直接让子类获取到父类的方法或属性，避免编写重复性的代码，并且也符合OCP原则
#   所以我们经常需要通过继承来对一个类进行扩展

class Dog(Animal):
    def bark(self):
        print('汪汪汪~~~') 

    def run(self):
        print('狗跑~~~~')    

class Hashiqi(Dog):
    def fan_sha(self):
        print('我是一只傻傻的哈士奇')        

d = Dog()
h = Hashiqi()

# d.run()
# d.sleep()
# d.bark()

# r = isinstance(d , Dog)
# r = isinstance(d , Animal)
# print(r)

# 在创建类时，如果省略了父类，则默认父类为object
#   object是所有类的父类，所有类都继承自object
class Person(object):
    pass

# issubclass() 检查一个类是否是另一个类的子类
# print(issubclass(Animal , Dog))
# print(issubclass(Animal , object))
# print(issubclass(Person , object))

# isinstance()用来检查一个对象是否是一个类的实例
#   如果这个类是这个对象的父类，也会返回True
#   所有的对象都是object的实例
print(isinstance(print , object))

