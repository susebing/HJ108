# coding=utf-8
"""
题目描述
给出一个名字，该名字有26个字符串组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个字母拥有相同的“漂亮度”。字母忽略大小写。
给出多个名字，计算每个名字最大可能的“漂亮度”。
输入描述:
整数N，后续N个名字

输出描述:
每个名称可能的最大漂亮程度

示例1
输入
复制
2
zhangsan
lisi
输出
复制
192
101
"""

# 方法一
# 这道题使用Counter模块来做非常适合，
# 将字母出现的顺序递减排列，
# 分别乘以26、25、24……就可以得到结果

from collections import Counter

while True:
    try:
        a = int(input())
        for i in range(a):
            c, start, res = Counter(input()), 26, 0
            for j in c.most_common():
                res += j[1] * start
                start -= 1
            print(res)
    except:
        break

# 方法二
while True:
    try:
        a = int(input())
        s = []
        for i in range(0, a):
            s.append(input().lower())
        for each in s:
            sum1 = 0
            c = 26
            count = []
            for i in list(set(each)):
                count.append(each.count(i))
                count = sorted(count, reverse=1)

            for i in count:
                sum1 += int(i) * c
                c -= 1
            print(sum1)
    except:
        break
