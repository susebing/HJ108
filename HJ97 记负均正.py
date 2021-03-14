# coding=utf-8
"""
题目描述
首先输入要输入的整数个数n，然后输入n个整数。输出为n个整数中负数的个数，和所有正整数的平均值，结果保留一位小数。

输入描述:
首先输入一个正整数n，
然后输入n个整数。

输出描述:
输出负数的个数，和所有正整数的平均值。

示例1
输入
复制
5
1 2 3 4 5

输出
复制
0 3.0
"""

# 看清楚n个数是横着输入还是竖着输入。
# 输出格式中间是空格 不是换行。
# 所以感觉 n 没有用。

while 1:
    try:
        n = int(input())
        arr = map(int, input().split())
        count = 0
        zheng = []
        for x in arr:
            if x > 0:
                zheng.append(x)
            if x < 0:
                count += 1
        print(f'{count} {round(sum(zheng) / len(zheng), 1)}')
    except:
        break
