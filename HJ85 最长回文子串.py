# coding=utf-8
"""
题目描述
Catcher 是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？

（注意：记得加上while处理多个测试用例）

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


# 这道题可以使用两种方法，一种是暴力枚举法，时间复杂度为O(n)2。就不介绍了。
# 另一种是（时间复杂度为O（n）。）：
# 理论支持：每当增加一个新的字母，最大回文串的长度只能增加1或者2，不可能增加更多，
# 并且，新的最大回文串必然要包含这个字母！
# 证明：如果新增了一个字母，最大回文串的长度增加了3，这是不可能的，
# 例如：abcdefgfedcba，当增加到最后的b或者a时，是不可能增加3个长度的，
# 因为每增加一个字母，前面必然已经存在一个回文子串，且长度比新串小1或者小2.
# 所以，从头到尾扫描字符串，每增加一个新的字符，判断以这个字符结尾，
# 且长度为maxLen+1或者maxLen+2的子串是否为回文，如果是，更新最大回文子串。

# 注意要判断输入是否为空，如果为空就不要输出0了。。被坑过一次。

def fin(a):
    for i in range(len(a), -1, -1):
        for n in range(0, len(a) - i + 1):
            if a[n:i + n] == a[n:i + n][::-1]:
                return (i)


while True:
    try:
        a = input()
        if a:
            print(fin(a))
    except:
        break


# 方法二
# 本体的精华在：要求最大长度，遍历就从lens+1开始，向前遍历
# 以后算公共的记得用j:j+i，下标这种思路
def password(s):
    lens = len(s)
    s2 = s[::-1]
    for i in range(1, lens + 1)[::-1]:
        for j in range(lens - i + 1):
            temp = s[j:j + i]
            if temp in s2:
                return i


while True:
    try:
        s = input()
        if s:
            print(password(s))
    except:
        break
