"""
题目描述
计算字符串最后一个单词的长度，单词以空格隔开。
输入描述:
一行字符串，非空，长度小于5000。

输出描述:
整数N，最后一个单词的长度。

示例1
输入
复制
hello world
输出
复制
5
"""

# split 分割
# -1 取最后一个
# len 求长度

while 1:
    try:
        print(len(input().split()[-1]))
    except:
        break
