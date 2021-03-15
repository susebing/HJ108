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
#利用栈，检测')'，最终输出。
# 解题思路：利用栈存储，一次存两个数，存行和列，
# 然后每次遇到(不处理，遇到字母入栈，遇到扩回出栈，
# 注意处理(A(B(CD)))这一类的情况，
# 这种情况多一个扩回，要进行检测避免栈空还出栈的异常，
# 同时，也要处理(A(BCD))的情况，避免最后)检测结束，
# 栈中存放两个以上行列的情况。每次计算的结果加到res中累加，最终输出。

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
