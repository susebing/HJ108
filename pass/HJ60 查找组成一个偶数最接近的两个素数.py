# coding=utf-8
"""
题目描述
任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对
输入描述:
输入一个偶数

输出描述:
输出两个素数

示例1
输入
复制
20
输出
复制
7
13
"""


def sushu(x):
    for j in range(2, x):
        if x % j == 0:
            return False
    return True


while 1:
    try:
        n = int(input())
        m = n // 2
        for i in range(m):
            a = n // 2 - i
            b = n // 2 + i
            if sushu(a) and sushu(b):
                print(a)
                print(b)
                break
    except:
        break
