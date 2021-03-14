# coding=utf-8
"""
题目描述
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度大于2的子串重复

输入描述:
一组或多组长度超过2的子符串。每组占一行

输出描述:
如果符合要求输出：OK，否则输出NG

示例1
输入
复制
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
输出
复制
OK
NG
NG
OK
"""

while 1:
    try:
        pwd = input()
        a, b, c, d = 0, 0, 0, 0
        for s in pwd:
            if s.isupper():
                a = 1
            elif s.islower():
                b = 1
            elif s.isdigit():
                c = 1
            else:
                d = 1
        flag = True
        for i in range(len(pwd) - 3):
            s3 = pwd[i:i + 3]
            if pwd.count(s3) >= 2:
                flag = False
        if len(pwd) > 8 and (a + b + c + d) >= 3 and flag:
            print('OK')
        else:
            print('NG')
    except:
        break

# 方法二
import re

while 1:
    try:
        s = input()
        a = re.findall(r'(.{3,}).*\1', s)
        b1 = re.findall(r'\d', s)
        b2 = re.findall(r'[A-Z]', s)
        b3 = re.findall(r'[a-z]', s)
        b4 = re.findall(r'[^0-9A-Za-z]', s)
        print('OK' if ([b1, b2, b3, b4].count([]) <= 1 and a == [] and len(s) > 8) else 'NG')
    except:
        break
