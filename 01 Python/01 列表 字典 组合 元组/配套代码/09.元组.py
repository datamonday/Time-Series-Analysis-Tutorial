# 元组 tuple
# 元组是一个不可变的序列
# 它的操作的方式基本上和列表是一致的
# 所以你在操作元组时，就把元组当成是一个不可变的列表就ok了
# 一般当我们希望数据不改变时，就使用元组，其余情况都使用列表

# 创建元组
# 使用()来创建元组
my_tuple = () # 创建了一个空元组
# print(my_tuple,type(my_tuple)) # <class 'tuple'>

my_tuple = (1,2,3,4,5) # 创建了一个5个元素的元组
# 元组是不可变对象，不能尝试为元组中的元素重新赋值
# my_tuple[3] = 10 TypeError: 'tuple' object does not support item assignment
# print(my_tuple[3])

# 当元组不是空元组时，括号可以省略
# 如果元组不是空元组，它里边至少要有一个,
my_tuple = 10,20,30,40
my_tuple = 40,
# print(my_tuple , type(my_tuple))

my_tuple = 10 , 20 , 30 , 40

# 元组的解包（解构）
# 解包指就是将元组当中每一个元素都赋值给一个变量
a,b,c,d = my_tuple

# print("a =",a)
# print("b =",b)
# print("c =",c)
# print("d =",d)

a = 100
b = 300
# print(a , b)

# 交互a 和 b的值，这时我们就可以利用元组的解包
a , b = b , a

# print(a , b)
my_tuple = 10 , 20 , 30 , 40


# 在对一个元组进行解包时，变量的数量必须和元组中的元素的数量一致
# 也可以在变量前边添加一个*，这样变量将会获取元组中所有剩余的元素
a , b , *c = my_tuple
a , *b , c = my_tuple
*a , b , c = my_tuple
a , b , *c = [1,2,3,4,5,6,7]
a , b , *c = 'hello world'
# 不能同时出现两个或以上的*变量
# *a , *b , c = my_tuple SyntaxError: two starred expressions in assignment
print('a =',a)
print('b =',b)
print('c =',c)
 
