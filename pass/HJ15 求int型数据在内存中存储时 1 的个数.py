"""
题目描述
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。

输入描述:
 输入一个整数（int类型）

输出描述:
 这个数转换成2进制后，输出1的个数

示例1
输入
5

输出
2
"""

# 使用 bin 转换成2进制
# 使用 count 统计 '1' 出现的次数

while 1:
    try:
        a = int(input())
        b = bin(a)
        print(b.count('1'))
    except:
        break
