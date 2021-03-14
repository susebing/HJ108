# coding=utf-8
"""
题目描述
Levenshtein 距离，又称编辑距离，指的是两个字符串之间，由一个转换成另一个所需的最少编辑操作次数。许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。编辑距离的算法是首先由俄国科学家Levenshtein提出的，故又叫Levenshtein Distance。

Ex：
字符串A:abcdefg
字符串B: abcdef
通过增加或是删掉字符”g”的方式达到目的。这两种方案都需要一次操作。把这个操作所需要的次数定义为两个字符串的距离。

要求：
给定任意两个字符串，写出一个算法计算它们的编辑距离。
请实现如下接口
/*  功能：计算两个字符串的距离
 *  输入： 字符串A和字符串B
 *  输出：无
 *  返回：如果成功计算出字符串的距离，否则返回-1
 */
     public   static   int  calStringDistance (String charA, String  charB)
    {
        return  0;
    }

输入描述:
输入两个字符串

输出描述:
得到计算结果

示例1
输入
复制
abcdefg
abcdef
输出
复制
1
"""


def compare(a, b):
    m, n = len(a), len(b)
    dp = list(range(n + 1))
    for i in range(1, m + 1):
        pre = dp[::]
        dp[0] = i
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[j] = pre[j - 1]
            else:
                dp[j] = min(pre[j], pre[j - 1], dp[j - 1]) + 1
    return dp[-1]


while True:
    try:
        a = input()
        b = input()
        if a == '' or b == '':
            print(abs(len(a) - len(b)))
        else:
            print(compare(a, b))
    except:
        break
