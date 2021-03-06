# coding=utf-8
"""
题目描述
问题描述：在计算机中，通配符一种特殊语法，广泛应用于文件搜索、数据库、正则表达式等领域。现要求各位实现字符串通配符的算法。
要求：
实现如下2个通配符：
*：匹配0个或以上的字符（字符由英文字母和数字0-9组成，不区分大小写。下同）
？：匹配1个字符

输入：
通配符表达式；
一组字符串。

输出：
返回匹配的结果，正确输出true，错误输出false

输入描述:
先输入一个带有通配符的字符串，再输入一个需要匹配的字符串

输出描述:
返回匹配的结果，正确输出true，错误输出false

示例1
输入
复制
te?t*.*
txt12.xls
输出
复制
false
"""

import re

while True:
    try:
        a, b = input().strip(), input().strip()
        a = a.replace("?", "\w{1}")\
            .replace(".", "\.")\
            .replace("*", "\w*")
        c = re.findall(a, b)
        if b in c and len(c) == 1:
            print("true")
        else:
            print("false")
    except:
        break

# 方法二
while True:
    try:
        a = input()
        b = input()
        x = 0
        y = 0
        flag = "true"
        while x < len(a) - 1 and y < len(b) - 1:
            if a[x] == b[y] or a[x] == '?':
                x += 1
                y += 1
            elif a[x] == '*':
                if a[x + 1] == b[y + 1]:
                    x += 1
                    y += 1
                else:
                    y += 1
            else:
                flag = "false"
                break
        print(flag)
    except:
        break
