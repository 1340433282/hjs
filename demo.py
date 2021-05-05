#让用户输入多个用户，每次输入都要提示是否继续
while True:
    answer = input("是否要输入用户信息（Y/N）:")
    if answer=="Y":
        uer1_name=input("请输入用户姓名：")
        print("输入用户信息是：",uer1_name)
    elif answer=="N":
        print("不需要输入用户信息")
        break
    else:
        print("填写错误，请重新填写")
        
