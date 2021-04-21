a = int(10) # 创建一个int类的实例
b = str('hello') # 创建一个str类的实例

# print(a , type(a))
# print(b , type(b))

# 定义一个简单的类
# 使用class关键字来定义类，语法和函数很像！
# class 类名([父类]):
#   代码块
# <class '__main__.MyClass'>
class MyClass():
    pass

# print(MyClass)
# 使用MyClass创建一个对象
# 使用类来创建对象，就像调用一个函数一样
mc = MyClass() # mc就是通过MyClass创建的对象，mc是MyClass的实例
mc_2 = MyClass()
mc_3 = MyClass()
mc_4 = MyClass()
# mc mc_2 mc_3 mc_4 都是MyClass的实例，他们都是一类对象
# isinstance()用来检查一个对象是否是一个类的实例
result = isinstance(mc_2,MyClass)
result = isinstance(mc_2,str)

# print(mc , type(mc))
# print('result =',result)

# print(id(MyClass) , type(MyClass))

# 现在我们通过MyClass这个类创建的对象都是一个空对象
# 也就是对象中实际上什么都没有，就相当于是一个空的盒子
# 可以向对象中添加变量，对象中的变量称为属性
# 语法：对象.属性名 = 属性值
mc.name = '孙悟空'
mc_2.name = '猪八戒'

print(mc_2.name)
