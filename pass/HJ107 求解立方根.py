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

# 牛顿迭代法。设f(x)=x3-y, 求f(x)=0时的解x，即为y的立方根。
# 根据牛顿迭代思想，xn+1=xn-f(xn)/f'(xn)即x=x-(x3-y)/(3*x2)=(2*x+y/x/x)/3;

while True:
    try:
        n = float(input())
        t = n
        while abs(t * t * t - n) > 0.0001:
            t = t-(t**3-n)*1.0/(3*t**2)
        print(round(t, 1))
    except:
        break
