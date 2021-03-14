# coding=utf-8
"""
题目描述
问题描述：给出4个1-10的数字，通过加减乘除，得到数字为24就算胜利
输入：
4个1-10的数字。[数字允许重复，但每个数字仅允许使用一次，测试用例保证无异常数字]
输出：
true or false

输入描述:
输入4个int整数

输出描述:
返回能否得到24点，能输出true，不能输出false

示例1
输入
复制
7 2 1 10
输出
复制
true
"""

# /*思路：采用递归的方式，
# 每次只取两个数做加减乘除运算，并放回数组中,
# 直到数据中只剩下一个数，判断这个数是否等于24*/

def helper(arr, item):
    if item < 1:
        return False
    if len(arr) == 1:
        return arr[0] == item
    for i in range(len(arr)):
        L = arr[:i] + arr[i + 1:]
        v = arr[i]
        if helper(L, item - v) or helper(L, item + v) or helper(L, item * v) or helper(L, item / v):
            return True
    return False


while True:
    try:
        arr = list(map(int, input().split(' ')))
        if helper(arr, 24):
            print("true")
        else:
            print("false")
    except:
        break
