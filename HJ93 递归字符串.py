# coding=utf-8
"""
题目描述
编写一个函数，传入一个int型数组，返回该数组能否分成两组，使得两组中各元素加起来的和相等，并且，所有5的倍数必须在其中一个组中，所有3的倍数在另一个组中（不包括5的倍数），能满足以上条件，返回true；不满足时返回false。
输入描述:
第一行是数据个数，第二行是输入的数据

输出描述:
返回true或者false

示例1
输入
复制
4
1 5 -5 1
输出
复制
true
"""

while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))
        x = []
        y = []
        z = []
        for i in a:
            if i % 5 == 0:
                x.append(i)
            elif i % 3 == 0:
                y.append(i)
            else:
                z.append(abs(i))

        s1 = sum(x)
        s2 = sum(y)
        s3 = sorted(z, reverse=True)

        for i in s3:
            if s1 < s2:
                s1 += i
            else:
                s2 += i
        print('true' if s1 == s2 else 'false')

    except:
        break
