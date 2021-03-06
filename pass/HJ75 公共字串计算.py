# coding=utf-8
"""
题目描述
题目标题：
计算两个字符串的最大公共字串的长度，字符不区分大小写

详细描述：
接口说明
原型：
int getCommonStrLength(char * pFirstStr, char * pSecondStr);
输入参数：
     char * pFirstStr //第一个字符串
     char * pSecondStr//第二个字符串

输入描述:
输入两个字符串

输出描述:
输出一个整数

示例1
输入
复制
asdfas
werasdfaswer

输出
复制
6
"""

# 使用较短字符串长度倒序遍历，取下标时在纸上推导很容易理解
# 如果去较长的，时间复杂度更大

while True:
    try:
        a = input()
        b = input()
        n = 0
        if len(a) > len(b):
            a, b = b, a
        for i in range(len(a)):
            if a[i - n:i + 1] in b:
                n += 1
        print(n)
    except:
        break
