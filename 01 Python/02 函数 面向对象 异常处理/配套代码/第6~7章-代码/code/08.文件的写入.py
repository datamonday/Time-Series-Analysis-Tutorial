file_name = 'demo5.txt'

# 使用open()打开文件时必须要指定打开文件所要做的操作（读、写、追加）
# 如果不指定操作类型，则默认是 读取文件 ， 而读取文件时是不能向文件中写入的
# r 表示只读的
# w 表示是可写的，使用w来写入文件时，如果文件不存在会创建文件，如果文件存在则会截断文件
#   截断文件指删除原来文件中的所有内容
# a 表示追加内容，如果文件不存在会创建文件，如果文件存在则会向文件中追加内容
# x 用来新建文件，如果文件不存在则创建，存在则报错
# + 为操作符增加功能
#   r+ 即可读又可写，文件不存在会报错
#   w+
#   a+
# with open(file_name , 'w' , encoding='utf-8') as file_obj:
# with open(file_name , 'r+' , encoding='utf-8') as file_obj:
with open(file_name , 'x' , encoding='utf-8') as file_obj:
    # write()来向文件中写入内容，
    # 如果操作的是一个文本文件的话，则write()需要传递一个字符串作为参数
    # 该方法会可以分多次向文件中写入内容
    # 写入完成以后，该方法会返回写入的字符的个数
    file_obj.write('aaa\n')
    file_obj.write('bbb\n')
    file_obj.write('ccc\n')
    r = file_obj.write(str(123)+'123123\n')
    r = file_obj.write('今天天气真不错')
    print(r)
