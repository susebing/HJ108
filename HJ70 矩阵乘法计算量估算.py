# coding=utf-8
"""
题目描述
矩阵乘法的运算量与矩阵乘法的顺序强相关。
例如：
    A是一个50×10的矩阵，B是10×20的矩阵，C是20×5的矩阵
计算A*B*C有两种顺序：（（AB）C）或者（A（BC）），前者需要计算15000次乘法，后者只需要3500次。

编写程序计算不同的计算顺序需要进行的乘法次数

输入描述:
输入多行，先输入要计算乘法的矩阵个数n，每个矩阵的行数，列数，总共2n的数，最后输入要计算的法则

输出描述:
输出需要进行的乘法次数

示例1
输入
复制
3
50 10
10 20
20 5
(A(BC))
输出
复制
3500
"""

while True:
    try:
        n = int(input())
        arr = []
        order = []
        res = 0
        for i in range(n):
            arr.append(list(map(int, input().split())))
        f = input()
        for i in f:
            if i.isalpha():
                order.append(arr[ord(i) - 65])
            elif i == ')' and len(order) >= 2:
                a = order.pop()
                b = order.pop()
                res += b[0] * b[1] * a[1]
                order.append([b[0], a[1]])
        print(res)
    except:
        break
