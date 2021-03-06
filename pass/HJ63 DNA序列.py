# coding=utf-8
"""
题目描述
一个DNA序列由A/C/G/T四个字母的排列组合组成。G和C的比例（定义为GC-Ratio）是序列中G和C两个字母的总的出现次数除以总的字母数目（也就是序列长度）。在基因工程中，这个比例非常重要。因为高的GC-Ratio可能是基因的起始点。
给定一个很长的DNA序列，以及要求的最小子序列长度，研究人员经常会需要在其中找出GC-Ratio最高的子序列。

输入描述:
输入一个string型基因序列，和int型子串的长度

输出描述:
找出GC比例最高的子串,如果有多个输出第一个的子串

示例1
输入
复制
AACTGTGCACGACCTGA
5
输出
复制
GCACG
"""

while True:
    try:
        s, n, gc, index = input(), int(input()), 0, 0
        for i in range(0, len(s) - n + 1):
            gc_ratio = s.count('G', i, i + n) + s.count('C', i, i + n)
            if gc < gc_ratio:
                gc = gc_ratio
                index = i
        print(s[index:index + n])
    except:
        break

# 方法二 易懂
while True:
    try:
        p = input()
        n = int(input())
        maxcount = 0
        str1 = ''
        for i in range(len(p) + 1 - n):
            a = p[i:i + n]
            xucount = a.count('C') + a.count('G')
            if xucount > maxcount:
                str1 = a
                maxcount = xucount
        print(str1)
    except:
        break
