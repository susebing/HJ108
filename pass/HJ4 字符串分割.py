"""
题目描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述:
连续输入字符串(输入2次,每个字符串长度小于100)

输出描述:
输出到长度为8的新字符串数组

示例1
输入
复制
abc
123456789
输出
复制
abc00000
12345678
90000000
"""

while 1:
    try:
        s = input()
        while len(s) > 8:
            print(s[:8])
            s = s[8:]
        print(s.ljust(8, '0'))
    except:
        break
