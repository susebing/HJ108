# coding=utf-8
"""
题目描述
Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，
比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。
比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214。
因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），
Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？

输入描述:
输入一个字符串

输出描述:
返回有效密码串的最大长度

示例1
输入
复制
ABBA
输出
复制
4
"""

# 方法一 时间短，代码短
def check(s):
    n = len(s)
    num = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            a = i
            b = i + 1
            while a >= 0 and b < n and s[a] == s[b]:
                a -= 1
                b += 1
            num = max(num, b - a - 1)
        elif s[i - 1] == s[i + 1]:
            a = i - 1
            b = i + 1
            while a >= 0 and b < n and s[a] == s[b]:
                a -= 1
                b += 1
            num = max(num, b - a - 1)
    return num


while True:
    try:
        s = input()
        num = check(s)
        print(num)
    except:
        break


# 方法二
def max_len(string):
    abba = []
    aba = []
    # 遍历寻找对称位置
    for i in range(len(string) - 1):
        current = i
        next_one = i + 1
        if string[current] == string[next_one]:
            abba.append(i)
        elif string[current - 1] == string[next_one]:
            aba.append(i)
    length = []
    for j in abba:
        first = j
        last = j + 1
        while first >= 0 and last < len(string) and string[first] == string[last]:
            first += -1
            last += 1
            # CABBA，第一循环时，符合条件的只有2个字符，而此时last-first=3,所以需要减去1
            length.append(last - first - 1)
    for k in aba:
        first = k - 1
        last = k + 1
        while first >= 0 and last < len(string) and string[first] == string[last]:
            first += -1
            last += 1
            length.append(last - first - 1)
    if len(length) == 0:
        return 0
    else:
        return max(length)


while True:
    try:
        string = input()
        print(max_len(string))
    except:
        break
