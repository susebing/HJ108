# coding=utf-8
"""
题目描述
请实现如下接口
public static int findNumberOf1( int num)
{
/* 请实现 */
return 0;
} 譬如：输入5 ，5的二进制为101，输出2
涉及知识点：
注意多组输入输出！！！！！！

输入描述:
输入一个整数

输出描述:
计算整数二进制中1的个数

示例1
输入
复制
5
输出
复制
2
"""

while True:
    try:
        print(bin(int(input())).count('1'))
    except:
        break