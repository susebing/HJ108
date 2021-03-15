# coding=utf-8
"""
题目描述
题目标题：

将两个整型数组按照升序合并，并且过滤掉重复数组元素。
输出时相邻两数之间没有空格。
请注意本题有多组样例。

输入描述:
输入说明，按下列顺序输入：
1 输入第一个数组的个数
2 输入第一个数组的数值
3 输入第二个数组的个数
4 输入第二个数组的数值

输出描述:
输出合并之后的数组

示例1
输入
复制
3
1 2 5
4
-1 0 3 2
输出
复制
-101235
"""

# 一开始还以为有很多个数组，没想到就两个数组，题目真的让人产生误解
# python只需要两行就能通过：
# 方法一
while True:
    try:
        a, b, c, d = input(), list(map(int, input().split())), input(), list(map(int, input().split()))
        print("".join(map(str, sorted(list(set(b + d))))))
    except:
        break

# 方法二
while True:
    try:
        a = input()
        b = list(map(int, input().split()))
        c = input()
        d = list(map(int, input().split()))
        print("".join(map(str, sorted(list(set(b + d))))))
    except:
        break
