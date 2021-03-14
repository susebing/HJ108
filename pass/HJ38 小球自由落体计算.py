# coding=utf-8
"""
题目描述
假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下,
求它在第5次落地时，共经历多少米?
第5次反弹多高？

最后的误差判断是小数点6位

输入描述:
输入起始高度，int型

输出描述:
分别输出第5次落地时，共经过多少米第5次反弹多高

示例1
输入
复制
1
输出
复制
2.875
0.03125
"""
# 方法一
# 按比例缩放,能过
while 1:
    try:
        num = int(input())
        print(num * 2.875)
        print((num * 0.03125))
    except:
        break

# 方法二
while 1:
    try:
        num = int(input())
        print(num * 2.875)
        print((num / 32))
    except:
        break
