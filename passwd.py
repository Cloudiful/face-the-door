def input_password():
    passwd = input("请输入密码：")
    if passwd == "123456":
        print("密码正确！")
        return "success"
    else:
        print("密码错误！")
        return "error"
