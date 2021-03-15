# coding=utf-8
"""
题目描述
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
输入描述:
输入两个字符串
输出描述:
返回重复出现的字符

示例1
输入
复制
abcdefghijklmnop
abcsafjklmnopqrstuvw

输出
复制
jklmnop
"""

# 思路：动态规划经典问题，加一个start标记即可,注意将较短子串最先出现的那个输出
# 先确定那个长，那个短，短的切片，在长的中找

while True:
    try:
        a = input()
        b = input()
        n = 0
        s = ''
        if len(a) > len(b):
            a, b = b, a
        for i in range(len(a)):
            if a[i-n:i+1] in b:
                s = a[i-n:i+1]
                n += 1
        print(s)
    except:
        break
