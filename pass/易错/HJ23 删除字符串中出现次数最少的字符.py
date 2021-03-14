# coding=utf-8
"""
题目描述
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。
输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
注意每个输入文件有多组输入，即多个字符串用回车隔开

输入描述:
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述:
删除字符串中出现次数最少的字符后的字符串。

示例1
输入
复制
abcdd
输出
复制
dd
"""

# 首先计算出最少次数是多少
# 遍历每个字符，如果次数等于最少，则不加入结果数组，否则加入结果数组

while 1:
    try:
        res = []
        s = input()
        min_time = min([s.count(c) for c in s])
        for c in list(s):
            if s.count(c) == min_time:
                pass
            else:
                res.append(c)
        print(''.join(res))
    except:
        break


