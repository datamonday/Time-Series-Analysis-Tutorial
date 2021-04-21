# open(file, mode='r', buffering=-1, encoding_=None, errors=None, newline=None, closefd=True, opener=None)
# 使用open函数来打开一个文件
# 参数：
#   file 要打开的文件的名字（路径）
# 返回值：
#   返回一个对象，这个对象就代表了当前打开的文件

# 创建一个变量，来保存文件的名字
# 如果目标文件和当前文件在同一级目录下，则直接使用文件名即可
file_name = 'demo.txt'

# 在windows系统使用路径时，可以使用/来代替 \
# 或者可以使用 \\ 来代替 \
# 或者也可以使用原始字符串
file_name = 'hello\\demo.txt'
file_name = r'hello\demo.txt'

# 表示路径，可以使用..来返回一级目录
file_name = '../hello/demo.txt'

# 如果目标文件距离当前文件比较远，此时可以使用绝对路径
# 绝对路径应该从磁盘的根目录开始书写
file_name = r'C:\Users\lilichao\Desktop\hello.txt'

# file_obj = open(file_name) # 打开 file_name 对应的文件

# print(file_obj)
