"""
题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

输入描述:
输入一个int型整数

输出描述:
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

示例1
输入
复制
9876673
输出
复制
37689
"""
while 1:
    try:
        arr = list(input())
        res = []
        while arr:
            a = arr.pop()
            if a not in res:
                res.append(a)
        print(''.join(res))
    except:
        break