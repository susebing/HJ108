# coding=utf-8
"""
题目描述
•计算一个数字的立方根，不使用库函数
详细描述：
•接口说明
原型：
public static double getCubeRoot(double input)
输入:double 待求解参数
返回值:double  输入参数的立方根，保留一位小数

输入描述:
待求解参数 double类型

输出描述:
输入参数的立方根 也是double类型

示例1
输入
复制
216
输出
复制
6.0
"""

while True:
    try:
        n = float(input())
        t = n
        while abs(t * t * t - n) > 0.0001:
            t = t - (t * t * t - n) * 1.0 / (3 * t * t)
        print(round(t, 1))
    except:
        break
