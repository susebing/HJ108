# coding=utf-8
"""
题目描述
题目标题：
判断短字符串中的所有字符是否在长字符串中全部出现
详细描述：
接口说明
原型：
boolIsAllCharExist(char* pShortString,char* pLongString);
输入参数：
    char* pShortString：短字符串
    char* pLongString：长字符串

输入描述:
输入两个字符串。第一个为短字符，第二个为长字符。

输出描述:
返回值：

示例1
输入
复制
bc
abc

输出
复制
true
"""

# python两行代码解决，
# 思路：
# 使用set，集合的交。

while True:
    try:
        set1, set2 = set(input()), set(input())
        print("true" if set1 & set2 == set1 else "false")
    except:
        break
