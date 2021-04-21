# 字典
# 使用 {} 来创建字典
d = {} # 创建了一个空字典

# 创建一个保护有数据的字典
# 语法：
#   {key:value,key:value,key:value}
#   字典的值可以是任意对象
#   字典的键可以是任意的不可变对象（int、str、bool、tuple ...），但是一般我们都会使用str
#       字典的键是不能重复的，如果出现重复的后边的会替换到前边的
# d = {'name':'孙悟空' , 'age':18 , 'gender':'男' , 'name':'sunwukong'}
d = {
'name':'孙悟空' , 
'age':18 , 
'gender':'男' , 
'name':'sunwukong'
}

# print(d , type(d))

# 需要根据键来获取值
# print(d['name'],d['age'],d['gender'])

# 如果使用了字典中不存在的键，会报错
# print(d['hello']) KeyError: 'hello'