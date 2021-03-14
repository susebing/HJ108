# coding=utf-8
"""
题目描述

注意：字典中可能有重复单词
输入描述:
先输入字典中单词的个数，再输入n个单词作为字典单词。
输入一个单词，查找其在字典中兄弟单词的个数
再输入数字n

输出描述:
根据输入，输出查找到的兄弟单词的个数

示例1
输入
复制
3 abc bca cab abc 1
输出
复制
2
bca
"""

# 尼玛，出题的语文水平简直服了。一道破题，坑比要求还多。
# 1.输出不是一行，而是两行，分别是数量及对应的单词。
# 2.要判断一下，如果兄弟单词列表为空或者输入的数字大于列表的长度，都不进行输出。。。
# 3.强行把简单题目难度上升到困难，你们开心就好。
# 方法一
from collections import defaultdict

while True:
    try:
        dd = defaultdict(list)
        a = input().split()
        # words是输入的单词，lookup是要查找的单词，num是要查找兄弟单词的索引，brothers是找到的兄弟单词列表
        words, lookup, num, brothers = a[1:1 + int(a[0])], a[-2], int(a[-1]), []
        for i in words:
            dd["".join(sorted(i))].append(i)
        for i in dd["".join(sorted(lookup))]:
            if i != lookup: brothers.append(i)
        # 下面这两行坑的老子调了半个小时。
        print(len(brothers))
        if brothers and num <= len(brothers):
            print(sorted(brothers)[num - 1])
    except:
        break

# 方法二
while True:
    try:
        s = input().split(' ')
        N = int(s.pop(0))
        n = int(s.pop())
        if len(s) == N:
            print(0)
            break
        if n > N:
            print(0)
            break
        b = s.pop()
        bob = sorted(b)

        s = sorted(s)
        ce, m = 0, ''
        for j in s:
            if sorted(j) == bob and j != b:
                ce += 1
                if ce == n:
                    m = j
        print(ce)
        if m:
            print(m)
    except:
        break

# 方法二
while True:
    try:
        s = input().split(" ")
        sl = s[1:int(s[0]) + 1]
        st = s[int(s[0]) + 1]
        sn = int(s[int(s[0]) + 2])  # 要查找的兄弟单词的指定序号
        ans = []
        for i in sl:
            if i != st and sorted(list(i)) == sorted(list(st)):  # 判断要抄找的单词是不是原单词，以及是不是兄弟单词
                ans.append(i)
        ans.sort()  # 对兄弟单词排序
        print(len(ans))  # 打印出兄弟单词的数量
        if sn <= len(ans):  # 查找指定序号的兄弟单词
            print(ans[sn - 1])  # 序号从1开始，列表从0开始
    except:
        break
