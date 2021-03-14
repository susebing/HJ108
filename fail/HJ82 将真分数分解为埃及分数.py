# coding=utf-8
"""
题目描述
分子为1的分数称为埃及分数。现输入一个真分数(分子比分母小的分数，叫做真分数)，请将该分数分解为埃及分数。如：8/11 = 1/2+1/5+1/55+1/110。
接口说明
/*
功能: 将分数分解为埃及分数序列
输入参数：
String pcRealFraction:真分数(格式“8/11”)
返回值：
String pcEgpytFraction:分解后的埃及分数序列(格式“1/2+1/5+1/55+1/100”)
*/
public static String  ConvertRealFractToEgpytFract(String pcRealFraction)
{
return null;
}
如有多个解，输出任意一个

输入描述:
输入一个真分数，String型

输出描述:
输出分解后的string

示例1
输入
复制
8/11
输出
复制
1/2+1/5+1/55+1/110
"""

while True:
    try:
        a = input().split('/')
        fz = int(a[0])
        c = []
        for i in range(fz):
            c.append(f'{1}' + '/' + a[1])
        print('+'.join(c))
    except:
        break


# 方法二
def egypt(a, b):
    res = []
    while b % a:
        p, r = b // a, b % a
        res.append('1/' + str(p + 1))
        a -= r
        b *= p + 1
    res.append('1/' + str(b // a))
    return res


while True:
    try:
        a, b = list(map(int, input().split('/')))
        egypt(a, b)
        print('+'.join(egypt(a, b)))
    except:
        break
