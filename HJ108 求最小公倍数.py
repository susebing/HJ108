# coding=utf-8
"""
题目描述
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。

输入描述:
输入两个正整数A和B。

输出描述:
输出A和B的最小公倍数。

示例1
输入
复制
5 7
输出
复制
35
"""

# a*b = 最小公倍数*最大公约数

while True:
    try:
        a, b = map(int, input().split())
        r = a * b
        for i in range(2, min(a, b)):
            if (a % i == 0 and b % i == 0):
                r = r / i
        print(int(r))
    except:
        break
