# 显示系统的欢迎信息
print('-'*20 , '欢迎使用员工管理系统', '-'*20)
# 创建一个列表，用来保存员工的信息，员工的信息以字符串的形式统一保存到列表
emps = ['孙悟空\t18\t男\t花果山','猪八戒\t28\t男\t高老庄']

# 创建一个死循环
while True:
    # 显示用户的选项
    print('请选择要做的操作：')
    print('\t1.查询员工')
    print('\t2.添加员工')
    print('\t3.删除员工')
    print('\t4.退出系统')
    user_choose = input('请选择[1-4]:')
    print('-'*62)
    # 根据用户的选择做相关的操作
    if user_choose == '1' :
        # 查询员工
        # 打印表头
        print('\t序号\t姓名\t年龄\t性别\t住址')
        # 创建一个变量，来表示员工的序号
        n = 1
        # 显示员工信息
        for emp in emps :
            print(f'\t{n}\t{emp}')
            n += 1
    elif user_choose == '2':
        # 添加员工
        # 获取要添加员工的信息，姓名、年龄、性别、住址
        emp_name = input('请输入员工的姓名：')
        emp_age = input('请输入员工的年龄：')
        emp_gender = input('请输入员工的性别：')
        emp_address = input('请输入员工的住址：')

        # 创建员工信息
        # 将四个信息拼接为一个字符串，然后插入到列表中
        emp = f'{emp_name}\t{emp_age}\t{emp_gender}\t{emp_address}'
        # 显示一个提示信息
        print('以下员工将被添加到系统中')
        print('-'*62)
        print('姓名\t年龄\t性别\t住址')
        print(emp)
        print('-'*62)
        user_confirm = input('是否确认该操作[Y/N]:')

        # 判断
        if user_confirm == 'y' or user_confirm == 'yes' :
            # 确认
            emps.append(emp)
            # 显示提示信息
            print('添加成功！')
        else :
            # 取消操作
            print('添加已取消！')
        
    elif user_choose == '3':
        # 删除员工，根据员工的序号来删除员工
        # 获取要删除的员工的序号
        del_num = int(input('请输入要删除的员工的序号：'))

        # 判断序号是否有效
        if 0 < del_num <= len(emps) :
            # 输入合法，根据序号来获取索引
            del_i = del_num - 1
            # 显示一个提示信息
            print('以下员工将被删除')
            print('-'*62)
            print('\t序号\t姓名\t年龄\t性别\t住址')
            print(f'\t{del_num}\t{emps[del_i]}')
            print('-'*62)
            user_confirm = input('该操作不可恢复，是否确认[Y/N]:')
            # 判断
            if user_confirm == 'y' or user_confirm == 'yes' :
                # 删除元素
                emps.pop(del_i)
                # 显示提示
                print('员工已被删除！')
            else :
                # 操作取消
                print('操作已取消！')
        else :
            # 输入有误
            print('您的输入有误，请重新操作！')

    elif user_choose == '4':
        # 退出
        print('欢迎使用！再见!')
        input('点击回车键退出！')
        break
    else :
        print('您的输入有误，请重新选择！')

    # 打印分割线
    print('-'*62)