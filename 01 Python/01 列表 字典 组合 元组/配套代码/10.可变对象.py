# # 可变对象
# a = [1,2,3]
# print('修改前：', a , id(a))

# # 通过索引修改列表
# a[0] = 10
# print('修改后：', a , id(a))

# # 为变量重新赋值
# a = [4,5,6]
# print('修改后：', a , id(a))


a = [1,2,3]
b = a
# b[0] = 10
b = [10,2,3]
# print("a",a,id(a))
# print("b",b,id(b))

# == !=  is is not
# == != 比较的是对象的值是否相等 
# is is not 比较的是对象的id是否相等（比较两个对象是否是同一个对象）

a = [1,2,3]
b = [1,2,3]
print(a,b)
print(id(a),id(b))
print(a == b) # a和b的值相等，使用==会返回True
print(a is b) # a和b不是同一个对象，内存地址不同，使用is会返回False

