# coding=utf-8
"""
题目描述
从输入任意个整型数，统计其中的负数个数并求所有非负数的平均值，结果保留一位小数，

如果没有非负数，则平均值为0

本题有多组输入数据，输入到文件末尾，请使用while(cin>>)读入
数据范围小于1e6
输入描述:
输入任意个整数

输出描述:
输出负数个数以及所有非负数的平均值

示例1
输入
复制
-13
-4
-7

输出
复制
3
0.0
"""

# 方法一
a, b = [], []
while 1:
    try:
        i = int(input())
        a.append(int(i)) if int(i) < 0 else b.append(int(i))
    except:
        break
print(len(a))
print(round(sum(b) / len(b), 1) if b else 0.0)

# 方式二
n = []
k = 0
while True:
    try:
        a = int(input())
        if a < 0:
            k += 1
        if a >= 0:
            n.append(a)
    except:
        break

print(k)
print(round(sum(n) / len(n), 1) if n else 0.0)
