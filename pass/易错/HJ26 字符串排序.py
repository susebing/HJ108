# coding=utf-8
"""
题目描述
编写一个程序，将输入字符串中的字符按如下规则排序。

规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
如，输入： Type 输出： epTy

规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
如，输入： BabA 输出： aABb

规则 3 ：非英文字母的其它字符保持原来的位置。
如，输入： By?e 输出： Be?y

注意有多组测试数据，即输入有多行，每一行单独处理（换行符隔开的表示不同行）

输入描述:
输入字符串

输出描述:
输出字符串

示例1
输入
复制
A Famous Saying: Much Ado About Nothing (2012/8).

输出
复制
A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).
"""

while True:
    try:
        new = input()
        old = [0] * len(new)
        alpha = []
        for i in range(len(new)):
            if new[i].isalpha():
                alpha.append(new[i])
            else:
                old[i] = new[i]
        alpha.sort(key=lambda x: x.upper())
        for i, v in enumerate(old):
            if not v:
                old[i] = alpha[0]
                alpha.pop(0)
        print(''.join(old))
    except:
        break
