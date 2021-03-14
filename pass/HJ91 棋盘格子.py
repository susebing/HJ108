# coding=utf-8
"""
题目描述
请编写一个函数（允许增加子函数），计算n x m的棋盘格子（n为横向的格子数，m为竖向的格子数）沿着各自边缘线从左上角走到右下角，总共有多少种走法，要求不能走回头路，即：只能往右和往下走，不能往左和往上走。
输入描述:
输入两个正整数

输出描述:
返回结果

示例1
输入
复制
2
2
输出
复制
6
"""


def f(n, m):
    if n == 0 or m == 0:
        return 1
    else:
        return f(n - 1, m) + f(n, m - 1)


while True:
    try:
        n, m = map(int, input().split())
        print(f(n, m))
    except:
        break
