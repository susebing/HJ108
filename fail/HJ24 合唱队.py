# coding=utf-8
"""
题目描述
计算最少出列多少位同学，使得剩下的同学排成合唱队形

说明：
N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形。
合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，他们的身高分别为T1，T2，…，TK，
则他们的身高满足存在i（1<=i<=K）使得T1<T2<......<Ti-1<Ti>Ti+1>......>TK。

你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

注意不允许改变队列元素的先后顺序
请注意处理多组输入输出！

输入描述:
整数N

输出描述:
最少需要几位同学出列

示例1
输入
复制
8
186 186 150 200 160 130 197 200
输出
复制
4
"""

import bisect


def deal(l, res):
    b = [9999] * len(l)
    for i in range(len(l)):
        pos = bisect.bisect_left(b, l[i])
        res += [pos + 1]
        b[pos] = l[i]
    return res


while True:
    try:
        n = int(input())
        s = list(map(int, input().split()))
        dp1 = []
        dp2 = []
        dp1 = deal(s, dp1)
        dp2 = deal(s[::-1], dp2)[::-1]
        a = max(dp1[i] + dp2[i] for i in range(n))
        print(n - a + 1)
    except:
        break
