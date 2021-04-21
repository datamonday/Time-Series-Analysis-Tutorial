file_name = 'c:/Users/lilichao/Desktop/告白气球.flac'

# 读取模式
# t 读取文本文件（默认值）
# b 读取二进制文件

with open(file_name , 'rb') as file_obj:
    # 读取文本文件时，size是以字符为单位的
    # 读取二进制文件时，size是以字节为单位
    # print(file_obj.read(100))

    # 将读取到的内容写出来
    # 定义一个新的文件
    new_name = 'aa.flac'

    with open(new_name , 'wb') as new_obj:

        # 定义每次读取的大小
        chunk = 1024 * 100

        while True :
            # 从已有的对象中读取数据
            content = file_obj.read(chunk)

            # 内容读取完毕，终止循环
            if not content :
                break

            # 将读取到的数据写入到新对象中
            new_obj.write(content)