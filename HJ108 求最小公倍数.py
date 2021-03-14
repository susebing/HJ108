# coding=utf-8
"""
题目描述
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。

输入描述:
输入两个正整数A和B。

输出描述:
输出A和B的最小公倍数。

示例1
输入
复制
5 7
输出
复制
35
"""

# a*b = 最小公倍数*最大公约数
# 最小公倍数 = 两数之积除以最大公约数

# 求最小公倍数：公式法
# 两个数a,b的最小公倍数是a*b/gcd(a,b)
# 由于两个数的乘积等于这两个数的最大公约数与最小公倍数的积，即（a，b）× [a，b] = a × b
# 所以，求两个数的最小公倍数，就可以先求出它们的最大公约数，然后用上述公式求出它们的最小公倍数。

while True:
    try:
        a, b = map(int, input().split())
        r = a * b
        for i in range(2, min(a, b)):
            if (a % i == 0 and b % i == 0):
                r = r / i
        print(int(r))
    except:
        break


# 方法二
# 这道题把math库给禁了，只好自己实现gcd和lcm。。
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


while True:
    try:
        a, b = map(int, input().split())
        print(lcm(a, b))
    except:
        break
