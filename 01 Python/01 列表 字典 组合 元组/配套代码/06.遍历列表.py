# 遍历列表，指的就是将列表中的所有元素取出来
# 创建列表
stus = ['孙悟空','猪八戒','沙和尚','唐僧','白骨精','蜘蛛精']

# 遍历列表
# print(stus[0])
# print(stus[1])
# print(stus[2])
# print(stus[3])

# 通过while循环来遍历列表
# i = 0
# while i < len(stus):
#     print(stus[i])
#     i += 1

# 通过for循环来遍历列表
# 语法：
#   for 变量 in 序列 :
#       代码块
# for循环的代码块会执行多次，序列中有几个元素就会执行几次
#   没执行一次就会将序列中的一个元素赋值给变量，
#   所以我们可以通过变量，来获取列表中的元素

for s in stus :
    print(s)