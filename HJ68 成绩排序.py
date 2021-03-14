# coding=utf-8
"""
题目描述
查找和排序

题目：输入任意（用户，成绩）序列，可以获得成绩从高到低或从低到高的排列,相同成绩
都按先录入排列在前的规则处理。

例示：
jack      70
peter     96
Tom       70
smith     67

从高到低  成绩
peter     96
jack      70
Tom       70
smith     67

从低到高

smith     67
jack      70
Tom       70
peter     96

注：0代表从高到低，1代表从低到高
输入描述:
输入多行，先输入要排序的人的个数，然后分别输入他们的名字和成绩，以一个空格隔开

输出描述:
按照指定方式输出名字和成绩，名字和成绩之间以一个空格隔开

示例1
输入
复制
3
0
fang 90
yang 50
ning 70
输出
复制
fang 90
ning 70
yang 50
"""

while True:
    try:
        num = int(input())
        flag = False if int(input().strip()) == 1 else True
        out = []
        for i in range(num):
            info = input().split()
            out.append((info[0], int(info[1])))
        for j in sorted(out, key=lambda x: x[1], reverse=flag):
            print(j[0], j[1])
    except:
        break
