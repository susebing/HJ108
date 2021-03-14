# coding=utf-8
"""
题目描述
找出字符串中第一个只出现一次的字符

输入描述:
输入几个非空字符串

输出描述:
输出第一个只出现一次的字符，如果不存在输出-1

示例1
输入
复制
asdfasdfo
aabb
输出
复制
o
-1
"""

while True:
    try:
        a = input()
        for i in a:
            if a.count(i) == 1:
                print(i)
                break
        else:
            print(-1)
    except:
        break
