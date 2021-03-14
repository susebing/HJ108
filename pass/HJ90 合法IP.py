# coding=utf-8
"""
题目描述
现在IPV4下用一个32位无符号整数来表示，一般用点分方式来显示，点将IP地址分成4个部分，每个部分为8位，表示成一个无符号整数（因此不需要用正号出现），如10.137.17.1，是我们非常熟悉的IP地址，一个IP地址串中没有空格出现（因为要表示成一个32数字）。

现在需要你用程序来判断IP是否合法。

输入描述:
输入一个ip地址

输出描述:
返回判断的结果YES or NO

示例1
输入
复制
10.138.15.1
输出
复制
YES
"""

# 二进制8位数最大为11111111，转换为十进制就是255
# 1.首先合法的IP地址为: A.B.C.D,其中A,B,C,D的取值范围为0-255。

while True:
    try:
        ip = input().split(".")
        isValid = True
        for i in ip:
            if 0 <= int(i) <= 255:
                pass
            else:
                isValid = False
                break
        print("YES" if isValid else "NO")
    except:
        break

# 方法二
while True:
    try:
        # 遍历输入的每个段
        for i in input().strip().split('.'):
            # 如果是数字，并且该数字对应的整型在[0,256]范围内
            if not (i.isdigit() and 0 <= int(i) <= 255):
                print('NO')
                break
        # 如果上面的遍历没有触发break，则执行这个else，打印YES
        else:
            print('YES')
    except:
        break
