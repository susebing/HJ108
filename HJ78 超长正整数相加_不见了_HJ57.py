# coding=utf-8
"""
题目描述
请设计一个算法完成两个超长正整数的加法。

接口说明
/*
请设计一个算法完成两个超长正整数的加法。
输入参数：
String addend：加数
String augend：被加数
返回值：加法结果
*/
public String AddLongInteger(String addend, String augend)
{
/*在这里实现功能*/
return null;
}
本题有多组输入数据，请使用while(cin>>)等方式读取

输入描述:
输入两个字符串数字

输出描述:
输出相加后的结果，string型

示例1
输入
复制
99999999999999999999999999999999999999999999999999
1
输出
复制
100000000000000000000000000000000000000000000000000
"""


# 华为OJ平台——超长正整数相加
while 1:
    try:
        a = int(input())
        b = int(input())
        print(a+b)
    except:
        break