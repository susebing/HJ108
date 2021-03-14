# coding=utf-8
"""
题目描述
功能: 求一个byte数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1
输入: 一个byte型的数字

输出: 无
返回: 对应的二进制数字中1的最大连续数

输入描述:
输入一个byte数字

输出描述:
输出转成二进制之后连续1的个数

示例1
输入
复制
3
输出
复制
2
"""

while 1:
    try:
        bin_arr = [len(item) for item in bin(int(input()))[2:].split('0') if item]
        print(max(bin_arr))
    except:
        break


